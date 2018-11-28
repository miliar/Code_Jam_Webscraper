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

/*
using maxima
(%i1) integrate( sqrt(r^2-x^2), x );

                        2        x
                       r  asin(------)           2    2
                               abs(r)    x sqrt(r  - x )
(%o1)                  --------------- + ---------------
                              2                 2
*/

long double radius;

long double F(long double x)
{
	return 0.5* ( radius*radius * asin( x / abs(radius) ) + x*sqrt( radius*radius - x*x ) );
}


long double sa(long double x0, long double x1)
{
	return F(x1) - F(x0);
}

long double fx(long double x)
{
	return sqrt( radius*radius - x*x );
}

long double clamp(long double l, long double u, long double v)
{
//	assert( u >= l);
	if( u < l ) swap( u, l);

	if( v > l )
	{
		if( v < u)
			return v;
		else
			return u;
	}
	else return l;
}

long double sqa(long double x0, long double x1, long double y0, long double y1)
{

//	cerr << "["<< x0 << "," << x1 << "]x[" <<  y0 << "," << y1 << "] = ";

	assert( x0 < x1 );
	assert( y0 > y1 );
	long double a = 0;

	long double mx0 = clamp(x0, x1, fx(y0) );

	a += (mx0 - x0) * (y0 - y1);
	x0 = mx0;
	y0 = fx(x0);
	
	long double my1 = clamp(y1, y0, fx(x1) );
	a += (my1 - y1) * (x1 - x0);
	y1 = my1;
	x1 = fx(y1);

	a += sa(x0, x1) - (x1-x0)*y1;

//	cerr << a << endl;
	return a;
}


long double prob(long double raquete, long double espaco, long double fio, long double mosca, long double raquete_width)
{
	long double area = 0;

	radius = raquete - raquete_width - mosca;
	
	for(int i=0; ; i++)
	{
		long double x0 = (2*i+1)*fio + i*espaco + mosca;
		long double x1 = (2*i+1)*fio + (i+1)*espaco - mosca;

		if(x0 >= x1) break;
		if(x0 >= radius) break;

		x0 = min(x0, radius);
		x1 = min(x1, radius);

		long double my0 = fx( x0 );

		for(int j=0; ; j++)
		{

			long double y1 = (2*j+1)*fio + j*espaco + mosca;
			long double y0 = (2*j+1)*fio + (j+1)*espaco - mosca;
			
			if(y1 >= my0) break;
			if(y1 >= y0) break;

			area += sqa(x0, x1, y0, y1);
		}
	}

	return 1.0 - area / (M_PI * raquete * raquete * 0.25 );
}

void solve()
{
	char buf[100];
	long double f, R, t, r, g;
	cin >> f >> R >> t >> r >> g;
	snprintf(buf, size(buf), "%.6f", (float)prob(R,g,r,f,t) );
	cout << buf << endl;
}

