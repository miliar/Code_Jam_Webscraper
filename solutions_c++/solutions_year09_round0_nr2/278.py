#include<fstream>
using namespace std;

const int maxn = 100+3;
const int c[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int cases, n, m, now;
int a[maxn][maxn], b[maxn][maxn];

int dfs(int x, int y)
{
    if (b[x][y] > 0) return b[x][y];
    
    int z = a[x][y], j = -1;             
    for (int i = 0; i <= 3; ++i)
      if (a[x+c[i][0]][y+c[i][1]] < z){
        z = a[x+c[i][0]][y+c[i][1]]; j = i;                            
      }
    if (j == -1) {
      ++now; b[x][y] = now;            
    }
    else b[x][y] = dfs(x+c[j][0],y+c[j][1]);
    return b[x][y];
}

int main()
{
    ifstream input("2.in");
    ofstream output("2.out");
    input >> cases;
    for (int k = 1; k <= cases; ++k){
      output << "Case #" << k << ": " << endl;
      input >> n >> m; now = 0;
      for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) input >> a[i][j];
        
      memset(b, 0, sizeof(b));
      for (int i = 0; i <= n+1; ++i) a[i][0] = 10000000;
      for (int j = 0; j <= m+1; ++j) a[0][j] = 10000000;
      for (int i = 0; i <= n+1; ++i) a[i][m+1] = 10000000;
      for (int j = 0; j <= m+1; ++j) a[n+1][j] = 10000000;
      
      for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
          if (b[i][j] == 0) b[i][j] = dfs(i,j); 
      
      for (int i = 1; i <= n; ++i){
        for (int j = 1; j <= m; ++j) output << char(b[i][j]+int('a')-1) << " ";
        output << endl;    
      }
    }
    return 0;
}
