/****** String Library */
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>

/****** Containers */
#include <bitset>
#include <deque>
#include <stack>
//#include <queue> //queue - priority_queue
#include <vector>
#include <list>
#include <set> //set - multiset
#include <map> //map - multimap
//#include <iterator> //iterators for !need
//#include <valarray> ???

/****** Algorithms finds... sorts... merges... */
#include <algorithm>

/****** Functions' Adaptors and Objects */
#include <functional>

/****** Mth and Numeric Ops */
#include <cmath>
#include <complex>
#include <numeric>
#include <limits>

/****** Memory Utils */
#include <memory> 

/****** var */
#include <utility> 
#include <iomanip> 
#include <ctime> 

#define FOR(i, m, n) for (int i(m), _n(n); i<_n; ++i)
#define FORd(i, m, n) for (int i(m), _n(n); i>_n; --i)
#define FORc(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define FORr(it,c) for (__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define ALL(c) (c).begin(),(c).end()
#define ALLr(c) (c).rbegin(),(c).rend()

using namespace std;


int main()
{
	int N;
	int k;
	int n;
	int d, t, ps, p, v;
	int tm;

	string s;
	cout << setprecision(16);

	cin >> N;
	FOR(c,1,N+1)
	{
		cin >> n >> d;
		tm=0;
		ps = -99999999;
		FOR(i,0,n)
		{
			cin >> p >> v;
			ps = (p < ps + d) ? ps + d : p;
			ps += (v-1)*d;
			t = ps - p;
			if(tm < t)
				tm = t;
//			cout << p << " " << ps << " " << t << " " << tm << endl;
		}

		cout << "Case #" << c << ": "<< (long double)(tm)/2.0L << endl;
	}
	return 0;
}
