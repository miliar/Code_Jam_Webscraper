#include<iostream>
using namespace std;
int N, K;
char M[128][128];
int dx[4] = {1, 1, 0, -1};
int dy[4]= {0, 1, 1, 1};
bool Check(char c)
{
     int i, j, k, d;
     int y, x;
     for(i = 1; i <= N;++i)
       for(j = 1; j <= N; ++j) for(d = 0; d < 4; ++d)
       {
           y = i, x = j;
           for(k = 1; k <= K; ++k)
           {
               if(y < 1 || y > N || x < 1 || x > N) break;
               if(M[y][x] != c) break;
               y += dy[d];
               x += dx[d];
           }
           if(k > K) return 1;
       }
       return 0;
}
int main()
{
    int t, cs = 0;
    int i, j, k;
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &N, &K);    
         for(i = 1; i <= N; ++i)
            scanf("%s", M[i] + 1);
         
         for(i = 1; i <=N; ++i)
         {
             k = N;
             for(j = N; j >= 1; --j)
                 if(M[i][j] != '.')
                     M[i][k--] = M[i][j];
             for(j = k; j >= 1; --j)
                 M[i][j] = '.';
         }
         
         bool R=0, B=0;
         if(Check('R')) R = 1;
         if(Check('B')) B = 1;
         
         printf("Case #%d: ", ++cs);
         if(R && B)
         {
              printf("Both\n");
          }
          else if(R)
          
          {
               printf("Red\n");
           }
           else if(B)
           {
                printf("Blue\n");
            }
            else
            {
                printf("Neither\n");
            }
        
         
    /*     for(i = 1; i <= N; ++i)
            printf("%s\n", M[i] + 1);*/
    }
}
/*
7 3
.......
.......
.......
...R...
...BB..
..BRB..
.RRBR..
6 4
......
......
.R...R
.R..BB
.R.RBR
RB.BBB
4 4
R...
BR..
BR..
BR..
3 3
B..
RB.
RB.
3 2
B..
RB.
RB.
4 3
R...
BR..
BR..
BR..
4 4
....
BR..
BR..
BR..
*/
