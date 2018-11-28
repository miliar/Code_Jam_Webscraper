#include <fstream>

using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

int test_case, n,m, a[128][128];

char v[128][128], flag;

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

void fill(int x,int y)
{
     if (v[x][y] != 0)
          return;

     int Min = 123456, mx=0,my=0;
     
     for (int i=0;i<4;++i)
          if (x+dx[i] > 0 && x+dx[i] <= n)     
          if (y+dy[i] > 0 && y+dy[i] <= m)     
          if (Min > a[x+dx[i]][y+dy[i]])
          {
               Min = a[x+dx[i]][y+dy[i]];
               mx = x + dx[i];
               my = y + dy[i];
          }
     if (Min < a[x][y])
     {
          fill(mx,my);
          v[x][y] = v[mx][my];
     }
          else
     {
          v[x][y] = flag;
          flag++;
     }
}

void solve()
{
     ++test_case;
     
     fin >> n >> m;
     
     for (int i=1;i<=n;++i)
     for (int j=1;j<=m;++j)
          fin >> a[i][j];
          
     for (int i=1;i<=n;++i)
     for (int j=1;j<=m;++j)
          v[i][j] = 0;
          
     flag = 'a';     
     
     for (int i=1;i<=n;++i)
     for (int j=1;j<=m;++j)
          fill(i,j);
          
     fout << "Case #" << test_case << ":\n";
     
     for (int i=1;i<=n;++i)
     {
          for (int j=1;j<m;++j)
               fout << v[i][j] << " ";
          fout << v[i][m] << "\n";
     }
          
}

int main()
{
     int t;
     
     fin >> t;
     
     while (t--)
          solve();
     
     return 0;     
}
