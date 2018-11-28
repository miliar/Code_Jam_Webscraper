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

using namespace std;
long long n;
int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);  
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T++) {
        scanf("%d", &n);
        int ind = 0, prime[MAXN] = {0};
        for(int i = 2; i <= n; i++) {
            if(!prime[i]) {
                for(int j = i * i; j < 1001; j += i) {
                    prime[j] = 1;
                }
                prime[ind++]=i;
            }
        }
        
        int minv = ind, maxv = 1;
        int bj[MAXN * 10] = {0};
        for(int i = 2; i <= n; i++) {
            bool flag = 0;
            int t = i;
            for(int j = 0; j < ind; j++) {
                int z=0;
                while(t % prime[j] == 0) {
                    z++;
                    t /= prime[j];
                }
                if(bj[j] < z) {
                    bj[j] = z;
                    flag = 1;
                }
            }
            maxv += flag;
        }
        if (n == 1) {
            minv=1;
        }
        printf("Case #%d: %d\n", T,maxv - minv);
    }
}