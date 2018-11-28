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
template <class _T> inline _T sgn(const _T& x) { return x > 0 ? 1 : (x < 0 ? -1 : 0); }
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

char reactTo[128][128];
bool opposed[128][128];
char ans[1024];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int testsCount;
	scanf("%d", &testsCount);
	forn(testNumber, testsCount)
	{
		clr(reactTo);
		clr(opposed);
		clr(ans);
		
		int n;
		scanf("%d", &n);
		forn(i, n)
		{
			char s[4];
			scanf("%s", s);
			reactTo[s[0]][s[1]] = reactTo[s[1]][s[0]] = s[2];
		}
		
		scanf("%d", &n);
		forn(i, n)
		{
			char s[3];
			scanf("%s", s);
			opposed[s[0]][s[1]] = opposed[s[1]][s[0]] = true;
		}
		
		scanf("%d", &n);
		char s[128];
		scanf("%s", s);
		
		char* res = ans;
		for (const char* p = s; *p; ++p)
		{
			*res++ = *p;
			while (res - ans >= 2)
			{
				int c1 = *(res - 1);
				int c2 = *(res - 2);
				
				if (!reactTo[c1][c2]) break;
				
				*(res - 2) = reactTo[c1][c2];
				--res;
			}
			*res = '\0';
			for (const char* q = ans; *(q + 1); ++q)
			{
				if (opposed[*q][*(res - 1)])
				{
					res = ans;
					break;
				}
			}
		}
		*res = '\0';
		
		string t;
		for (const char* p = ans; *p; ++p)
		{
			t += *p;
			t += ", ";
		}
		if (t.sz > 0)
		{
			t.erase(t.sz - 2);
		}
		
		printf("Case #%d: ", testNumber + 1);
		printf("[%s]\n", t.c_str());
	}

	return 0;
}
