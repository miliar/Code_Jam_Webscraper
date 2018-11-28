#include <cstdio>

int main()
{
	int T,N,K;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
	{
		scanf("%d%d",&N,&K);
		int g=(K+1)&-(K+1);
		printf("Case #%d: ",i);
		puts((g>=1<<N)?"ON":"OFF");
	}
	return 0;
}
