#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#include <stdio.h>

int t , i , j , k ;
__int64 n;

int main()
{
	freopen("B-large.in" , "r" , stdin);
	freopen("B-large.out" , "w" , stdout);
	cin >> t;
	for(k = 1 ; k <= t ; k++)
	{
		//scanf("%I64d" , &n);
		int b[1000];
		char a[1000] , c[1000];
		//sprintf(a,"%d",n);
		cin >> a;
		j = strlen(a);
		for(i = 0 ; i < j ; i++)
		{
			b[i] = a[i] - 48 ;
		}

		if( next_permutation(b , b + j ) == 1)
		{
			cout <<"Case #"<< k <<": ";
			for(i = 0 ; i < j ; i++)
			{
				cout << b[i] ;
			}
		}
		else
		{
			sort(a,a+strlen(a));
			c[0] = a[0];
			c[1] = '0';
			for(i = 2 ; i <= strlen(a) ; i++)
			{
				c[i] = a[i - 1];
			}
			//sort(c + 1 , c + strlen(a) + 1 ); 
			while(c[0] == '0')
			{
				next_permutation(c , c + strlen(a) + 1 );
			}
			cout <<"Case #"<< k <<": ";
			for(i = 0 ; i <= strlen(a) ; i++)
			{
				cout << c[i] ;
			}
		}
		cout << endl;
	}
	return 0;
}