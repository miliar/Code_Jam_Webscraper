
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
#include <stdint.h>

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

int R;
int k;
int N;
int group_size[1000];
int prevrun_startgrp[1000];
int64_t revenu_at_run[1000];


int64_t ProcessTestCase() {
  int grp_head=0;
  int64_t res=0;
  memset(prevrun_startgrp,0xFF,sizeof(int)*N);
  for(int i=0; i<R; ++i) {
    revenu_at_run[i]=res;
    int cursize = 0;
    int cur_start=grp_head;
    if(prevrun_startgrp[cur_start]<0) {
      prevrun_startgrp[cur_start]=i;
      while(cursize+group_size[grp_head]<=k) {
        cursize+=group_size[grp_head];
        grp_head=(grp_head+1)%N;
        if(grp_head==cur_start) break;
      }
      res+=cursize;
    } else {
      const int prevrun = prevrun_startgrp[cur_start];
      const int dist = i-prevrun;
      const int64_t rev=res-revenu_at_run[prevrun];
      const int fullserie = (R-i)/dist;
      const int reminder = (R-i)%dist;
      return res+fullserie*rev+(revenu_at_run[prevrun+reminder]-revenu_at_run[prevrun]);
    }
  }
  return res;
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

  int T;
  fscanf(in,"%i",&T);
  for(int i=0; i<T; ++i) {
    fscanf(in,"%i %i %i",&R,&k,&N);
    for(int i=0; i<N; ++i) fscanf(in,"%i",group_size+i);

    int64_t res = ProcessTestCase();

    fprintf(out, "Case #%i: %lli\n", i+1, res);
  }

#endif


  return 0;
}

