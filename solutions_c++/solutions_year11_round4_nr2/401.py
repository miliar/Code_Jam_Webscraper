#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

using namespace std;

#define clr(x) memset((x),0,sizeof(x))
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define Ford(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define ford(i,n) for(int i=(n)-1;i>=0;i--)
#define fori(it,x) for (__typeof((x).begin()) it = (x).begin();it != (x).end();it++)

template <class T> inline T sqr(const T& x) { return x * x; }
template <class T> inline string tostr(const T& a) { ostringstream os(""); os << a; return os.str(); }
template <class T> inline istream& operator << (istream& is, const T& a) { is.putback(a); return is; }

// Types
typedef long double ld;
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

// Constants
const ld PI = acos(-1.0);//3.1415926535897932384626433832795;
const ld EPS = 1e-8;
const int dx[] = {-1,0,1,0,-1,-1,1,1};
const int dy[] = {0,1,0,-1,-1,1,-1,1};
const int MAXN = 1234;
int mat[MAXN][MAXN];
int n, d, m;

inline int sgn(double x) {
    return x < -EPS ? -1 : x > EPS;
}

int check(int i,int j,int d) {
    double x = 0, y = 0;
    for(int ii = 0; ii < d; ii++) {
        for(int jj = 0; jj < d; jj++) {
            if ((ii == 0 && jj == 0) || 
                (ii == 0 && jj == d - 1) ||
                (ii == d - 1 && jj == d - 1) ||
                (ii == d - 1 && jj == 0) ) {
                    continue;
            }
            x += mat[ii + i][jj + j] * (ii - (d - 1) / 2.0);
            y += mat[ii + i][jj + j] * (jj - (d - 1) / 2.0);
        }
    }
    return sgn(x) == 0 && sgn(y) == 0;
}
int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);  
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T++) {
        scanf("%d%d%d", &n, &m, &d);
        for(int i = 0;i < n; i++) {
            for(int j = 0; j < m; j++) {
                char z;
                cin >> z;
                mat[i][j] = z - '0';
            }
        }
        int ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j=0;j<m;j++) {
                for(int d = 3; i + d - 1 < n && j + d <= m; d++) {
                    if (check(i, j, d) && d > ans) {
                        ans = d;
                    }
                }
            }
        }
        printf("Case #%d: ", T);
        if (ans != -1) {
            printf("%d\n", ans);
        } else {
            puts("IMPOSSIBLE");
        }
    }
}