// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include "stdio.h"
#include "string.h"
#include "stdlib.h"

int n;

int x[1200],y[1200];

int cmp(const void *a,const void *b)
{
	int *aa=(int *)a, *bb=(int *)b;
	return *aa<*bb;
}

void solve()
{
	scanf("%d",&n);

	int i;

	for(i=1;i<=n;++i)
	{
		scanf("%d",&x[i]);
	}
	for(i=1;i<=n;++i)
	{
		scanf("%d",&y[i]);
	}

	qsort(x+1,n,sizeof(int),cmp);
	qsort(y+1,n,sizeof(int),cmp);
	__int64 ans=0,temp;

	for (i=1;i<=n;++i)
	{
		temp = x[i];
		ans=ans+temp*y[n+1-i];
	}

	printf("%I64d",ans);
}


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int T,i;

	scanf("%d",&T);

	for (i=1;i<=T;++i)
	{
		printf("Case #%d: ",i);
		solve();
		printf("\n");
	}

	return 0;
}

