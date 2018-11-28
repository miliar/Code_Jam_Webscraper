#include <iostream>
#include <fstream>
using namespace std;

#define LL long long
#define MAXP 110
#define MAXN 10010
#define UND 0
LL i,j,n,m,T;
LL in[MAXP];
LL dp[MAXN][MAXN], low, high;

ifstream fin("in.txt");
ofstream fout("out.txt");

LL f(LL x, LL y) {
   LL low, high;
   //cout << "Enter-> x: " << x << "  y: " << y << endl;
   
   if (dp[x][y] != UND) return dp[x][y];
   
   // find bounds
   for (low=0; low < m && in[low] < x; low++);
   for (high=m-1; high >= 0 && in[high] > y; high--);
   
   //cout << "bounds: " << low << " " << high << endl;
   
   if (low > high || low == m || high < 0) {
      dp[x][y] = 0;
      return 0;
      }
   LL ret = UND;
   LL now;
   for (LL i=low;i<=high;i++) {
       now = y - x + f(x,in[i]-1) + f(in[i]+1,y);
       if (ret == UND || ret > now) ret = now;
       }
   
   //cout << "x: " << x << "  y: " << y << "    = " << ret << endl;
   dp[x][y] = ret;
   return ret;
   }
   
LL solve() {
   //LL dp[MAXN][MAXN];
   return f(1,n);
   }
   
int main() {
    fin >> T;
    for (LL t=1;t<=T;t++) {
        fin >> n >> m;
        for (i=0;i<m;i++) fin >> in[i];
        
        cout << "Case #" << t << ": " << endl;
        
        for (int a=0;a<=n;a++) fill(dp[a], dp[a] + n + 1, UND);
   
        fout << "Case #" << t << ": " << solve() << endl;
        /*
        cout << "Deb[]:" << endl;
        for (i=1;i<=n;i++) {
            for (j=1;j<=n;j++) cout << dp[i][j] << " ";
            cout << endl;
            }
        system("pause");
        */
        }
    cout << "All done!" << endl;
    system("pause");
}
    
