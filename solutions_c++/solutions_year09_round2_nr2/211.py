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
#define fst first
#define snd second
#define It(x) __typeof((x).begin())
#define For(i, st, en) for(__typeof(en) i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(__typeof(n) i=0; i<(n); i++)
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

char s[128];

int main()
{
	freopen("b-l.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int tc;
	scanf("%d\n", &tc);
	forn(tn, tc)
	{
		printf("Case #%d: ", tn + 1);

		scanf("%s", s);
		int d[10] = {};
		int len = strlen(s);

		bool found = false;
		ford(i, len)
		{
            ++d[s[i] - '0'];

			int k = -1;
			For(j, s[i] - '0' + 1, 9)
			{
				if (d[j] > 0)
				{
					k = j;
					break;
				}
			}
			if (k != -1)
			{
				s[i] = 0;
				printf("%s%d", s, k);
                --d[k];

                forn(j, 10)
                {
                	forn(l, d[j])
                	{
                		printf("%d", j);
                	}
                }
				
				found = true;
				break;
			}
		}

		if (!found)
		{
			For(i, 1, 9)
			{
				if (d[i] > 0)
				{
					printf("%d", i);
                    --d[i];
                    break;
				}
			}
			forn(i, d[0] + 1)
			{
				putchar('0');
			}
            For(j, 1, 9)
            {
            	forn(l, d[j])
            	{
            		printf("%d", j);
            	}
            }
		}
		puts("");
	}

	return 0;
}
