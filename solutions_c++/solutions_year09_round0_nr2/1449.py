#include <stdio.h>

int T, H, W;
int t;
int i, j;
int a[100][100];
int b[100][100];
int c;

int srch(int i, int j)
{
   int min_v = a[i][j];
   int n_i = i, n_j = j;
  
   if (i-1 >= 0 && a[i-1][j] < min_v) {
     min_v = a[i-1][j];
     n_i = i-1; n_j = j;  
   }
   if (j-1 >= 0 && a[i][j-1] < min_v) {
     min_v = a[i][j-1];
     n_i = i; n_j = j-1;  
   }
   if (j+1 < W && a[i][j+1] < min_v) {
     min_v = a[i][j+1];
     n_i = i; n_j = j+1;  
   }
   if (i+1 < H && a[i+1][j] < min_v) {
     min_v = a[i+1][j];
     n_i = i+1; n_j = j;  
   }

   if (i == n_i && j == n_j) {
     c++;
     b[i][j] = c;
     return c; 
   }

   if (b[n_i][n_j] != 0) {
     b[i][j] = b[n_i][n_j];
     return b[i][j];
   }   

   b[i][j] = srch(n_i, n_j);
   return b[i][j];
}

int main() {

  scanf("%d", &T);
  
  for (t = 1; t <= T; t++) { 
    scanf("%d %d", &H, &W);

    for (i = 0; i < H; i++)
      for (j = 0; j < W; j++) {
        scanf("%d", &a[i][j]);
        b[i][j] = 0;
      }

    c = 0;
    for (i = 0; i < H; i++)
      for (j = 0; j < W; j++)
        if (b[i][j] == 0) {          
          srch(i, j);  
        } 

    printf("Case #%d:\n", t); 
    for (i = 0; i < H; i++) {
      for (j = 0; j < W-1; j++)
        printf("%c ", (char)('a' + b[i][j] - 1));
      printf("%c\n", (char)('a' + b[i][W-1] - 1)); 
    }
    
    
  }

  return 0;
}