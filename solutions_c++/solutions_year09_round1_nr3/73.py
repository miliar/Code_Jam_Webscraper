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
int N, C;

double prob[41];

#define CMAX  110
 
using namespace std;
 
typedef unsigned long long ull;
 
ull c[CMAX][CMAX];  // o desperdício de memória é irrelevante
 
ull gcd(ull a, ull b) { while(b)  swap(a%=b, b);  return a; }
 
ull comb(int n, int p) {
  if(p > n) return 0;
  if(p == n) return 1;
  if(c[n][p]) return c[n][p];
  if(!p || n == p) return c[n][p] = c[n][n-p] = 1;
  if(p == 1 || n == p-1) return c[n][p] = c[n][n-p] = n;
 
  return c[n][p] = c[n][n-p] = comb(n-1, p-1) + comb(n-1, p);
  //if(c[n][p] < comb(n-1, p-1) || c[n][p] < comb(n-1, p)) => overflow
}
 // com repetição nFk = (n+k-1)!/(k!(n-1)!) => (x1+x2+...+xn=k), xi >= 0
ull rep_comb(int n, int k) { return comb(n+k-1, k); }


double prob_draw(int h, int n)
{
	double a = comb(C-h, n);
	double b = comb(h, N-n);
	double c = comb(C, N);

//	cout << "prob_draw(" << h << "," << n << ")=" << a << "*" << b << "/" << c << "= " << a*b/c << endl;
	if(c == 0)
		return 0;
	return a*b/c;
}


void advance()
{
	double new_prob[41] = {};
	for(int i=0; i<=C; i++)
	for(int j=0; j<=N && i+j <= C; j++)
		new_prob[i+j] += prob[i]*prob_draw(i, j);

	for(int i=0; i<=C; i++)
		prob[i] = new_prob[i];	
}

void debug()
{
	for(int i=0; i<=C; i++) cout << prob[i] << ";";
	cout << endl;
}

void solve()
{	
	cin >> C >> N;
//	cout << endl;
	
	double e = 0;
	double acc = 0;
	
	for(int i=0; i<=C; i++) prob[i] = 0;
	prob[0] = 1;
	
//	debug();
	for(int i=1; ; i++)
	{

		advance();		
//		debug();
		
		acc += prob[C];
		prob[C] = 0;
		e += 1.0-acc;
		
//		cout << "-- " << e << "\t" << acc << endl;
		if(1-acc < 10e-6) break;
	}
		
	cout << e+1 << endl;
//	cout << ":" << acc << endl;
}

