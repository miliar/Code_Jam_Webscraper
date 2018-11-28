#include <stdio.h>
#include <stdlib.h>


int d,m,i,n;

int pix[101];

int cost [256][101];

int solution () {
  for (int h = 1; h <= 255; h++)
    cost [h][0] = 0;    
      
  for (int h = 1; h <= n; h++) {    
    for (int j = 0; j <= 255; j++) {
      cost [j][h] = -1;
      int abs_value = abs (j-pix[h]);
      
      for (int k = 0; k <= 255; k++) {          
        int diff = abs(k-j);  
        
        for (int q = h-1; q >= 0; q--) {
          int partial_value = abs_value + (h-q-1)*d + cost[k][q];
          
          if (diff > m) {
            if (m == 0) {
              partial_value = -1;
            }
            else {
              partial_value += diff/m*i - i;
              if (diff%m != 0) partial_value += i;
            }
          }
          
          if (partial_value != -1 && (cost [j][h] == -1 || cost [j][h] > partial_value))
            cost [j][h] = partial_value;
        }
      }
    }
  }
  
  int max = cost [0][n];
  
  for (int i = 1; i <= 255; i++)
    if (cost [i][n] < max)
      max = cost [i][n];
  
  return max;
}

int main () {
  FILE *fin = fopen ("B-small-attempt3.in","r");
  FILE *fout = fopen ("B-small-attempt3.out","w");
  
  int t;
  
  fscanf (fin,"%d",&t);
  
  for (int h = 1; h <= t; h++) {
    fscanf (fin,"%d %d %d %d",&d,&i,&m,&n);
    
    for (int j = 1; j <= n; j++)
      fscanf (fin,"%d",&pix[j]);
      
    fprintf (fout,"Case #%d: ",h);
    
    fprintf (fout,"%d\n",solution());
  }
  
  fclose (fin);
  fclose (fout);
  
  return 0;
}
