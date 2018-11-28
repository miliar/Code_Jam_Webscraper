#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
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
#define It(x) x::iterator
#define CIt(x) x::const_iterator
#define For(i, st, en) for(__typeof(en) i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(__typeof(n) i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

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

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

string st;
char ch[512];
string wlc="welcome to code jam";
int n;
int l,ll;
i64 ans=0;

void rek(int x, int y)
{
	if (y==ll)
	{
		ans++;
		return;
	}

	for (int i=x;i<l;i++)
	{
		if (st[i]==wlc[y])
		{
			rek(i+1, y+1);
		}
	}
}

//welcome to code jam

void viv(i64 x)
{
	string stt=tostr(x);

	while (stt.sz < 4)
	{
		stt='0'+stt;
	}

	printf("%s\n", stt.c_str());
}

int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &n);
	gets(ch);

	ll=wlc.sz;

	for (int i=0;i<n;i++)
	{
		gets(ch);
		st=ch;
		l=st.sz;

		ans=0;

		rek(0,0);

		printf("Case #%d: ", i+1);
		viv(ans);
//		printf("\n");
	}

	return 0;
}
