#include <iostream>
#include <cstdio>
#include <limits>

using namespace std;

double p[100000];
double keeptying, backonce, backtwice, enter;

struct Num
{
	int wrong;
	double p;
};

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int t, i, j;
	scanf("%d", &t);

	for(i = 1; i <= t; i++)
	{
		int A, B;
		scanf("%d%d", &A, &B);

		double pp = 1;

		for(j = 0; j < A; j++)
		{
			scanf("%lf", &p[j]);
			pp *= p[j];
		}

	    keeptying = pp * (B - A + 1) + (1-pp)*(B-A+1+B+1);

		backonce = 1;
		double tem = pp / p[A-1] * (1 - p[A-1]);
		backonce = pp * ( B - A + 3) + tem*(B - A + 3) + (1-pp-tem)*(B-A+3+B+1);

		if(A >= 2)
		{
			tem = pp/p[A-1] *(1-p[A-1]) + pp/p[A-1]/p[A-2]*(1-p[A-1])*(1-p[A-2])+pp/p[A-2]*(1-p[A-2]);

			backtwice = pp * ( B-A+5) + tem*(B-A+5) + (1-pp-tem)*(B-A+5+B+1);
		}
		else{
			backtwice = 1000000000;
		}

		enter = 1 + B + 1;

		double min = 1000000000;
		if(keeptying < min)
		{
			min = keeptying;
		}
		if(backonce < min)
		{
			min = backonce;
		}
		if(backtwice < min)
		{
			min = backtwice;
		}
		if(enter < min)
		{
			min = enter;
		}
		printf("Case #%d: %.6lf\n", i, min);
	}
	return 0;
}



		

		





