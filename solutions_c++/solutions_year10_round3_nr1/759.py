#include <stdio.h>

using namespace std;

#include <iostream>

int n;

typedef struct{
        int a;
        int b;
}wire;

wire wires[1000];

int solution () {
  if (wires[0].a < wires[1].a) {
    if (wires[0].b < wires[1].b)
      return 0;
    else return 1;
  }
  else {
    if (wires [0].b < wires[1].b)
      return 1;
  }
  
  return 0;
}

int main () {
  FILE *fin = fopen ("A-small-attempt0.in","r");
  FILE *fout = fopen ("A-small-attempt0.out","w");
  
  int t;
  
  fscanf (fin,"%d",&t);
  
  for (int i = 1; i <= t; i++) {   
    fscanf (fin,"%d",&n);
    
    for (int j = 0; j < n; j++) {
      fscanf (fin,"%d %d",&wires[j].a , &wires[j].b);
    }             
    
    fprintf (fout,"Case #%d: %d\n",i,solution()); 
  }
  
  fclose (fin);
  fclose (fout);
  
  return 0;
}
