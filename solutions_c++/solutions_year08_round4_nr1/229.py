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
int ntype[20000], nchange[20000];
int leaf[20000];
int dp[20000][2];
int Nnodes;

int getMin(int node, int val)
{
	if(node >= Nnodes)
	{
//		cout << node << " is leaf\n";
		if(val == leaf[node]) return 0;
		return INT_MAX/4;
	}
	if(dp[node][val] == -1)
	{
		int a = 2*node, b = 2*node + 1;
		int best = INT_MAX / 4;
		//And gate
		if(ntype[node] == 1)
		{
			if(val == 1)
			{
				best = min( best, getMin(a, 1) + getMin(b, 1) );
			}
			else
			{
				best = min( best, getMin(a, 0) + getMin(b, 1) );
				best = min( best, getMin(a, 0) + getMin(b, 0) );
				best = min( best, getMin(a, 1) + getMin(b, 0) );
			}
		}
		else
		{
			if(val == 1)
			{
				best = min( best, getMin(a, 0) + getMin(b, 1) );
				best = min( best, getMin(a, 1) + getMin(b, 1) );
				best = min( best, getMin(a, 1) + getMin(b, 0) );
			}
			else
			{
				best = min( best, getMin(a, 0) + getMin(b, 0) );
			}
			
		}

		if(nchange[node])
		{
			if(ntype[node] != 1)
			{
				if(val == 1)
				{
					best = min( best, 1+getMin(a, 1) + getMin(b, 1) );
				}
				else
				{
					best = min( best, 1+getMin(a, 0) + getMin(b, 1) );
					best = min( best, 1+getMin(a, 0) + getMin(b, 0) );
					best = min( best, 1+getMin(a, 1) + getMin(b, 0) );
				}
			}
			else
			{
				if(val == 1)
				{
					best = min( best, 1+getMin(a, 0) + getMin(b, 1) );
					best = min( best, 1+getMin(a, 1) + getMin(b, 1) );
					best = min( best, 1+getMin(a, 1) + getMin(b, 0) );
				}
				else
				{
					best = min( best, 1+getMin(a, 0) + getMin(b, 0) );
				}
				
			}
		}

		if(best > INT_MAX/4)
			best = INT_MAX/4;

		dp[node][val] = best;
	}
	return dp[node][val];
}

void solve()
{
	int M, V;
	cin >> M >> V;

	memset( dp, -1, sizeof(dp) );

	int nodes = (M-1) / 2;
	for(int i=1; i<=nodes; i++)
		cin >> ntype[i] >> nchange[i];

	Nnodes = nodes+1;
	int leafs = (M+1) / 2;
	for(int i=1; i<=leafs; i++)
	{
		cin >> leaf[nodes+i];
//		cerr << "leaf: " << nodes+i << "=" << leaf[nodes+i] << endl;
	}

//	cout << getMin(2, 1) << endl;

	int v = getMin(1, V);
	if(v == INT_MAX/4)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << v << endl;
}

