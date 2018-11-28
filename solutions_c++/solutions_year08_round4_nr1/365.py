#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define FOR(i,a,b) for (int i=a; i<=b; i++)
#define FI first
#define SE second
#define tmax(x, y) (((x)>(y))? (x):(y))
#define tmin(x, y) (((x)<(y))? (x):(y))
#define myabs(x) (((x)>0)? (x):(-(x)))
#define INF 1000000000

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

typedef pair<int, int> II;
typedef vector<int> VI;
typedef long long LL;

int res;
int n, value;
int g[11111], c[11111], f[11111][2];

int ntest, test;

void read_in() {
     cin >> n >> value;
     int j = (n-1)/2;
     FOR(i,1,(n-1)/2) cin >> g[i] >> c[i];
     FOR(i,j+1, n) cin >> g[i];
}

bool isLeaf(int i) {
     return (i > (n-1)/2);
}

void dyna(int i, int v) {
     if (f[i][v] != -1) return;
     
     
     f[i][v] = INF;
     if (isLeaf(i)) {
       if (g[i] == v) f[i][v] = 0;
       //else f[i][v] = 1;
     }
     else {
       // i*2 i*2+1
       if (v==1) { // value = 1
         if (g[i]==0) { // or
           f[i][v] <?= f[i*2][0] + f[i*2+1][1];
           f[i][v] <?= f[i*2][1] + f[i*2+1][1];
           f[i][v] <?= f[i*2][1] + f[i*2+1][0];
         }
         else { // and
           if (c[i]==1) {
             f[i][v] <?= f[i*2][0] + f[i*2+1][1] + 1;
             f[i][v] <?= f[i*2][1] + f[i*2+1][1] + 1;
             f[i][v] <?= f[i*2][1] + f[i*2+1][0] + 1;
           }
           
           f[i][v] <?= f[i*2][1] + f[i*2+1][1];
         }
       }
       else { // value = 0
         
         if (g[i]==1) { // and         
           f[i][v] <?= f[i*2][0] + f[i*2+1][1];
           f[i][v] <?= f[i*2][0] + f[i*2+1][0];
           f[i][v] <?= f[i*2][1] + f[i*2+1][0];
         }
         else { // or
         
           if (c[i]==1) {
             f[i][v] <?= f[i*2][0] + f[i*2+1][1] + 1;
             f[i][v] <?= f[i*2][0] + f[i*2+1][0] + 1;
             f[i][v] <?= f[i*2][1] + f[i*2+1][0] + 1;
           }
           
           f[i][v] <?= f[i*2][0] + f[i*2+1][0];
         }
       }
     }
     
     
     
}

void process() {
     memset(f, 0xff, sizeof(f));
     for (int i=n; i>=1; i--) {
         dyna(i, 0);
         dyna(i, 1);
         //cout << i << " " << f[i][0] << " " << f[i][1] << endl;
     }
     
     //cout << f[2][1] << endl;
     res = f[1][value];
}

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    
    scanf("%d", &ntest);
    FR(test, ntest) {        
        read_in();
        process();
        cout << "Case #" << test+1<<": ";
        if (res == INF) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
    
    return 0;
}
