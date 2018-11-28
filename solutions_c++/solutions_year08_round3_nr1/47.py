#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a,const void *b)
{
	return *(int *)b - *(int *)a;
}

int main()
{
	__int64 ans;
	int p,k,l,i;
	int asd,cas;
	int freq[1002];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d %d %d",&p,&k,&l);
		for(i=0;i<l;i++)
			scanf("%d",&freq[i]);
		qsort((void *)freq,l,sizeof(freq[0]),cmp);
		ans=0;
		for(i=0;i<l;i++)
			ans += (freq[i] * (i/k+1));
		printf("Case #%d: ",asd+1);
		printf("%I64d\n",ans);
	}
	return 0;
}
