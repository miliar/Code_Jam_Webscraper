
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

int main(int argc, const char* argv[]) {
  
#if USE_CPPSTREAM
  std::istream& in = GetIStream(argc,argv);
  std::ostream& out = GetOStream(argc,argv);


#else
  FILE* in = GetIStream(argc,argv);
  FILE* out = GetOStream(argc,argv);
  
  int T;
  fscanf(in,"%i",&T);
  for(int i=0; i<T; ++i) {
    int N;
    fscanf(in,"%i",&N);

    std::map<int,int> lines;
    for(int j=0; j<N; ++j) {
      int A,B;
      fscanf(in,"%i %i",&A, &B);
      lines.insert(std::make_pair(A,B));
    }
    int result=0;
    for(std::map<int,int>::const_iterator it=lines.begin(),
      end=lines.end(); it!=end; ++it)
    {
      const int ref = it->second;
      for(std::map<int,int>::const_iterator it2=lines.begin();
        it2!=it; ++it2)
      {
        if(it2->second>ref) ++result;
      }
    }
    
    fprintf(out, "Case #%i: %i\n", i+1, result);
  }
#endif


  return 0;
}

