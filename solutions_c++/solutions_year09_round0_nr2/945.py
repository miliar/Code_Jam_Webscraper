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
		cout << "Case #" << i << ":\n";
		solve();
	}
	return 0;
}


/*
 * Code itself
 */

int delta[][2] = { {0,-1}, {-1,0}, {1,0}, {0,1} };
int uset[100*100];

void init_set(int size)
{
	for(int i=0; i<size; i++)
		uset[i] = i;
}

int find_set(int c)
{
	if(uset[c] == c) return c;
	return uset[c] = find_set(uset[c]);
}

void join_set(int a, int b)
{
	a = find_set(a);
	b = find_set(b);
	if(a == b) return;
	if(a > b) swap(a,b);
	uset[b] = a;
}

//
int H, W;
int weight[100][100];

int get_id(int x, int y)
{
	if(x >= 0 && x < W && y >= 0 && y < H)
		return y*W + x;
	else
		assert( false );
}

int getWeight(int x, int y)
{
	if(x >= 0 && x < W && y >= 0 && y < H)
		return weight[y][x];
	else
		assert( false );
}

void solve()
{
	cin >> H >> W;
	
	for(int i=0; i<H; i++)
	for(int j=0; j<W; j++)
		cin >> weight[i][j];
	
	init_set( H * W );
		
	for(int y=0; y<H; y++)
	for(int x=0; x<W; x++)
	{
		int bc = -1;
		int best = getWeight(x, y);
		for(int k=0; k<4; k++)
		{
			int nx = x+delta[k][0];
			int ny = y+delta[k][1];
			if(nx >= 0 && nx < W && ny >= 0 && ny < H)
			{
				int w = getWeight(nx, ny);
				if(w < best)
				{
					best = w;
					bc = k;
				}
			}
		}
		
		if(bc != -1)
		{
			join_set( get_id(x, y), get_id(x+delta[bc][0], y+delta[bc][1]) );
		}
	}
	
	map<int,char> id;
	for(int y=0; y<H; y++)
	{
		for(int x=0; x<W; x++)
		{
			int pid = find_set( get_id(x,y) );
			char &code = id[pid];
			if(code == 0)
				code = 'a'+id.size()-1;

			if(x != 0) cout << " ";
			cout << code;
		}
		cout << endl;
	}
	assert(id.size() <= 26 );
}

