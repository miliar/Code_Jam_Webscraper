#include<cstdio>
using namespace std;
main()
{
	int T,A,B;
	scanf("%d",&T);
	float arr[100000];
	double prob[100000];
	for(int i=0;i<T;i++)
	{
		//cin>>A>>B;
		scanf("%d%d",&A,&B);
		//printf("\nA & B is %d %d\n",A,B);
		double res=1.0;
		for(int j=0;j<A;j++)
		{
			scanf("%f",&arr[j]);
			res*=arr[j];
		}
		for(int j=0;j<=A;j++)
		{
			prob[j]=res;
			res=(res/arr[A-j-1])*(1-arr[A-j-1]);
		}
		float dummy=0;
		double prob_mul=0.0;
		float min=(float)B+2.0;
		for(int j=0;j<=A;j++)
		{
			prob_mul+=prob[j];
			dummy=prob_mul*(B-A+1+j*2);
			dummy+=(1-prob_mul)*(2*B-A+2+j*2);
			if(min>dummy)min=dummy;

		}


		printf("Case #%d: %f\n",i+1,min);

	}
	return 0;
}
