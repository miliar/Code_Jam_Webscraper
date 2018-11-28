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
#include <memory>
#include <cstring>
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

int L, D;
vector<string> words;

void solve();

int main()
{
	int cases;
	cin >> L >> D >> cases; cin.ignore();
	words.resize(D);
	foreach(words, w) cin >> *w;
	
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
int pattern[15][256];

void load(string w)
{
	memset( pattern, 0, sizeof(pattern) );

	int pos = 0;
	int in_group = 0;
	foreach(w, c)
	{
		if(in_group)
		{
			if(*c == ')') in_group--, pos++;
			else
				pattern[ pos ][ int(*c) ]= 1;
		}
		else
		{
			if(*c == '(') in_group++;
			else
				pattern[ pos++ ][ int(*c) ]= 1;
		}
	}
}

bool match(string &w)
{
	int pos = 0;

	foreach(w, c)
	if(pattern[pos++][int(*c)] == 0)
		return false;

	return true;
}
 
void solve()
{
	string word;
	cin >> word;

	int matchs = 0;
	load(word);
	
	foreach(words, w)
		if(match(*w))
			matchs++;
			
	cout << matchs << endl;
}

