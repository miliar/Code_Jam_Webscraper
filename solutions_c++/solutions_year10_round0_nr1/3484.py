#include <stdio.h>

int k,n;

int main () {
  FILE *fin = fopen("A-large.in","r");    
  FILE *fout = fopen("A-large.out","w");
  
  int t;
  
  fscanf (fin,"%d",&t);
  for (int i = 1; i <= t; i++) {
    fscanf (fin,"%d %d",&n,&k);            
    
    int pot = 1 << (n);
    
    if ((k-pot+1)%pot == 0)
      fprintf (fout,"Case #%d: ON",i);
    else
      fprintf (fout,"Case #%d: OFF",i);
      
    fprintf (fout,"\n");
  }
  
  fclose (fin);
  fclose (fout);
  return 0;
}
