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

struct point 
{
	int x,y;
	point (int a,int b)
	{x = a; y = b;}
};
int main ()
{
	freopen("A-small-attempt1.in" , "rt" , stdin );
	//freopen("A-small-attempt1.out" , "wt" , stdout);
	int i,j,k,N,cc = 1;

	cin >> N ;

	while ( N > 0 )
	{
		int n, A, B, C, D, x0, y0, M ,X ,Y;
		cin >>  n>>  A >>  B >>  C >>  D >>  x0 >>  y0 >>  M;

		vector <point> v;
		X = x0; Y = y0;
		v.push_back(point(X,Y));

		for ( i = 1 ; i < n ; i ++ )
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			v.push_back(point(X,Y));
		}

		for ( i = 0 ; i < v.size () ; i ++ )
			cout << v[i].x <<" " << v[i].y <<"\t";
		cout << endl;

		int cnt = 0 ;
		for ( i = 0 ; i < n ; i ++ )
			for ( j = i+1 ; j < n ; j ++ )
				for ( k = j+1 ; k < n ; k ++ )
				{
					if (   ( v[i].x + v[j].x + v[k].x  ) % 3 == 0 &&  ( v[i].y + v[j].y + v[k].y  ) % 3 == 0    )   
						cnt++;
				}

		cout <<"Case #" << cc << ": " << cnt << endl;

		cc++;
		N-- ;
	}
	return 0;
}