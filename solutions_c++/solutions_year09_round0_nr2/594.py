#include <iostream>
using namespace std;
int a[128][128];

int dx[] = {-1, 0, 0, +1};
int dy[] = { 0, -1, +1,  0};
int n, m;
char b[128][128];
char c;
char dfs (int x, int y)
{
    //cout << x <<" "<< y << endl;
    if (b[x][y]!=0) return b[x][y];
    
    int i, dir = -1; int temp = 0;
    for (i = 0; i< 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx< 1 || nx > n || ny < 1 || ny > m) continue;
        
        if (a[nx][ny] >= a[x][y]) continue;
        if (dir == -1 || a[nx][ny] < temp)
        {
            temp = a[nx][ny];
            dir = i;        
        }
    }
    
    if (dir == -1)return b[x][y] = c++;
    
return b[x][y] = dfs(x + dx[dir], y + dy[dir]);
}

void solve (int pos)
{
    c = 'a';
    memset (a, 0 , sizeof (a));
    memset (b, 0 , sizeof (b));
      int i, j; 
      scanf ("%d%d", &n, &m);
    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++)
            scanf("%d", &a[i][j]);
            
  
    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++)
          dfs (i, j);
        
        printf ("Case #%d:\n", pos);
    for (i = 1; i <= n; i++)
        {printf ("%c", b[i][1]);
            for (j = 2; j <= m; j++)
                printf (" %c", b[i][j]);
        printf ("\n");
        }     
    
}
int main ()
{
    int o;
    scanf ("%d", &o);
    int i;
    for (i= 1; i<=o; i++) solve (i);
    
    return 0;
}
