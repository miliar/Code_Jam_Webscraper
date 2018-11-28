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
int ntest, test;
int n, m, a;
int kq[55][55][2555][5];

void read_in() {
     cin >> n >> m >> a;
}

void pre() {
     memset(kq, 0, sizeof(kq));
     int x1 = 0, y1 = 0;
     FOR(x2, 0, 50) FOR(x3, 0, 50) FOR(y2, 0, 50) FOR(y3, 0, 50) {
       int dt = (x1-x2)*(y1+y2) + (x2-x3)*(y2+y3) + (x3-x1)*(y3+y1);       
       dt = myabs(dt);       
       int xx = tmax(x2, x3);
       int yy = tmax(y2, y3);
       kq[xx][yy][dt][0] = 1;
       kq[xx][yy][dt][1] = x2;
       kq[xx][yy][dt][2] = y2;
       kq[xx][yy][dt][3] = x3;
       kq[xx][yy][dt][4] = y3;        
     }
}

void process() {
     FOR(n0, 0, n) FOR(m0, 0, m)
       if (kq[n0][m0][a][0]>0) {
         //cout << n0 << " "<<m0<<endl;
         cout << "0 0 "<<kq[n0][m0][a][1]<< " "<<kq[n0][m0][a][2]<<" "<<kq[n0][m0][a][3]<<" "<<kq[n0][m0][a][4];
         return;
       }
     cout << "IMPOSSIBLE";
}

int main() {
    pre(); cout<<"xong\n";
    freopen("B-small-attempt1.in", "rt", stdin);
    freopen("b.out", "wt", stdout);
    
    
    
    scanf("%d", &ntest);
    FR(test, ntest) {
        read_in();
        cout << "Case #" << test+1<<": ";
        process();
        cout << endl;
    }
    
    return 0;
}
