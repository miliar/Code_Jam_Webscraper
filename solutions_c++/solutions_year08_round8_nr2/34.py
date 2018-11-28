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
 
int needed(const vector< pair<int,int> > &a, const vector< pair<int,int> > &b)
{
  vector<pair<int,int> > sum( a.size() + b.size() );
  
  merge( all(a), all(b), sum.begin() );

//  foreach(a, i) sum.push_back( *i );
//  foreach(b, i) sum.push_back( *i );

//  foreach(c, i) sum.push_back( *i );
  
//  sort(all(sum));
  
//  foreach(sum, s)  cout << "[" << s->first << "," << s->second << "],";
  
  int painted_end = 1;
  int current_end = 1;
  int needed = 0;
  foreach(sum, i)
  {
    if(i->second > current_end && i->first <= current_end)
    {
      if(i->first > painted_end)
      {
        needed++;
        painted_end = current_end;
        current_end = i->second;
      }
      else if(i->first <= painted_end && i->second > current_end)
      {
        current_end = i->second;
      }   
      else
      {
        cout << "frjkfhjrek\n";
      }     
            
    }
    
  }
  int ret = INT_MAX;
  if(current_end == 10001)
    ret = needed+1;

  return ret;
}
 
void solve()
{

  map<string, vector< pair<int,int> > > offers;
  int N;
  cin >> N;
  for(int i=0; i<N; i++)
  {
    string C;
    int A, B;
    cin >> C >> A >> B;
    offers[C].push_back( make_pair( min(A,B), max(A,B)+1 ) );
  }
  
  foreach(offers, o)
    sort( all(o->second) );
  
  int best = INT_MAX;
  map<string, vector< pair<int,int> > >::iterator oend = offers.end();
  vector< pair<int,int> > empty;
  foreach( offers, o)
  {
    for(map<string, vector< pair<int,int> > >::iterator o2 = o; o2 != oend; o2++)
    {
      vector<pair<int,int> > sum( o->second.size() + o2->second.size() );
      merge( all(o->second), all(o2->second), sum.begin() );
      
      for(map<string, vector< pair<int,int> > >::iterator o3 = o2; o3 != oend; o3++)
      {
        best = min( best, needed( sum, o3->second ) );
      }
    }
  }
  
  if(best == INT_MAX)
    cout << "IMPOSSIBLE\n";
  else
    cout << best << endl;     
}








