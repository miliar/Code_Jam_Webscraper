#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;



int main()
{
	//freopen("test.in", "rt", stdin);
	freopen("A-small-1.in", "rt", stdin);
	freopen("A-small-1.out", "wt", stdout);
	//cout << setiosflags(ios::fixed) << setprecision(10);

	int qq;
	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d:\n", ii+1);
		int row,col;
		cin >>row>>col;
		char plot[52][52];
		bool ok  = true;
		forn(r, row) {
			forn(c, col) {
				cin >> plot[r][c];
			}
		}

		forn(r, row) {
			forn(c, col) {
				if (plot[r][c] == '#') {
					if (c+1<col && r+1 <row 
							&& plot[r][c+1] == '#' 
							&& plot[r+1][c] == '#' 
							&& plot[r+1][c+1] == '#' ) {

						plot[r][c] = '/'; 
						plot[r][c+1] = '\\';
						plot[r+1][c] = '\\'; 
						plot[r+1][c+1] = '/';

					} else {
						ok = false;
						goto end;
					}
				}
			}
		}

end:
		if (ok) {
			forn(r, row) {
				forn(c, col) {
					cout << plot[r][c];
				}
				cout <<endl;
			}
		}
		else {
		   cout << "Impossible\n";
		}

	}

	return 0;
}
