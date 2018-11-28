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
const ld EPS = 1e-11;
const int dx[] = {-1,0,1,0,-1,-1,1,1};
const int dy[] = {0,1,0,-1,-1,1,-1,1};

struct data {
    int b, e;
    double w, len;
    bool operator <(const data& d) const {
        return w < d.w;
    }
}a[1001];

int main() {
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);  
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas, X, S, R, N;
    double t;
    scanf("%d", &cas);
    for (int TT = 1; TT <= cas; TT++) {
        scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
        int left = X;
        for (int i = 1; i <= N; i++) {
            scanf("%d%d%lf", &a[i].b, &a[i].e, &a[i].w);
            a[i].len = a[i].e - a[i].b;
            left -= (a[i].e - a[i].b);
        }
        a[0].len = left;
        a[0].w = 0;
        N++;
        sort(a, a + N);
        /*for (int i = 0; i < N; i++) {
            for (int j = a[i].b; j <= a[i].e; j++) {
                id[j] = i;
            }
        }*/
        double T = 0;
        for (int i = 0; i < N; i++) {
            T += a[i].len / (S + a[i].w);
        }
        //cout << T << endl;
        for (int i = 0; i < N; i++) {
            if (t <= 0) break;
            if (t * (R + a[i].w) >= a[i].len) {
                //T -= a[i].len / (S + a[i].w);
                //T += a[i].len / (R + a[i].w);
                T -= a[i].len / (S + a[i].w);
                T += a[i].len / (R + a[i].w);// + (a[i].len - t * (R + a[i].w)) / (S + a[i].w);
                t -= a[i].len / (R + a[i].w);
            } else {
                T -= a[i].len / (S + a[i].w);
                T += t + (a[i].len - t * (R + a[i].w)) / (S + a[i].w);
                t = 0;
               //T -= t;
                //T += t * (S + a[i].w) / (R + a[i].w);
                break;
            }
            //cout << T  << endl;
        }
        printf("Case #%d: %.9lf\n", TT , T);
    }
}