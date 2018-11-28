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

vector <int> original;
vector <int> sorted;
vector <bool> test;

multimap<int, int> vectors;

int main()
{
	int N;
	int nc, tt, t, nv;
	original.reserve(1000);
	sorted.reserve(1000);

	cin >> N;
	FOR(c,1,N+1)
	{
		original.clear();
		sorted.clear();
		test.clear();

		cin >> nc;

		FOR(i,0,nc)
		{
			cin >> t;
			original.push_back(t);
		}
		sorted = original;
		sort(sorted.begin(),sorted.end());
		test.resize(sorted.size(),false);

		FOR(i,0,nc)
			if(original[i]!=sorted[i])
				vectors.insert(pair<int,int>(sorted[i],original[i]));
		tt = 0;

		while(vectors.size())
		{
			t = 1;
			nv = (*(vectors.begin())).second;
			//cerr << " cc " << (*(vectors.begin())).first << " " << nv ;
			for(multimap<int,int>::iterator nt = vectors.lower_bound(nv);
					nt != vectors.begin();
					nt = vectors.lower_bound(nv))
			{
			   nv = (*nt).second;
			   vectors.erase(nt);
			   t++;
			   //cerr << " " << nv;
			}
			vectors.erase(vectors.begin());
			tt += t;
			//cerr << " t " << t << " " << tt << endl;
		}

		cout << "Case #" << c << ": ";
		printf ("%.6f", 1.0 * tt);
//		cout << tt * 2.0;
		cout << endl;
	}
	return 0;
}
