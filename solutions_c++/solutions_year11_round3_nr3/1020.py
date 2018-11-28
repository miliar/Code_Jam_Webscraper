#include <stdio.h>


int n,l,h;

int nums[100];

int main () {
  FILE *in = fopen ("C-small-attempt0.in","r");
  FILE *out = fopen ("c.out","w");
  
  int t;
  
  fscanf (in,"%d",&t);        
  
  for (int i = 1; i <= t; i++) {    
    fscanf (in,"%d %d %d",&n,&l,&h);    
    
    for (int j = 0; j < n; j++) {
      fscanf (in,"%d",&nums[j]);   
    }
    
    int sol = -1;
    
    for (int j = l; j <= h; j++) {
      bool is_ok = true;
      for (int k = 0; k < n; k++)
        if (j % nums[k] != 0 && nums[k] % j != 0) {
          is_ok = false;
          k = n;
        }
        
      if (is_ok) {sol = j; j = h+1;}
    }         
      
    fprintf (out,"Case #%d: ",i);
    
    if (sol != -1)
      fprintf (out,"%d\n",sol);
    else
      fprintf (out,"NO\n");
  }
  
  fclose (in);
  fclose (out);
  return 0;
}
