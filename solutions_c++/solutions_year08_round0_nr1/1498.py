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
#include <fstream>

using namespace std;



int main()
{
	ifstream in ( "input.txt" , ifstream::in );
	ofstream out ( "output.txt" , ifstream::out );

	int n ;
	in >> n;
	int MAX = 1000000;
	int a[1000][100] ;

	map<string,int> m;

	for( int tcase = 0 ; tcase < n ; ++tcase)
	{
		m.clear();
		int s ;
		int q;
		in >> s;
		for( int i = 0 ; i < s ; ++i)
		{
			string t;
			getline(in,t);
			if(t == "")
			{
				--i;
				continue;
			}
			m[t] = i ;
		}

		in >> q;

		if( q == 0 )
		{
			out << "Case #" << tcase + 1 << ": " << 0 << endl;
			continue;
		}

		string t ;
	
		// offset the number
		getline(in,t);

		getline(in,t);
		int curstr = m[t];

		// init the array

		for( int i = 0 ; i < s ; ++i)
		{
			if( curstr == i) a[0][i] = MAX;
			else a[0][i] = 0;
		}

		for( int i = 1 ; i < q ; ++i )
		{
			getline(in,t);
			curstr = m[t];
			// try using the jth search engine.
			for( int j = 0 ; j < s ; ++j)
			{
				// j can not be used
				if( curstr == j )
				{
					a[i][j] = MAX;
					continue;
				}
				// j can be used.

				int usej = a[i-1][j];
				
				// min without j begin used

				int last = MAX;
				for( int k = 0 ; k < s ;  ++k)
				{
					if( k == j ) continue;
					last = min(last,a[i-1][k]);
				}

				a[i][j] = min( usej,last+1);
			}
		}

		int mi = MAX;
		for( int i = 0 ; i < s ; ++i)
			mi = min(mi,a[q-1][i]);

		out << "Case #" << tcase + 1 << ": " << mi << endl;
			




	}

	getchar();
	return 0;
}
