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

int K;
char buf[60000] = {};
int num[20];

inline int rle_size()
{
//	cout << "rle_size"<< endl;

	char *stat = buf, last = 0;
	int n = 0;

	while(*stat)
	{
//		cout << stat << endl;
		for(int i=0; i<K; i++)
		{
			if(last == stat[ num[i] ]) continue;
			last = stat[ num[i] ];
			n++;
		}
		stat = stat + K;
	}
	return n;
}


void solve()
{
	cin >> K;
	cin >> buf;

	for(int i=0; i<K; i++)	 num[i] = i;

	int best = INT_MAX;
	do
	{
		best = min( best, rle_size() );

	} while(next_permutation( num , num + K) );

	cout << best << endl;
}

