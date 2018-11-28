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
typedef vector<string> VS;


int ntest, test;
int a[5555];
int cnt;
int k, x, n;

int main() {
    freopen("c1.in", "rt", stdin);
    freopen("c1.out", "wt", stdout);
    
    scanf("%d", &ntest);
    FR(test, ntest) {
        scanf("%d", &k);
        memset(a, 0, sizeof(a));
        a[1] = 1;
        cnt = 0;
        int cur = 1;
        FOR(i, 2, k) {
          while (true) {
           cur++; if (cur>k) cur-=k;
           if (a[cur]==0) cnt++;
           if (cnt==i) {
             a[cur] = i;
             cnt = 0;
             break;
           }
          }
        }
        
        
        //FOR(i,1,k) cout << a[i] << endl;
        scanf("%d", &n);
        
        
        cout << "Case #" << test+1<<":";
        FR(i, n) {
          scanf("%d", &x);
          cout << " " << a[x];
        }
        cout<<endl;
    }
    
    return 0;
}
