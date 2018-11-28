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

LL n, a, b, c, d, m;
LL x[100001], y[100001];
int cc[3][3];
int ntest, test;

int main() {
    freopen("al.in", "rt", stdin);
    freopen("al.out", "wt", stdout);
    
    scanf("%d", &ntest);
    FR(test, ntest) {
        scanf("%d%d%d%d%d%d%d%d", &n, &a, &b, &c, &d, &x[0], &y[0], &m);
        memset(cc, 0, sizeof(cc));               
        cc[x[0]%3][y[0]%3]++;
        FOR(i, 1, n-1) {
          x[i] = (a * x[i-1] + b) % m;
          y[i] = (c * y[i-1] + d) % m;      
          cc[x[i] % 3][y[i] % 3]++;          
          //cout << x[i] << " "<< y[i] << endl;
        }       
        
        
        LL cnt = 0;
        /*
        FR(i, n) FOR(j, i+1, n-1) FOR(k, j+1, n-1)
          if ((x[i] + x[j] + x[k]) % 3==0 && (y[i] + y[j] + y[k]) % 3==0) {
            //cout << i << " " << j << " " << k << endl;
            cnt++;
          }
        */
        
        LL t1, t2, t3;
        FR(x1, 3) FR(y1, 3) {      
          if (cc[x1][y1] <= 0) continue;
          t1 = cc[x1][y1];
          cc[x1][y1]--;
          
          FR(x2, 3) FR(y2, 3) {      
              if (cc[x2][y2] <= 0) continue;
              t2 = cc[x2][y2];
              cc[x2][y2]--;
              
              FR(x3, 3) FR(y3, 3) {      
                  if (cc[x3][y3] <= 0) continue;
                  t3 = cc[x3][y3];
                  cc[x3][y3]--;
                  
                  if (((x1 + x2 + x3) % 3) == 0 && ((y1 + y2 + y3) % 3) == 0)
                    cnt += t1*t2*t3;
                  
                  
                  cc[x3][y3]++;
                }
              
              cc[x2][y2]++;
            }
          
          cc[x1][y1]++;
        }
        
        //printf("Case #%d: %lld\n", test+1, cnt);
        //if (cnt % 6 != 0) cout << "dadsa" << endl;
        cout << "Case #" << test+1<<": "<<cnt/6<<endl;
    }
    
    return 0;
}
