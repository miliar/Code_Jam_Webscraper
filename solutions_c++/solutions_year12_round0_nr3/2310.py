#include<iostream>
using namespace std;
int fl[ 2000001];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.ans","w",stdout);
	int tc, cs = 1, cc = 1;
	cin >> tc;
	while( tc -- )
	{
		int a, b, i,j;
		cin >> a >> b;
		int m = 1, cnt = 0;;
		while( m <= a ) m *=10;
		for(i = a; i <= b ; i ++ )
		{
			cc++;
			for(j = 10; j <= i; j *= 10 )
			{
				int x = (i % j) * (m / j) + ( i / j );
				if( x > i && x <= b )
				{
					if( fl[ x - i ] != cc )
						cnt ++;
					fl[ x - i ] = cc;
				}
			}
		}
		printf("Case #%d: %d\n", cs++, cnt );
	}

	return 0;
}