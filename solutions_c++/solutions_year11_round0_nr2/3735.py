#pragma once
#ifndef MAGICKA_H_INCLUDED
#define MAGICKA_H_INCLUDED

#include <cstdlib>
#include <cstdio>
#include <windows.h>

#include <list>

struct Com {
  char e1;
  char e2;
  char pd;
};

struct Cnc {
  char e1;
  char e2;
};

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

  unsigned int T;
  fscanf(infile, "%d", &T);
  //printf("T: %d\n", T);

  for(unsigned int t = 0; t < T; ++t) {
    unsigned int C;
    fscanf(infile, "%d", &C);
    //printf("C: %d\n", C);

    //allocate combination structs
    Com* coms = new Com[C];
    for(unsigned int c = 0; c < C; ++c) {
      fscanf(infile,"%s",(char*)(&coms[c]));
      //printf("e1: %c\n",coms[c].e1);
    }

    unsigned int D;
    fscanf(infile, "%d", &D);
    //printf("D: %d\n", D);

    //allocate cancel structs
    Cnc* cncs = new Cnc[D];
    for(unsigned int d = 0; d < D; ++d) {
      fscanf(infile,"%s",(char*)(&cncs[d]));
    }

    unsigned int N;
    fscanf(infile, "%d", &N);
    //printf("N: %d\n", N);

    size_t stackptr = 0;
    size_t stacksize = N;
    char* stack = (char*)malloc(stacksize * sizeof(char));

    char* string = (char*)malloc((stacksize*3) * sizeof(char));
    fscanf(infile, "%s", string);


    for(unsigned int n = 0; n < N; ++n) {
      char chr = string[n];
      //printf("|%c|", chr);
      stack[stackptr] = chr;
      unsigned int curr = stackptr;
      unsigned int prev = stackptr-1;
      ++stackptr;
      if(stackptr > 1) {
        for(unsigned int comi = 0; comi < C; ++comi) {
          if((chr == coms[comi].e1 && stack[prev] == coms[comi].e2)
          || (chr == coms[comi].e2 && stack[prev] == coms[comi].e1)) {
            stack[prev] = coms[comi].pd;
            --stackptr;
            --curr;
            --prev;
          }
        }
      }
      if(stackptr > 1) {
        unsigned int i;
        for(unsigned int cnci = 0; cnci < D; ++cnci) {
          if(cncs[cnci].e1 == stack[curr]) {
            for(i = 0; i <= prev; ++i) {
              if(cncs[cnci].e2 == stack[i]) {
                stackptr = 0;
                goto lbl_finloop;
              }
            }
          }
          else if(cncs[cnci].e2 == stack[curr]) {
            for(i = 0; i <= prev; ++i) {
              if(cncs[cnci].e1 == stack[i]){
                stackptr = 0;
                goto lbl_finloop;
              }
            }
          }

        }
      }


      lbl_finloop:
      ;

    }

    delete[] coms;
    delete[] cncs;

    fprintf(outfile , "Case #%d: [" ,t+1);
    for(unsigned int s = 0; s < stackptr; ++s) {
      fprintf(outfile , "%c", stack[s]);
      if(s != stackptr-1)
        fprintf(outfile , ", ");
    }
    fprintf(outfile , "]\n");

    free(stack);
    free(string);
  }

  fclose(infile);
  fclose(outfile);

}

#endif // MAGICKA_H_INCLUDED
