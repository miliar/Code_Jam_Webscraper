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
#define _join(a,b) a##b
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
#define foreach(col, iter) FOREACH(col, iter, _join(iter, __end))
#define all(col)    IterBegin(col), IterEnd(col)

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
#define MOD 10000
void solve()
{
	string msg = "welcome to code jam";
	vector<int> count(msg.size());
	
	string line;
	getline( cin, line );
	foreach(line, c)
	{
		for(int i=msg.size()-1; i>0; i--)
		if(msg[i] == *c)
			count[i] = (count[i] + count[i-1]) % MOD;
		if(*c == msg[0])
			count[0] = (count[0]+1) % MOD;
	}
	
	printf("%04d\n", count.back() );
}

