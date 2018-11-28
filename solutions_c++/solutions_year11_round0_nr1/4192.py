#pragma once
#ifndef ROBOT_H_INCLUDED
#define ROBOT_H_INCLUDED

#include <cstdlib>
#include <cstdio>
#include <windows.h>

#include <stack>

enum I {
  none,
  forw,
  back,
  stay,
  push
};


struct Inst {
  bool robot;
  char button;
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

  unsigned int T; //T test cases follow
  fscanf(infile, "%i", &T);

  for(unsigned int t = 0; t < T; ++t) {
    printf("T: %i\n", t);

    unsigned int N; //N instructions follow
    fscanf(infile, "%i", &N);
    //printf("N: %i\n", N);

    Inst* insts = new Inst[N];
    unsigned int instsN = 0;

    for(unsigned int n = 0; n < N; ++n) {
      char chr;
      fscanf(infile,"%s",&chr);
      //printf("C: %c\n",chr);
      if(chr == 'O')
        insts[instsN].robot = 0;
      else
        insts[instsN].robot = 1;

      int it;

      fscanf(infile,"%d",&it);
      insts[instsN].button = it;
      //printf("B: %i\n", insts[instsN].button);
      ++instsN;
    }

    unsigned int s = 0;
    unsigned int buttons = 0;
    unsigned int p[2];
    p[0] = 1;
    p[1] = 1;
    while(buttons < N) {
      ++s;
      //I cm[2];
      //cm[0] = none;
      //cm[1] = none;

      Inst* curr;
      Inst* next;

      curr = &insts[buttons];
      next = NULL;
      unsigned int nextn = 0;
      for(unsigned int n = buttons+1; n < N; ++n) {
        if(insts[n].robot != curr->robot) {
          next = &insts[n];
          nextn = n;
          break;
        }
      }


      //move
      if(p[curr->robot] != (unsigned int)curr->button) {
        if((p[curr->robot] < (unsigned int)curr->button)) {
          //cm[curr->robot] = forw;
          ++p[curr->robot];
        }
        else {
          //cm[curr->robot] = back;
          --p[curr->robot];
        }
      }
      else {
        //cm[curr->robot] = push;
        ++buttons;
      }

      if(next) {
        if(p[next->robot] != (unsigned int)next->button) {
          if((p[next->robot] < (unsigned int)next->button)) {
            //cm[next->robot] = forw;
            ++p[next->robot];
          }
          else {
            //cm[next->robot] = back;
            --p[next->robot];
          }
        }
      }

    }
    delete[] insts;

    fprintf(outfile , "Case #%i: %i\n" ,t+1, s);
  }




  fclose(infile);
  fclose(outfile);
  return 0;
}


#endif // ROBOT_H_INCLUDED
