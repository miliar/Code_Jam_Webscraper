#include <stdio.h>


int n,m;

int board [50][50];


bool check (int j , int k) {
  if (j+1 >= n) return false;
  
  if (k+1 >= m) return false;
  
  return board [j][k+1] == 1 && board [j+1][k] == 1 && board [j+1][k+1] == 1;
}

int main () {
  FILE *in = fopen ("A-large.in","r");
  FILE *out = fopen ("a.out","w");
  
  int t;
  
  fscanf (in,"%d",&t);        
  
  for (int i = 1; i <= t; i++) {
    fscanf (in,"%d %d",&n,&m);
    char temp;
    
    for (int j = 0; j < n; j++) {
      fscanf (in,"%c",&temp);
      for (int k = 0; k < m; k++) {
        fscanf (in,"%c",&temp);
        
        if (temp == '.') board [j][k] = 0;
        else board [j][k] = 1;
      }
    }
    
    bool imp = false;
    
    for (int j = 0; j < n; j++)
      for (int k =0; k < m; k++)
        if (board [j][k] == 1) {
          if (check (j,k)) {
            board [j][k] = 2;
            board [j][k+1] = 3;
            board [j+1][k] = 4; board [j+1][k+1] = 5;
          }
          else {
            imp = true;
            j = n; k = m;
          }
        }
        
    fprintf (out,"Case #%d:\n",i);
    if (imp)
      fprintf (out,"Impossible\n");
    else {
      for (int j = 0; j < n; j++) {
        for (int k = 0; k < m; k++) {
          if (board[j][k] == 0)
            fprintf (out,".");
          else if (board [j][k] == 2 || board [j][k] == 5)
            fprintf (out,"/");
          else fprintf (out,"\\");
        }
        fprintf (out,"\n");
      }
    }
  }
  
  fclose (in);
  fclose (out);
  return 0;
}
