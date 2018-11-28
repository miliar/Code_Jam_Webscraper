#include <iostream>
#include <string>
#include <sstream>
#include <vector>

#include <iomanip>

/*
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <deque>
#include <queue>
#include <stack>
#include <valarray>
#include <vector>
#include <list>
#include <set> //set - multiset
#include <map> //map - multimap

#include <algorithm>
#include <functional>
#include <math.h>
#include <complex>
#include <numeric>
#include <limits>
#include <memory>
#include <utility>

/**/
#define FOR(i, m, n) for (int i(m), _n(n); i<_n; ++i)
#define FORd(i, m, n) for (int i=(m), _n=(n); i>_n; --i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

using namespace std;

int main(int argc, char *argv[])
{
	char wcj[25]= " welcome to code jam";
	int N;
	cin >> N;
	string t;
	getline( cin, t, '\n' );

	FOR(i,0,N)
	{
		unsigned int  tot[25] = {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		getline( cin, t, '\n' );
		FOR(d,0,t.size())
		{
// 			cerr << t[d] << "\t";
			FOR(l,1,20)
			{
				if (t[d]==wcj[l])
					tot[l]+=tot[l-1];
// 				cerr << " " << tot[l];
			}
// 			cerr << "\t\t" << tot[19] << endl;
		}
		cout << "Case #"<< i+1 << ": " << setw(4) << setfill('0') << tot[19]%10000 << ("\n");
// 		cerr << endl << endl;
	}
	return 0;
}
