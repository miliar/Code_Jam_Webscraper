#include <iostream>
#include <cmath>
using namespace std;
int T,y;
char x;
int a[10000], b[10000];
char seq[10000];
int main()
{
	int n, i;
	cin >> T;
	for ( int ti = 1; ti <= T; ++ti )
	{
		cin >> n;
		int len1=0, len2 = 0;
		a[0] = b[0] =1;
		int pp1 = 1,pp2 = 1;
		for ( i = 1; i <= n; ++i )
		{
			cin >> x >> y;
			if ( x == 'O' )
			{
				++len1;
				a[len1] = 1+abs( y - pp1);
				pp1 = y;
			}
			else if ( x == 'B' )
			{
				++len2;
				b[len2] = 1+abs( y - pp2);
				pp2 = y;
			}
			seq[i] = x;
		}
		int p1 = 1, p2 = 1, ans = 0;
		a[n+1] = b[n+1] = 1000000000;
		for ( i = 1; i <= n; ++i )
		{
			if ( seq[i] == 'O' )
			{
				ans += a[p1];
				if ( a[p1] >=b[p2] ) b[p2] = 1;
				else b[p2] -=a[p1];
				++p1;
			}
			else
			{
				ans += b[p2];
				if ( b[p2] >= a[p1] ) a[p1] = 1;
				else a[p1] -= b[p2];
				++p2;
			}
		//	printf( "!%d %d %d\n", ans, p1, p2);
		}
		cout <<"Case #"<< ti <<": "<<ans << endl;
	}
}
