#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,A,B,CASE=0;
	int i,j,k,p;

	double a[100005];

	double res,temp;

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d %d",&A,&B);

		for(i=0; i<A; i++)
			scanf("%lf",&a[i]);

		res = 999999999.00;

		if(A == 1)
		{
			temp = a[0]*(B-A+1) + (1-a[0])*(B-A+1+B+1);
			if(temp < res)
				res = temp;

			temp = a[0]*(1+(B-A+1)+1) + (1-a[0])*(1+(B-A+1)+1);
			if(temp < res)
				res = temp;

			temp = a[0]*(1+B+1) + (1-a[0])*(1+B+1);
			if(temp < res)
				res = temp;


		}
		else if(A == 2)
		{
			temp = (a[0]*a[1])*(B-A+1) + a[0]*(1-a[1])*(B-A+1+B+1) + (1-a[0])*a[1]*(B-A+1+B+1) + (1-a[0])*(1-a[1])*(B-A+1+B+1);
			if(temp < res)
				res = temp;

			temp = (a[0]*a[1])*(1+B-A+1+1) + a[0]*(1-a[1])*(1+B-A+1+1) + (1-a[0])*a[1]*(1+B-A+1+1+B+1) + (1-a[0])*(1-a[1])*(1+B-A+1+1+B+1);
			if(temp < res)
				res = temp;

			temp = (a[0]*a[1])*(2+B-A+2+1) + a[0]*(1-a[1])*(2+B-A+2+1+B+1) + (1-a[0])*a[1]*(2+B-A+2+1+B+1) + (1-a[0])*(1-a[1])*(2+B-A+2+1+B+1);
			if(temp < res)
				res = temp;

			temp = (a[0]*a[1])*(1+B+1) + a[0]*(1-a[1])*(1+B+1) + (1-a[0])*a[1]*(1+B+1) + (1-a[0])*(1-a[1])*(1+B+1);
			if(temp < res)
				res = temp;

		}
		else if(A == 3)
		{
			temp = a[0]*a[1]*a[2]*(B-A+1) + a[0]*a[1]*(1-a[2])*(B-A+1+B+1) + a[0]*(1-a[1])*a[2]*(B-A+1+B+1) + a[0]*(1-a[1])*(1-a[2])*(B-A+1+B+1) +
					(1-a[0])*a[1]*a[2]*(B-A+1) + (1-a[0])*a[1]*(1-a[2])*(B-A+1+B+1) + (1-a[0])*(1-a[1])*a[2]*(B-A+1+B+1) + (1-a[0])*(1-a[1])*(1-a[2])*(B-A+1+B+1);
			if(temp < res)
				res = temp;

			temp = a[0]*a[1]*a[2]*(1+B-A+1+1) + a[0]*a[1]*(1-a[2])*(1+B-A+1+1) + a[0]*(1-a[1])*a[2]*(1+B-A+1+1+B+1) + a[0]*(1-a[1])*(1-a[2])*(1+B-A+1+1+B+1) +
					(1-a[0])*a[1]*a[2]*(1+B-A+1+1+B+1) + (1-a[0])*a[1]*(1-a[2])*(1+B-A+1+1+B+1) + (1-a[0])*(1-a[1])*a[2]*(1+B-A+1+1+B+1) + (1-a[0])*(1-a[1])*(1-a[2])*(1+B-A+1+1+B+1);
			if(temp < res)
				res = temp;

			temp = a[0]*a[1]*a[2]*(2+B-A+2+1) + a[0]*a[1]*(1-a[2])*(2+B-A+2+1) + a[0]*(1-a[1])*a[2]*(2+B-A+2+1) + a[0]*(1-a[1])*(1-a[2])*(2+B-A+2+1) +
					(1-a[0])*a[1]*a[2]*(2+B-A+2+1+B+1) + (1-a[0])*a[1]*(1-a[2])*(2+B-A+2+1+B+1) + (1-a[0])*(1-a[1])*a[2]*(2+B-A+2+1+B+1) + (1-a[0])*(1-a[1])*(1-a[2])*(2+B-A+2+1+B+1);
			if(temp < res)
				res = temp;

			temp = a[0]*a[1]*a[2]*(3+B-A+3+1) + a[0]*a[1]*(1-a[2])*(3+B-A+3+1) + a[0]*(1-a[1])*a[2]*(3+B-A+3+1) + a[0]*(1-a[1])*(1-a[2])*(3+B-A+3+1) +
					(1-a[0])*a[1]*a[2]*(3+B-A+3+1) + (1-a[0])*a[1]*(1-a[2])*(3+B-A+3+1) + (1-a[0])*(1-a[1])*a[2]*(3+B-A+3+1) + (1-a[0])*(1-a[1])*(1-a[2])*(3+B-A+3+1);
			if(temp < res)
				res = temp;

			temp = a[0]*a[1]*a[2]*(1+B+1) + a[0]*a[1]*(1-a[2])*(1+B+1) + a[0]*(1-a[1])*a[2]*(1+B+1) + a[0]*(1-a[1])*(1-a[2])*(1+B+1) +
					(1-a[0])*a[1]*a[2]*(1+B+1) + (1-a[0])*a[1]*(1-a[2])*(1+B+1) + (1-a[0])*(1-a[1])*a[2]*(1+B+1) + (1-a[0])*(1-a[1])*(1-a[2])*(1+B+1);
			if(temp < res)
				res = temp;


		}




		printf("Case #%d: %lf\n",CASE, res);

	}




}