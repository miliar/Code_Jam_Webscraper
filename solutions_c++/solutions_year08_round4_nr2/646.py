#include<stdio.h>
#include<math.h>

double dis( int x1, int y1, int x2, int y2 )
{
	return sqrt( (double)( (x1-x2)*(x1-x2) + (y1 -y2)*(y1-y2) ) );
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int ca;
	for( ca = 1; ca <= T; ca ++ )
	{
		int n,m;
		int val;
		scanf("%d%d%d", &n, &m, &val);
		double s = (double)(val) / 2.0;
		int x1,x2,y1,y2;
		int flag = 0;
		for( x1 = 0; x1 <=n; x1 ++ )
		{
			for( y1 = 0; y1 <= m ; y1 ++ )
			{
				for( x2 = 0; x2 <=n; x2 ++ )
				{
					for( y2 = 0; y2 <=m; y2 ++ )
					{
						double a = dis( 0,0, x1, y1);
						double b = dis(0,0, x2, y2);
						double c = dis(x1,y1, x2,y2);
						double p = (a+b+c)/2.0;
						double re = sqrt(p*(p-a)*(p-b)*(p-c));
						if( fabs( re - s) < 0.1 )
						{
							flag = 1;
							goto out;
						}
					}
				}
			}
		}
out:
		if( flag )
		{
			printf("Case #%d: %d %d %d %d %d %d\n",ca,0,0,x1,y1,x2,y2);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", ca);
		}
	}
	return 0;
}