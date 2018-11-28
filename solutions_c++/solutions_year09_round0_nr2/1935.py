#include <iostream>

using namespace std;

const int MAXN = 110;
const int MAX = 100000000;
const int d[4][2]={{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
const int opp[4] = {3, 2, 1, 0};

int a[MAXN][MAXN], mark[MAXN][MAXN], dr[MAXN][MAXN], label[100];
int m, n, p;

void init()
{
 int i, j;
     scanf("%d%d", &n, &m);
     for (i=1; i<=n; i++)
         for (j=1; j<=m; j++)
             scanf("%d", &a[i][j]);
}

void search(int x, int y, int p)
{
     mark[x][y] = p;
     int u, x0, y0;
     for (u=0; u<4; u++){
         x0=x+d[u][0];
         y0=y+d[u][1];
         if (x0>0 && x0<=n && y0>0 && y0<=m && mark[x0][y0]==0 && opp[dr[x0][y0]]==u)
            search(x0, y0, p);
     }     
}
     
void work()
{
     int i, j, x, y, w, k;
     
     memset(mark, 0, sizeof(mark));
     memset(dr, 0xFF, sizeof(dr));
     p = 0;
     for (i=1; i<=n; i++)
         for (j=1; j<=m; j++)
         {
             w = MAX;
             for (k=0; k<4; k++){
                 x = i+d[k][0];
                 y = j+d[k][1];
                 if (x>0 && x<=n && y>0 && y<=m && a[x][y]<a[i][j] && a[x][y]<w){
                         w = a[x][y];
                         dr[i][j] = k;
                 }
             }
         }
     for (i=1; i<=n; i++)
         for (j=1; j<=m; j++)
             if (dr[i][j] == -1)
             { 
               p++;
               search(i, j, p);
             }
     memset(label, 0, sizeof(label));
     k = 0;
     for (i=1; i<=n; i++){
         for (j=1; j<=m; j++)
         {   if (label[mark[i][j]]==0){
                k++;
                label[mark[i][j]] = k;
             }
             printf("%c ", 'a'-1+label[mark[i][j]]);
         }                            
         printf("\n");
     }
}
          
int main()
{
    int i, t;
    
    scanf("%d", &t);
    i = 0;
    while (t--){
          i++;
          printf("Case #%d:\n", i);
          init();
          work();
    }
          
    
    return 0;
}
