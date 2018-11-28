
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
#include <assert.h>
#include <stdio.h>

#if USE_CPPSTREAM
std::istream& GetIStream(int argc, const char* argv[]) {
  if(argc<2) return std::cin;
  static std::ifstream fin(argv[1]);
  assert(fin);
  return fin;
}
std::ostream& GetOStream(int argc, const char* argv[]) {
  if(argc<3) return std::cout;
  static std::ofstream fout(argv[2]);
  assert(fout);
  return fout;
}
#else
FILE* GetIStream(int argc, const char* argv[]) {
  if(argc<2) return stdin;
  FILE* fin=fopen(argv[1],"rt");
  assert(fin);
  return fin;
}
FILE* GetOStream(int argc, const char* argv[]) {
  if(argc<3) return stdout;
  FILE* fout=fopen(argv[2],"wb");
  assert(fout);
  return fout;
}
#endif

int M,N;
bool init_map[512][512];
int size_map[512][512];

using std::max;
using std::min;

void TestSize(int i, int j) {
  int at_least = size_map[i][j];
  int valid_size=at_least;
  //int size=at_least+1;
  const bool color = init_map[i][j];
  bool finished=false;
  while(!finished) {
    if(i+valid_size>=M || j+valid_size>=N) break;
    if(init_map[i+valid_size][j+valid_size]!=color) break;
    for(int k=0;k<valid_size;++k) {
      if( (init_map[i+k][j+valid_size]!=color)==(((k+valid_size)&1)==0) ) {
        finished=true;
        break;
      }
      if( (init_map[i+valid_size][j+k]!=color)==(((k+valid_size)&1)==0) ) {
        finished=true;
        break;
      }
    }
    if(!finished) ++valid_size;
  }
  if(valid_size>at_least) {
    for(int k=0; k<valid_size-1; ++k) {
      for(int m=0; m<valid_size-1; ++m) {
        size_map[i+k][j+m]=max(size_map[i+k][j+m],valid_size-max(k,m));
      }
    }
  }
}
void RemoveBoard(int i, int j) {
  const int size= size_map[i][j];
  for(int k=0; k<size; ++k) {
    for(int m=0; m<size; ++m) {
      size_map[i+k][j+m]=0;
    }
  }
  for(int k=1; k<size; ++k) {
    for(int m=-k; m<size; ++m) {
      if(i-k>=0 && j+m>=0) size_map[i-k][j+m]=min(k,size_map[i-k][j+m]);
      if(j-k>=0 && i+m>=0) size_map[i+m][j-k]=min(k,size_map[i+m][j-k]);
    }
  }
}
std::vector<std::pair<int,int> > solutions;
void SolvePb(FILE* out, int case_num) {
  for(int i=0; i<M; ++i) {
    for(int j=0; j<N; ++j) {
      size_map[i][j]=1;
    }
  }
  for(int i=0; i<M; ++i) {
    for(int j=0; j<N; ++j) {
      TestSize(i,j);
    }
  }
  solutions.clear();
  int cur_size=513;
  int cur_num=0;
  while(true) {
    int maxS=0;
    int maxPx=0; int maxPy=0;
    for(int i=0; i<M; ++i) {
      for(int j=0; j<N; ++j) {
        if(size_map[i][j]>maxS) {
          maxS=size_map[i][j]; maxPx=i; maxPy=j;
          if(maxS>=cur_size) break;
        }
      }
    }
    RemoveBoard( maxPx,maxPy);
    assert(maxS<=cur_size);
    if(maxS<cur_size) {
      if(cur_num!=0) {
        solutions.push_back(std::make_pair(cur_size, cur_num));
      }
      cur_size=maxS;
      cur_num=0;
    }
    cur_num++;
    if(maxS==0) break;
  }
  fprintf(out, "Case #%i: %i\n", case_num+1, solutions.size());
  for(int i=0; i<solutions.size(); ++i) {
    fprintf(out,"%i %i\n", solutions[i].first, solutions[i].second);
  }
}


int main(int argc, const char* argv[]) {
  
#if USE_CPPSTREAM
  std::istream& in = GetIStream(argc,argv);
  std::ostream& out = GetOStream(argc,argv);

  std::string stmp;
  while(!in.eof()) {
    in >> stmp;
    out << stmp;
  }

#else
  FILE* in = GetIStream(argc,argv);
  FILE* out = GetOStream(argc,argv);

  char buf[256];
  int T;
  fscanf(in,"%i",&T);
  for(int i=0; i<T; ++i) {
    fscanf(in,"%i %i",&M,&N);
    fgets(buf, 255, in);
    for(int j=0; j<M; ++j) {
      fgets(buf, 255, in);
      for(int k=0; k<N; k+=4) {
        int v;
        switch(buf[k/4]) {
          case '0':case '1':case '2':case '3':case '4':case '5':case '6':case '7':
          case '8':case '9': v=buf[k/4]-'0'; break;
          case 'A':case 'B':case 'C':case 'D':case 'E':case 'F':
            v=buf[k/4]-'A'+10; break;
          default:
            assert(0);
        }
        init_map[j][k]= (v&8)!=0;
        init_map[j][k+1]= (v&4)!=0;
        init_map[j][k+2]= (v&2)!=0;
        init_map[j][k+3]= (v&1)!=0;
      }
    }
    SolvePb(out,i);
    //fprintf(out, "Case #%i: %s\n", i+1, result?"ON":"OFF");
  }

#endif


  return 0;
}

