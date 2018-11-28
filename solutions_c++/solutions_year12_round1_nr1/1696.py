#include <cstdio>

double expected;

int main(void)
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j,t,A,B,T;
	double p[5],prod,exp;
	scanf(" %d",&T);
	for(int t = 1; t <= T; ++t)
	{
		prod = 1.0;
		expected = 0.0;
		scanf("%d%d",&A,&B);
		for(i=0; i<A; i++)
		{
			scanf("%lf",&p[i]);
			prod *= p[i];
		}

		exp = prod*(B-A+1) + (1-prod)*(2*B-A+2);
		expected = (exp>B+2)?B+2:exp;

		if(A==2)
		{
			double pr = p[0] * (1-p[1]);
			exp = prod*(B-A+3) + (1-prod-pr)*(2*B-A+4) + pr*(B-A+3);
			if(expected > exp)
				expected = exp;
		}

		if(A==3)
		{
            double pr = p[0] * p[1] * (1-p[2]);
			exp = prod*(B-A+3) + (1-prod-pr)*(2*B-A+4) + pr*(B-A+3);
			if(expected > exp)
				expected = exp;

			exp = 0.5*(3*B-2*A+11);
			if(expected > exp)
				expected = exp;
		}

		printf("Case #%d: %f\n",t,expected);
	}
	return 0;
}
