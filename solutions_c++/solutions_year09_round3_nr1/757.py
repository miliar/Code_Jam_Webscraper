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

int dec(char x)
{
	if (x>='0' && x<='9')	return x-'0'; else return x-'a'+10;
}


int main()
{
  freopen("A-large.in", "rt", stdin);
  freopen("a.out", "wt", stdout);
  cout << setiosflags(ios::fixed) << setprecision(10);
  int TT;
  int n;
  string s;
  int a[1000],m[1000];
  cin >> TT;
  int used[100];

  int mm=0;

  forn (T,TT)
  {
  	
  	cin >> s;

  	clr(used);
  	
  	n=int(s.sz);
  	
  	forn(i,n) 
	{
	  	a[i]=dec(s[i]);
	  	used[a[i]]=1;
	  	if (dec(s[i])>mm) mm=dec(s[i]);
	}

	int b=0;
	forn (i,50)
		b+=used[i];
	if (b<2) b=2;

	memset(m,0xff,sizeof(m));
	m[dec(s[0])]=1;
	int next=0;

	for (int i=1; i<n; i++)
	if (m[dec(s[i])]<0)
	{
		if (next==1) next++;
		m[dec(s[i])]=next;
		next++;
	}

	i64 ans=0;

	forn(i,n)
	{
		ans*=b;
		ans+=m[dec(s[i])];
	}

	cout << "Case #" << T+1 << ": " << ans << endl;

  }
  

  return 0;
}
