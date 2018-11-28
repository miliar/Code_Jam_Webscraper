#include <stdio.h>
int N,K,B,T;
int X[55],V[55];
int Good[55];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int TEST;
	scanf("%d",&TEST);
	for (int kase=1;kase<=TEST;++kase)
	{
		scanf("%d %d %d %d",&N,&K,&B,&T);
		for (int q=0;q<N;++q) scanf("%d",X+q);
		for (int q=0;q<N;++q) scanf("%d",V+q);
		//1B + 0.1M < 2^31.
		for (int q=0;q<N;++q) Good[q] =(int)( (X[q] + V[q]*T) >= B );
		int bad = 0;
		int ret = 0;
		int suc = 0;
		for (int q=N-1;q>=0 && suc<K;q--)
		{
			if (!Good[q]) bad++;
			else
			{
				suc++;
				ret+=bad;
			}
		}
		if (suc<K) 
			printf("Case #%d: IMPOSSIBLE\n",kase);
		else
			printf("Case #%d: %d\n",kase,ret);
	}
	return 0;
}