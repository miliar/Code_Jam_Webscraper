#include <stdio.h>

using namespace std;

#include <iostream>

int l,p,c;

int points[32];

int find (int ini, int fin) {
  if (ini > fin) return 0;
  
  if (ini == fin) return 1;
  
  int med = (ini+fin)/2;
  
  int r1 = find (ini,med-1);
  int r2 = find (med+1,fin);
  
  if (r1 > r2)
    return r1+1;
    
  return r2+1;
}

int solution () {  
  int value = l*c;          
    
  int cont = 0;
  
  while (value < p) {
    cont++;
    
    value = value*c;
  }
      
  return find (0,cont-1);
}

int main () {
  FILE *fin = fopen ("B-small-attempt0.in","r");
  FILE *fout = fopen ("B-small-attempt0.out","w");
  
  int t;
  
  fscanf (fin,"%d",&t);
  
  for (int i = 1; i <= t; i++) {   
    fscanf (fin,"%d %d %d",&l,&p,&c);                     
    
    fprintf (fout,"Case #%d: %d\n",i,solution()); 
  }
  
  fclose (fin);
  fclose (fout);
  
  return 0;
}
