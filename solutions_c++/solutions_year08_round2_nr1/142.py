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
#define y0 __y0__
long long N, A, B, C, D, x0, y0, M;
vector< pair<long long,long long> > trees;

void gen()
{
	long long X = x0, Y = y0;

	trees.push_back(make_pair( X, Y ));

	for(long long i=1; i<N; i++)
	{
		X = (A*X + B) % M;
		Y = (C*Y + D) % M;
		trees.push_back(make_pair( X, Y ));
	}
//	foreach(trees, t) cout << "(" << t->x << "," << t->y << ")\n";
}

void solve()
{
	trees.clear();
	cin >> N >> A >> B >> C>> D >> x0 >> y0 >> M;
	gen();

	long long p[3][3] = {};

	foreach(trees, t)
		p[ t->x % 3][ t->y % 3]++;
	

	long long ways = 0;	

	for(long long i1=0; i1<3; i1++)
	for(long long i2=0; i2<3; i2++)
	for(long long j1=0; j1<3; j1++)
	for(long long j2=0; j2<3; j2++)
	for(long long k1=0; k1<3; k1++)
	for(long long k2=0; k2<3; k2++)
	{
		long long sX = i1+j1+k1;
		long long sY = i2+j2+k2;

		if(sX % 3 == 0 && sY % 3 == 0)
		{
			long long I = p[i1][i2]--;
			long long J = p[j1][j2]--;
			long long K = p[k1][k2]--;

			if(K > 0)
				ways += I*J*K;

			p[i1][i2]++;
			p[j1][j2]++;
			p[k1][k2]++;
		}
	}
			
	cout << ways / 6 << endl;
}

