#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define VI vector<int>
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 110;
const int mod = 10007;

int h,w,r,x[maxn],y[maxn];
int a[maxn][maxn],vis[maxn][maxn];

void tryit(int a1, int b1, int a2, int b2)
{
   if (a2 <= h && b2 <= w && !vis[a2][b2]) {
      a[a2][b2] = (a[a2][b2] + a[a1][b1]) % mod;
   }
}

int main()
{
   freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> h >> w >> r;
      memset(vis,0,sizeof(vis));
      for (i = 1; i <= r; i++) {cin >> x[i] >> y[i]; vis[x[i]][y[i]] = 1;}
      memset(a,0,sizeof(a));
      a[1][1] = 1;
      for (i = 1; i <= h; i++)
         for (j = 1; j <= w; j++) if (!vis[i][j]) {
            tryit(i,j,i+1,j+2); tryit(i,j,i+2,j+1);
         }
      cout << "Case #" << sc << ": ";
      cout << a[h][w];
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}