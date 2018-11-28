#include <stdio.h>
#include <iostream>
using namespace std;
int Dp[100*100+5];
int Vs[100*100+5];
int B[100];
int N;
long long L;
int main()
{	
	int T;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		scanf("%lld %d",&L,&N);
		for (int q=0;q<N;++q)
			scanf("%d",&B[q]);
		const int M =10000;
		for (int q=0;q<=M;++q) { Dp[q]=Vs[q]=0; }
		Vs[0]=1;
		for (int q=0;q<=M;++q)
			if (Vs[q])
			{
				for (int w=0;w<N;++w)
				{
					int e = q + B[w];
					if (e>=M) continue;
					if (!Vs[e] || Dp[e] > Dp[q] + 1)
					{
						Vs[e] = 1;
						Dp[e] = Dp[q] + 1;
					}
				}
			}
		int MAXB = B[0];
		for (int q=1;q<N;++q)
			if (B[q]>MAXB)
				MAXB=B[q];

		long long ret = -1;
		int md = L % MAXB;
		long long used = L / MAXB;

		for (;md<=M && used>=0;)
		{
			if (Vs[md])
			{
				if (ret<0 || ret > used + Dp[md])
				{
					ret = used + Dp[md];
				}
			}
			used--;
			md += MAXB;
		}
		if (ret>=0)
			printf("Case #%d: %lld\n",kase,ret);
		else 
			printf("Case #%d: IMPOSSIBLE\n",kase);
	}

	return 0;
}