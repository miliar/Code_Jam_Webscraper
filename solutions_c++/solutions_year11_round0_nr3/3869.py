#pragma once
#ifndef CANDY2_H_INCLUDED
#define CANDY2_H_INCLUDED

#include <cstdlib>
#include <cstdio>
#include <windows.h>

#include <list>


unsigned int max;
unsigned int N;
unsigned int* cv;

void branch(unsigned int pA, unsigned int pB, unsigned int sA, unsigned int pos, unsigned int num) {
  pA ^= cv[pos];
  sA += cv[pos];
  if(num == 0) {
    for(unsigned int n = pos+1; n < N; ++n) {
      pB ^= cv[n];
    }
    if(pA == pB) {
      if(sA > max)
        max = sA;
    }
    return;
  }

  for(unsigned int n = pos+1; n < N; ++n) {
    branch(pA,pB,sA,n, num-1);
    pB ^= cv[n];
  }
  return;
}


int main_entry(int argc, char *argv[]) {
  if(argc < 2) { //exit if not given infile
    fputs("no infile",stderr);
    system("PAUSE");
    exit(1);
  }
  if(argc > 2) { //exit if multiple infiles given
    fputs("too many infiles",stderr);
    system("PAUSE");
    exit(1);
  }

  //open the infile
  FILE* infile = fopen(argv[1],"rb");
  if(!infile) { //exit if there is error
    perror("infile could not be opened");
    system("PAUSE");
    exit(2);
  }

  //open the outfile
  FILE* outfile = fopen("output.txt","w");

  unsigned int T; //T test cases follow
  fscanf(infile, "%i", &T);

  for(unsigned int t = 0; t < T; ++t) {
    printf("T: %i\n", t);

    fprintf(outfile , "Case #%d: " ,t+1);

    fscanf(infile, "%d", &N);

    cv = new unsigned int[N];
    unsigned int A = 0;

    for(unsigned int n = 0; n < N; ++n) {
      fscanf(infile, "%u", &cv[n]);
      A ^= cv[n];
    }
    if(A != 0) {
      fprintf(outfile , "NO\n");
      continue;
    }

    max = 0;

    unsigned int pB = 0;
    for(unsigned int p = 0; p < N; ++p) {
      for(unsigned int n = 0; n < N-1; ++n) {
        branch(0,pB,0,p,n);
      }
      pB ^= cv[p];
    }

    fprintf(outfile , "%i\n",max);



    delete[] cv;
  }



  return 0;
}


#endif // CANDY2_H_INCLUDED
