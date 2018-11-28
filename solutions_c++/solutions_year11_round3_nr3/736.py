#include <cstdio>
#include <cstring>

int N,L,H,T,A[10005];

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for (int Te=1;Te<=T;++Te)
	{
		scanf("%d%d%d",&N,&L,&H);
		memset(A,0,sizeof(A));
		for (int i=0;i<N;++i)
			scanf("%d",&A[i]);
		int ret=-1;
		printf("Case #%d: ",Te);
		for (int i=L;i<=H;++i)
		{
			bool mk=0;
			for (int j=0;j<N;++j)
			if (A[j]%i!=0 && i%A[j]!=0)
			{
				mk=1;break;
			}
			if (!mk)	{ret=i;break;}
		}
		if (ret<0)	puts("NO");
		else	printf("%d\n",ret);
	}
	return 0;
}
