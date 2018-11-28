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
 #define MOD 1000000009
 
vector<int> edges[1000];
bool visited[1000];


long long count_visited(int node, int depth, int last)
{
  if(!visited[node]) return 0;
  if(depth == 0) return 0;
  
//  cout << node+1 << ",";
  
  long long sum = 0;
  foreach( edges[node], dest )
  {
    if(*dest != last)
      sum += count_visited( *dest, depth -1, node );
  }
  return sum+1;
}

long long ways(long long k)
{
  long long w = 1;
  queue<int> q;
  q.push(0);
  visited[0] = true;
  
  while(!q.empty())
  {
    int node = q.front();
    q.pop();
    
    foreach( edges[node], dest )
    if(!visited[*dest])
    {
      visited[*dest] = true;
      long long c = count_visited( *dest, 4, -1 )-2;
      
      
      w = (w*(k-c)) % MOD;
      
//      cout << endl << node+1 << "->" << *dest+1 << ":" << k-c << endl;
      
      q.push( *dest );
    }
    
    
  }

  return w;
}

void solve()
{
  long long n, k;
  cin >> n >> k;
//  cout << n << ":" << k << "---------\n";
  for(int i=0; i<n; i++)
    edges[i].clear(), visited[i] = false;
  
  for(int i=0; i<n-1; i++)
  {
    int a, b;
    cin >> a >> b;
    a--, b--;
    edges[a].push_back( b );
    edges[b].push_back( a );
  }
  
  
  cout << ways(k) << endl;  
}


