#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#define fo(a,b,c) for(a = (b); a < (c); a++)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define fn fr
#define forit(i,a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define fill(a,b) memset(a, b, sizeof(a))

using namespace std;

int ni() { int x; scanf( "%d", &x ); return x; }
double nf() { double x; scanf( "%lf", &x ); return x; }
char sbuf[10000]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long x; scanf( "%lld", &x ); return x; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( ", " ); first = false; cout << * i; } printf( "" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
template <class T> T abs(T x) { return x < 0 ? -x : x; }
template <class T> T sqr(T x) { return x*x; }
template <class T> inline string toStr(const T& a) { ostringstream os(""); os << a; return os.str(); }

const long double PI = acos(-1.0);

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef set<int> si;

// #define dbg(x) cout << (#x) << "= " << (x) << endl;

int main()
{
	int i, j, k, t, tt;
        int s, p, n, x, y;
        int a[100] = {0};

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	tt = ni();

	for( t = 1; t <= tt; t++ )
	{
            n = ni();
            s = ni();
            p = ni();
            y = 0;

            int c = 3*p - 2;

            fi(n)
            {
                x = a[i] = ni();
                if(x>=c) y++;
                else if(s>0) 
                {
                    int q = (x-p)/2;
                    if(p-q<=2 && x>=p) { y++; s--; }
                    //if ((x-p)/2>=p-2 && s>0 && x>=p) { y++; s--; }
                }
            }
                

            printf( "Case #%d: %d\n", t, y );
	}

	return 0;
}
