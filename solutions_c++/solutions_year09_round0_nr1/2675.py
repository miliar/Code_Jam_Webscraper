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

string dic[7000];
char ch[1024];
bool m[100][100];
int l,d,n;


int main()
{
	freopen("q.in", "rt", stdin);
	freopen("q.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);
	
	scanf("%d %d %d\n",&l,&d,&n);
	for (int i=0; i<d; i++)
	{
		gets(ch);
		dic[i]=ch;
	}
	
	for (int q=0; q<n; q++)
	{
		gets(ch);
		clr(m);
		int j=0;
		for (int i=0; i<int(strlen(ch)); i++)
		{
			if (ch[i]=='(') 
			{
			    i++;
				while (ch[i]!=')')
				{
					m[j][ch[i]-'a']=1;
					i++;
				}
				j++;
				continue;
			}
			m[j][ch[i]-'a']=1;
			j++;
		}

		int ans=0;
		bool can=true;

		for (int q1=0; q1<d; q1++)
		{
			can=true;
			for (int j=0; j<l; j++)
			if (!m[j][dic[q1][j]-'a'])
			{
				can=false;
				break;		
			}
			if (can) ans++;
		}
		printf("Case #%d: %d\n",q+1,ans);
	}




	return 0;
}
