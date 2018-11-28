#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 100

const int fx[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int CASE;
int n, m;
int f[MAXN + 1][MAXN + 1];
int g[MAXN + 1][MAXN + 1];
bool flag[MAXN + 1][MAXN + 1];
int count = 0;

void ini(void)
{
     memset(g, -1, sizeof(g));
     memset(flag, 0, sizeof(flag));
     
     scanf("%d %d\n", &n, &m);
          
     int i, j, k;
     for(i=1; i<=n; i++)
              for(j=1; j<=m; j++)
                      scanf("%d", &f[i][j]);
     
     return;
}

int dfs(int i, int j)
{
     int mini, minj, mins, k;
     int nx, ny;
     

     if (g[i][j] != -1)
        return g[i][j];

     flag[i][j] = true;                   
     mins = 214748364;    
     for(k=0; k<4; k++)
     {
          nx = i + fx[k][0]; ny = j + fx[k][1];
          if (nx < 1 || nx > n || ny < 1 || ny > m || flag[nx][ny])
             continue;
          if (f[nx][ny] < mins && f[nx][ny] < f[i][j])
          {
                  mins = f[nx][ny];
                  mini = nx; minj = ny;
          }   
     }   
     if (mins == 214748364)
     {
         g[i][j] = count;
         count++;
     }
     else
         g[i][j] = dfs(mini, minj);
         
     flag[i][j] = false;
     return g[i][j];
}


void work(void)
{
     int i, j, k, l, nx, ny;
     int mink, mins;
     for(i=1; i<=n; i++)
              for(j=1; j<=m; j++)
              {
                       if (g[i][j] != -1)
                          continue;
                       g[i][j] = dfs(i, j);
              }
              
     return;
} 

void out(void)
{
     int i, j;

     for(i=1; i<=n; i++)
     {
              for(j=1; j<=m; j++)
                       printf("%c ", g[i][j] + 'a');
              printf("\n");
     }
     return;
}

int main(void)
{
    freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    
    int i, p;
    scanf("%d", &p);
    for(i=1; i<=p; i++)
    {
             printf("Case #%d:\n", i);
             count = 0;
             ini();
             work(); 
             out();
    }
    
    return 0;
}
