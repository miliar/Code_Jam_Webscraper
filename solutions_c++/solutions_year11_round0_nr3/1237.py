/****** String Library */
#include <string>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

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

/****** Algorithms finds... sorts... merges... */
#include <algorithm>

/****** Functions' Adaptors and Objects */
#include <functional>

/****** Mth and Numeric Ops */
#include <math.h>
#include <complex>
#include <numeric>
#include <limits>

/****** Memory Utils */
#include <memory> 

/****** var */
#include <utility> 
#include <iomanip> 
#include <time.h> 

using namespace std;

#define FOR(i, m, n) for (int i=m, i_end=n; i<i_end; ++i)
#define FORd(i, m, n) for (int i=m-1, i_end=n; i>=i_end; --i)
#define FORit(type,it,cntnr) for (type::iterator it=cntnr.begin(); it!=cntnr.end(); ++it)
#define FORdit(type,it,cntnr) for (type::reverse_iterator it=cntnr.rbegin(); it!=cntnr.rend(); ++it)
#define FORit_(type,it,cntnr) for (type::iterator it=cntnr.begin()+1, _it=cntnr.end()-1;it != _it; ++it)
#define FORdit_(type,it,cntnr) for (type::reverse_iterator it=cntnr.rbegin()+1, _it=cntnr.rend()-1; it!=_it; ++it)

int main()
{
	int N;
	int t, tt, nc, mn, sP;

	cin >> N;
	FOR(c,1,N+1)
	{
		tt = sP = 0;
		cin >> nc;
		mn=99999999;

//		cerr  << " " << tt << " " << sP << endl;
		FOR(i,0,nc)
		{
			cin >> t;
			tt+=t;
			sP^=t;
			if(mn>t)mn=t;
//			cerr << t << " " << tt << " " << sP << endl;
		}
		cout << "Case #" << c << ": ";
		if (sP>0) cout << "NO";
		else
			cout << tt - mn;
		cout << endl;
	}
	return 0;
}
