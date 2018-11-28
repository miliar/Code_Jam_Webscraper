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
int N, K;
long long price[101][101];
long long touch[101][101];

int nt[100];

int best[1<<16];

bool cross(int a, int b, int k)
{
	if(k+1 == K)
		return price[a][k] == price[b][k];
		
	return (price[a][k]-price[b][k])*(price[a][k+1]-price[b][k+1]) <= 0;
}

int used, current, cost;

void dfs(int p)
{

	while( ((1<<p) & (used|current)) && p < N)
		p++;
	
	assert( p <= N);
	if(p == N)
	{
		int ob = best[used|current];
		best[used | current] = min( best[used | current], cost);
		if(ob == best[used|current]) return;
	
		//Start a new only with p
		for(int i=0; i<N; i++)
		if( ( (1<<i) & (used|current)) == 0)
		{
			int lused = used;
			int lcurr = current;
			cost++;
		
			used |= current;
			current = (1<<i);
			dfs(i);
		
			cost--;
			used = lused;
			current = lcurr;
			return;
		}		
		return;
	}
	else
	{
		//Skip
		dfs(p+1);
	
		//Use
		if( (nt[p] & current) == 0)
		{
			current |= (1<<p);
			dfs(p+1);
			current &= ~(1<<p);
		}
	}
	
}

void solve()
{
	cin >> N >> K;
	
	for(int i=0; i<N; i++)
	for(int j=0; j<K; j++)
		cin >> price[i][j];
	
	for(int a=0; a<N; a++)
	for(int b=0; b<N; b++)
		touch[a][b] = 0;
	
	for(int k=0; k<K; k++)
	{
		for(int a=0; a<N; a++)
		for(int b=0; b<N; b++)
		if(cross(a, b, k))
			touch[a][b] = touch[b][a] = 1;
	}
	for(int a=0; a<N; a++)
	{
		nt[a] = 0;
		for(int b=0; b<N; b++)
		if(touch[a][b])
			nt[a] |= (1<<b);
	}
	
	for(int a=0; a<(1<<N); a++)
		best[a] = N+100;

	used = 0;
	current = 0;
	cost = 1;
	dfs(0);
	
	assert( best[(1<<N)-1] != N+100);
	cout << best[(1<<N)-1] << endl;	
}

