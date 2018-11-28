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
int state[1000];
void solve()
{
	int N;
	cin >> N;
	
//	cout << N << endl;
	
	for(int i=0; i<N; i++)
		state[i] = -1;
	
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<N; j++)
		{
			char t;
			cin >> t;
			assert( t == '1' || t == '0');
			if(t == '1')
				state[i] = max(state[i], j);
		}
	}
	
	
	int swaps = 0;
	for(int i=0; i<N; i++)
	{
		if(state[i] > i)
		{
			for(int j=1; i+j <= N; j++)
			if(state[i+j] <= i)
			{
				int nstate = state[i+j];
				for(int k=j; k>=1; k--)
					state[i+k] = state[i+k-1];
				state[i] = nstate;	
//				swap(state[i], state[i+j]);
				swaps += j;
				break;
			}
		}
//		cout << state[i] << " " << endl;
		assert(state[i] <= i);
	}
//	cout << "=>";
	cout << swaps << endl;
	
}

