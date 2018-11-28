#include "iostream"
#include "algorithm"
#include "fstream"
#include "sstream"

#define tmax(a, b) (((a)>(b))?(a):(b))
#define tmin(a, b) (((a)<(b))?(a):(b))
#define FR(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=a; i<=b; i++)

using namespace std;

int ntest;
int ns, nq;
string s[111], q[1111];
int f[1111][111], maxf, res;

int main() {
    //freopen("1l.in",  "rt", stdin);
    //freopen("1l.out", "wt", stdout);
    
    cin >> ntest;
    FOR(test, 1, ntest) {
      cin >> ns; getline(cin, s[0]);
      FOR(i, 1, ns) getline(cin, s[i]);
      cin >> nq; getline(cin, q[0]);
      FOR(i, 1, nq) getline(cin, q[i]);
      
      if (nq == 0) res = 0;
      else {
          memset(f, 0x3f, sizeof(f));
          maxf = f[0][0];
          
          FOR(i, 1, ns)
            if (q[1] != s[i]) f[1][i] = 0;
    
          FOR(i, 1, nq-1) {
            FOR(j, 1, ns) if (f[i][j]<maxf) {
              if (q[i+1] != s[j]) 
                f[i+1][j] <?= f[i][j];
              
              FOR(k, 1, ns)
                if (q[i+1] != s[k])
                  f[i+1][k] <?= f[i][j]+1;
            }      
          }
        
        res = maxf;
        FOR(i,1,ns) res <?= f[nq][i];
      }
      printf("Case #%d: %d\n", test, res);
    }       

    return 0;
}
