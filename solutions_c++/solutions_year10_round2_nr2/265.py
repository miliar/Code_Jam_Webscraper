#include <cstdio>
int X[5005],V[5005];
int N,K,B,T;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int Te=1;Te<=Test;++Te)
	{
		scanf("%d%d%d%d",&N,&K,&B,&T);
		for (int i=1;i<=N;++i)
			scanf("%d",&X[i]);
		for (int i=1;i<=N;++i)
			scanf("%d",&V[i]);
		int j=0,k=0,Ans=0;
		for (int i=N;i&&j<K;--i)
		if (X[i]+T*(long long)V[i]<B)	++k;
		else	++j,Ans+=k;
		if (j==K)	printf("Case #%d: %d\n",Te,Ans);
		else	printf("Case #%d: IMPOSSIBLE\n",Te);
	}
	return 0;
}
