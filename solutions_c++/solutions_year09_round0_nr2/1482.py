#include <cstdio>
#include <cstring>

int T, H, W, t, i, j;
int A[128][128];
char C[128][128], c;

char curge(int x, int y)
{
 if (C[x][y] != 0) return C[x][y];
 if (A[x-1][y] < A[x][y] && A[x-1][y] <= A[x][y-1] && A[x-1][y] <= A[x+1][y] && A[x-1][y] <= A[x][y+1])
    C[x][y] = curge(x-1,y);
 else
     if (A[x][y-1] < A[x][y] && A[x][y-1] <= A[x-1][y] && A[x][y-1] <= A[x+1][y] && A[x][y-1] <= A[x][y+1])
        C[x][y] = curge(x, y-1);
     else         
         if (A[x][y+1] < A[x][y] && A[x][y+1] <= A[x-1][y] && A[x][y+1] <= A[x+1][y] && A[x][y+1] <= A[x][y-1])
            C[x][y] = curge(x, y+1);
         else   
            if (A[x+1][y] < A[x][y] && A[x+1][y] <= A[x-1][y] && A[x+1][y] <= A[x][y-1] && A[x+1][y] <= A[x][y+1])
               C[x][y] = curge(x+1, y);         
            else C[x][y] = c, ++c;
 return C[x][y];
}

int main()
{
 freopen("b.in","r",stdin);
 freopen("b.out","w",stdout);
 
 scanf("%d",&T);
 for (t=1; t<=T; ++t)
     {
      scanf("%d %d",&H,&W);
      for (i=1; i<=H; ++i)
          for (j=1; j<=W; ++j)
              scanf("%d",&A[i][j]);
      for (i=1; i<=H; ++i)
          A[i][0] = A[i][W+1] = 10001;
      for (j=1; j<=W; ++j)
          A[0][j] = A[H+1][j] = 10001;
              
      memset(C, 0, sizeof(C));
      c = 'a';
      
      for (i=1; i<=H; ++i)
          for (j=1; j<=W; ++j)
              if (C[i][j] == 0)
                 C[i][j] = curge(i,j);
      printf("Case #%d:\n", t);
      for (i=1; i<=H; ++i)
          {
           for (j=1; j<=W; ++j)
               printf("%c ",C[i][j]);
           printf("\n");
          }
     }
 
 
 return 0;
}
