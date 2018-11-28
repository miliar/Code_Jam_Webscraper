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

int gcd(int u, int v){
	if(u == v || u == 0 || v == 0)
		return u|v;
	if(u%2 == 0){ // if u is even
		if(v%2 == 0) // if u and v are even
			return (2*gcd(u/2, v/2));
		else // u is even and v is odd
			return  gcd(u/2, v);
	}
	else if(v%2 == 0) // if u is odd and v is even
		return gcd(u, v/2);
	else{ // both are odd
		if(u>=v)
			return gcd((u-v)/2, v);
		else
			return gcd((v-u)/2, u);
	}
}

int main()
{
	int N;
	int k;
	int n, pd, pg;
	int bd, bg, gd, wd;

	string s;

	cin >> N;
	FOR(c,1,N+1)
	{
		s = "Possible";
		cin >> n >> pd >> pg;
		if(pd > 0 && pg == 0) s = "Broken";
		if(pd < 100 && pg == 100) s = "Broken";
		if(pd != 0)
		{
			bd = gcd(100,pd);
			bg = gcd(100,pg);
			gd = 100/bd;
			wd = pd/bd;
			if(n / gd == 0) s = "Broken";
		}

		cout << "Case #" << c << ": ";
		cout << s; 
		cout << endl;
	}
	return 0;
}
