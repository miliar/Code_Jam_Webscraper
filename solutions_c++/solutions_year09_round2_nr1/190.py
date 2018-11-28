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

struct TNode
{
	ld p;
	string f;
	TNode* pLeft;
	TNode* pRight;

	TNode()
	{
		pLeft = pRight = NULL;
	}

	~TNode()
	{
		if (pLeft) delete pLeft;
		if (pRight) delete pRight;
	}
};

string s;
int cur;
char buf[128];

ld readNum()
{
	ld res;
	res = 0;
	while (isdigit(s[cur]))
	{
		res = res * 10 + (s[cur++] - '0');
	}
	if (s[cur] == '.')
	{
		++cur;
		ld d = 1;
		while (isdigit(s[cur]))
		{
			d /= 10;
			res += d * (s[cur++] - '0');
		}
	}
	return res;
}

TNode* parse()
{
	TNode* res = new TNode();

	assert(s[cur] == '(');
    ++cur;

	res->p = readNum();
	if (isalpha(s[cur]))
	{
		while (isalpha(s[cur]))
		{
			res->f += s[cur++];
		}
		res->pLeft = parse();
		res->pRight = parse();
	}
	assert(s[cur] == ')');
    ++cur;
	return res;
}

int main()
{
	freopen("a-l.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int tc;
	scanf("%d", &tc);
	forn(tn, tc)
	{
		int l;
		scanf("%d\n", &l);

		s.erase();
		forn(i, l)
		{
			gets(buf);
			for (char* p = buf; *p; ++p)
			{
				if (!isspace(*p))
				{
					s += *p;
				}
			}
		}
		cur = 0;
		TNode* pRoot = parse();

		printf("Case #%d:\n", tn + 1);

		int n;
		scanf("%d\n", &n);
		forn(i, n)
		{
			int k;
			scanf("%*s %d", &k);

			VS v;
			forn(j, k)
			{
				scanf("%s", buf);
				v.pb(buf);
			}

			TNode* pCur = pRoot;
			double p = 1;
			while (true)
			{
				p *= pCur->p;
				if (pCur->pLeft == NULL) break;

				if (find(all(v), pCur->f) != v.end())
				{
					pCur = pCur->pLeft;
				}
				else
				{
					pCur = pCur->pRight;
				}
			}
			printf("%.7f\n", p);
		}
		delete pRoot;
	}

	return 0;
}
