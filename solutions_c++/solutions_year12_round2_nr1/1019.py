#include <iostream>
#include <cstdio>

using namespace std;

int T,N,Nums[202],More0;
double Sums;
double Ans[202];

int main()
{
	scanf("%d\n",&T);
	for (int i(1);i<=T;++i)
	{
		Sums=0,More0=0;
		scanf("%d",&N);
		for (int j(1);j<=N;++j)
			scanf("%d",&Nums[j]),Sums+=Nums[j];
		for (int j(1);j<=N;++j)
		{
			Ans[j]=(Sums*2/N-Nums[j])/Sums;
			if (Ans[j]>0) ++More0;
		}
		for (int j(1);j<=N;++j)
		{
			if (Ans[j]<0)
			{
				for (int k(1);k<=N;++k)
					if (Ans[k]>0) Ans[k]+=Ans[j]/More0;
				Ans[j]=0;
			}
		}
		printf("Case #%d:",i);
		for (int j(1);j<=N;++j)
			printf(" %.6lf",Ans[j]*100);
		printf("\n");
	}
	return 0;
}
