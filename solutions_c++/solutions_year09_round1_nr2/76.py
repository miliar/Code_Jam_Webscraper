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
 
int S[20][20];
int W[20][20];
int T[20][20];
int N, M;

long long best_time[4][20][20];
#include <string.h>

priority_queue< pair<long long, pair<int,pair<int,int> > >, vector< pair<long long, pair<int,pair<int,int> > > >, greater<  pair<long long, pair<int,pair<int,int> > > > > q;

void expand2(long long t, int p, int x, int y)
{
	if(x >= 0 && y >= 0 && x < M && y < N)
		if(best_time[p][y][x] == -1
		|| best_time[p][y][x] > t)
		{
			assert(t != -1);
			best_time[p][y][x] = t;
			q.push( make_pair(t, make_pair(p, make_pair(x,y) ) ) );
		}
}


long long cur_state(long long t, int x, int y)
{
	long long s = S[y][x]+W[y][x];
	long long p = (t%s - T[y][x]%s + s) % s;
	assert(p >= 0);
	return p;
}

long long next_stime(long long t, int x, int y)
{
	long long p = cur_state(t,x,y);
	if(p < S[y][x])
		return t;
	else
		return t + W[y][x] - (p-S[y][x]);
}

long long next_wtime(long long t, int x, int y)
{
	long long p = cur_state(t,x,y);
	if(p >= S[y][x])
		return t;
	else
		return t + S[y][x] - p;
}

void expand(long long t, int p, int x, int y)
{
	expand2(next_wtime(t,x,y)+1, p^1, x, y);
	expand2(next_stime(t,x,y)+1, p^2, x, y);

	if(p == 0)
	{
		expand2(t+2, 1, x-1, y);
		expand2(t+2, 2, x, y+1);
	}
	if(p == 1)
	{
		expand2(t+2, 0, x+1, y);
		expand2(t+2, 3, x, y+1);
	}
	if(p == 2)
	{
		expand2(t+2, 0, x, y-1);
		expand2(t+2, 3, x-1, y);
	}
	if(p == 3)
	{
		expand2(t+2, 1, x, y-1);
		expand2(t+2, 2, x+1, y);
	}
}

void debug()
{
	cout << endl << "Debug:\n";
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<M; j++)
			cout << best_time[2][i][j] << " " << best_time[3][i][j] << "---";
		cout << endl;
		for(int j=0; j<M; j++)
			cout << best_time[0][i][j] << " " << best_time[1][i][j] << "---";
		cout << endl;
	}
}

void bfs()
{
	while(!q.empty())
		q.pop();
	
	memset(best_time, -1, sizeof(best_time));
	
	expand2(0, 0, 0, N-1);
	while(!q.empty())
	{
		pair<long long, pair<int,pair<int,int> > > e = q.top();
		q.pop();

		if(best_time[e.second.first][e.second.second.second][e.second.second.first] == e.first)
			expand(e.first, e.second.first,e.second.second.first, e.second.second.second);
	}
}

void solve()
{
	
	cin >> N >> M;
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<M; j++)
		{
			cin >> S[i][j] >> W[i][j] >> T[i][j];
		}
	}

	bfs();
	
	cout << best_time[3][0][M-1] << endl;
}

