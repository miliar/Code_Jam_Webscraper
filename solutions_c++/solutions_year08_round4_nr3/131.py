/*
 * Util defines and templates written by me before the GCJ2008 contest started
 * Andre Susano Pinto <andresusanopinto@gmail.com>
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cfloat>
#include <queue>
#include <climits>
#include <cassert>
#include <string.h>
#define join(a,b) a##b
#define EP (1e-9)

typedef unsigned int uint32;
typedef unsigned long long uint64;

using namespace std;

template<typename T> typename T::iterator IterBegin(T &t) { return t.begin(); }
template<typename T> typename T::iterator IterEnd  (T &t) { return t.end(); }
template<typename T,int S> T* IterBegin(T (&t)[S]) { return t+0; }
template<typename T,int S> T* IterEnd  (T (&t)[S]) { return t+S; }

template<typename T> typename T::const_iterator IterBegin(const T &t) { return t.begin(); }
template<typename T> typename T::const_iterator IterEnd  (const T &t) { return t.end(); }
template<typename T,int S> const T* IterBegin(const T (&t)[S]) { return t+0; }
template<typename T,int S> const T* IterEnd  (const T (&t)[S]) { return t+S; }

template<typename T> int size(const T &t) { return t.size(); }
template<typename T, int S> int size(const T (&t) [S]) { return S; }

#define FOREACH(col, iter, end) for(__typeof( IterBegin(col) ) iter = IterBegin(col), end=IterEnd(col); iter != end; iter++)
#define foreach(col, iter) FOREACH(col, iter, join(iter, __end))
#define all(col)    IterBegin(col), IterEnd(col)

#define x first
#define y second

template<typename T> T read()
{
	T t;
	cin >> t;
//	cerr << "read: " << t << endl;
	return t;
}

int readtime()
{
	int a, b;
	char t;
	cin >> 	a >> t >> b;
	return a*60 + b;
}

string readline()
{
	string line;
	getline(cin, line);
	return line;
}

template <typename T> inline void reset(T &t, const T &val) { t = val; }
template <typename T, int S> void reset(T (&t) [S], const T &val)
{
	for(int i=0; i<S; i++) reset(t[i], val);
}

vector<string> parse_strings(const string &s)
{
	istringstream is( s);
	string t;
	vector<string> vs;
	while(is >> t) vs.push_back(t);
	return vs;
}

void solve();

int main()
{
	int cases;
	cin >> cases; cin.ignore();
	for(int i=1; i<=cases; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}


/*
 * Code itself
 */
int N;
int px[1000];
int py[1000];
int pz[1000];
int pp[1000];

pair<long double,int> ps[1000];

void getFar(long double x, long double y, long double z)
{
	for(int i=0; i<N; i++)
	{
		ps[i].second = i;
		ps[i].first = (abs(x-px[i])+abs(y-py[i])+abs(z-pz[i])) / pp[i];
	}
	sort( ps, ps+N );
}

void solve()
{
	cin >> N;
	for(int i=0; i<N; i++)
		cin >> px[i] >> py[i] >> pz[i] >> pp[i];

	long double x = accumulate( px, px+N, 0.0);
	long double y = accumulate( py, py+N, 0.0);
	long double z = accumulate( pz, pz+N, 0.0);

	srandom(time(0));
	if(N > 1)
	{
		int last = -1;
		long double fac1 = 0.1;
		int steps = 500000;
		while(steps--)
		{
			getFar(x,y,z);
			int c1 = ps[N- 1].second;

			if(c1 != last) fac1 *= 0.999;


			x += ( px[ c1 ] - x )*fac1;
			y += ( py[ c1 ] - y )*fac1;
			z += ( pz[ c1 ] - z )*fac1;

			last = c1;
//			printf("%.6f %.6f %.6f : %.6f\n", x, y, z, ps[N-1].first);

/*
			x += px[ c2 ] * fac2;
			y += py[ c2 ] * fac2;
			z += pz[ c2 ] * fac2;
 */
//			if(fac1 < 1e-20) break;
		}
	}
	getFar(x,y,z);
	printf("%.6f\n", float(ps[N-1].first));
//	printf("%.6f %.6f %.6f\n", x, y, z);
}

