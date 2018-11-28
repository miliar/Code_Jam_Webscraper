#include <stdio.h>

int main () {
  int t;
  int n;
  
  FILE *in = fopen ("C-large.in","r");
  FILE *out = fopen ("c.out","w");  
  
  fscanf (in,"%d",&t);
  
  for (int i = 1; i <= t; i++) {
    fscanf (in,"%d",&n);
    
    int elem;
    fscanf (in,"%d",&elem);
    int sum = elem;
    int less = elem;
    int xtotal = elem;
        
    for (int j = 2; j <= n; j++) {
      fscanf (in,"%d",&elem);
      
      if (elem < less) less = elem;
      sum += elem;
      xtotal = xtotal ^ elem;
    }
      
    fprintf (out,"Case #%d: ",i);
    
    if (xtotal != 0) 
      fprintf (out,"NO");
    else {
      sum -= less;
      fprintf (out,"%d",sum);
    }
    
    if (i  < t) fprintf (out,"\n");
  }
  
  fclose (in);
  fclose (out);
  return 0;
}
