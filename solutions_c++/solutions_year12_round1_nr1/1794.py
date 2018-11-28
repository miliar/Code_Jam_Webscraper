#include <iostream>
#include <cstdio>

using namespace std;

double P[4];
int A,B,T;
double Ans;

int main()
{
	scanf("%d\n",&T);
	for ( int i(1) ; i<=T ; ++i )
	{
		scanf("%d %d\n",&A,&B);
		for ( int j(1) ; j<=A ; ++j )
			scanf("%lf",&P[j]);
		switch (A)
		{
			case 1:
				Ans = (2*B+1)*(1-P[1]) + P[1]*B ;
				if ( Ans > (2+B) ) Ans = 2+B ;
				break;
			case 2:
				Ans = 2*B - B*P[1]*P[2] - P[1]*P[2] ;
				if ( Ans > ((2*B+2) - (B+1)*P[1]) )
					Ans = (2*B+2) - B*P[1] - P[1] ;
				if ( Ans > (2+B) ) Ans = 2+B ;
				break;
			case 3:
				Ans = 2*B+3 - B*P[1] - P[1] ;
				if ( Ans > (2*B+1 - P[1]*P[2] - B*P[1]*P[2]) )
					Ans = 2*B+1 - P[1]*P[2] - B*P[1]*P[2] ;
				if ( Ans > (2*B-1 - B*P[1]*P[2]*P[3] - P[1]*P[2]*P[3]) )
					Ans = 2*B-1 - B*P[1]*P[2]*P[3] - P[1]*P[2]*P[3] ;
				if ( Ans > (2+B) ) Ans = 2+B ;
				break;
		}
		printf("Case #%d: %.6lf\n",i,Ans);
	}
	return 0;
}
