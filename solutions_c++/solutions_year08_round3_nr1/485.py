#include <stdio.h>
#include <cstdlib>
#include <ctype.h>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <queue>
using namespace std;


int main ()
{
	freopen("A-small-attempt0.in" , "rt" , stdin );
	freopen("A-small-attempt0.in" , "wt" , stdout );


	int N,i,j,cc=1;
	cin >> N ;

	while (N>0)
	{
		int p,k,lt;
		cin >> p >> k >> lt;

		//cout <<" ??? " << endl;
		vector<int> v;
		for ( i = 0 ; i < lt; i ++ )
		{
			int temp;
			cin >> temp;
			v.push_back(temp);
		}

		sort(v.rbegin() , v.rend () );

		int pres = 0;

		int ptr = 0;
		for ( i = 1 ; i <= p ; i ++ )
		{
			for ( j = 0 ; j < k ; j ++ )
			{
				pres += (v[ptr]*i);
				ptr++;
				if (ptr == v.size () )
					goto f;
			}
		}
f:

		cout <<"Case #"<<cc<<": "<<pres<<endl;



		cc++;
		N--;
	}
	return 0;
}