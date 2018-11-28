#include <stdio.h>
#include <string.h>
#include <math.h>

#define eps 0.00000001

int main()
{
	int T,u,N,i,j;
	int list[501][6];
	
	scanf("%d",&T);
	for( u = 1 ; u <= T ; ++u )
	{
		scanf("%d",&N);
		for( i = 0 ; i < N ; ++i )
		{
			for( j = 0 ; j < 6 ; ++j )
			{
				scanf("%d",&list[i][j]);
			}
		}
		double a1,a2,a3,b1,b2,b3;
		a1 = a2 = a3 = b1 = b2 = b3 = 0;
		for( i = 0 ; i < N ; ++i )
		{
			b1 += list[i][0];
			b2 += list[i][1];
			b3 += list[i][2];
			a1 += list[i][3];
			a2 += list[i][4];
			a3 += list[i][5];
		}
		a1 = a1 / N;
		b1 = b1 / N;
		a2 = a2 / N;
		b2 = b2 / N;
		a3 = a3 / N;
		b3 = b3 / N;
		double a,b,c,res,dis;
		a = a1*a1 + a2*a2 + a3*a3;
		b = 2*a1*b1 + 2*a2*b2 + 2*a3*b3;
		c = b1*b1 + b2*b2 + b3*b3;
		if( fabs(a) > eps )
		{
			res = - b / (2*a);
			if( res < 0 && fabs( res ) > eps )
				res = 0;
			dis = a*res*res + b*res + c;
			if( fabs( dis ) < eps )
				dis = 0;
			else
				dis = sqrt( dis );
		}
		else
		{
				res = 0;
				dis = sqrt(c);
		}
		//printf("%lf,%lf\n",a,b);
		printf("Case #%d: %lf %lf\n",u,fabs(dis),fabs(res));
	}
}
