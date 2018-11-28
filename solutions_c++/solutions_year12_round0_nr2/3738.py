#include <stdio.h>

FILE *fin = fopen ("B-large.in","r");
FILE *fout = fopen ("b.out","w");

int main () {
  int t,n,s,p;
  fscanf (fin,"%d",&t);
  
  for (int i = 1; i <= t; i++) {
    fscanf (fin,"%d%d%d",&n,&s,&p);
    
    int sol = s;
    
    int upper_bound = 3*p - 2;
    int lower_bound = 3*p - 4;
    
    if (upper_bound < 0) upper_bound =0;
    if (lower_bound < 0) lower_bound = upper_bound;
    
    for (int j = 1; j <= n; j++) {
      int score;
      fscanf (fin,"%d",&score);
      
      if (score >= upper_bound) sol++;
      else if (score >= lower_bound) s--;      
    }
    
    if (s > 0) sol= sol - s;
    
    fprintf (fout,"Case #%d: %d\n",i,sol);
  }
  
  return 0;
}
