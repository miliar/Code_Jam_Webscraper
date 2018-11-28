#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()

using namespace std;

int v( char c)
{
	if( c>='0' && c<= '9' ) return c - '0';
	return c - 'a' + 10;	
}

int main()
{

    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

	int n;
	char a[62];
	scanf("%d", &n);
	for( int u = 1; u<= n; u++)
	{
		cin >> a;
		int x = strlen(a), ok = 1, c = 1;
		vector<int> val(36, -1);
		for( int i = 0; i< x; i++)
		{
			if( i > 0 && ok)
			{
				c = 0;
				ok = 0;		
			}
			if( val[ v(a[i]) ] == -1 )
			{
				val[ v(a[i]) ] = c;
				if( c != 0 ) c++;
				else c = 2;
			}		
		}
		int b=1;
		for( int i = 0 ; i< x; i++ )
			b = max( b, val[ v(a[i]) ] );
		b++;	
		long long res = 0, pot = 1, B = b;

		for( int i = 0 ; i< x; i++ )
		{
			res += (long long)(val[ v(a[x-i-1]) ]) * pot;
			pot = pot * B;	
		}
		printf("Case #%d: ", u);
		cout<<res;	
		printf("\n");

	}
//system("pause");
return 0;
}
