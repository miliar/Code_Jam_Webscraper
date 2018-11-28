#include "stdio.h"
#include "string.h"
#include "assert.h"

int s,q;
char buf[210];
char name[110][210];

int x[1010];
int f[1010];

int solve()
{
	char xx;
	int i,j;
	int ans;

	scanf("%d",&s);
	scanf("%c",&xx);//skip CR
	assert(s<=100);	
	

	for (i=1;i<=s; ++i)
	{
		gets(name[i]);		
		//printf("%s\n",name[i]);
	}

	scanf("%d",&q);
	scanf("%c",&xx);//skip CR
	

	for (i=1;i<=q;++i)
	{
		gets(buf);		
		//printf("%s\n",buf);

		for( j=1;j<=s;++j)if(strcmp(buf, name[j])==0)break;
		if (j<=s)
		{
			x[i] = j;
		}
		else
		{
			assert(false);
		}
	}
	

	f[0]=0;
	for (i=1;i<=q;++i)
	{
		for (j=i-1;j>=1;--j)if(x[i]==x[j])break;

		if (j==0) f[i] = 1;
		else f[i] = 100000;		

		for (j++; j<i; ++j) if( f[j]+1 < f[i]) f[i]=f[j]+1;	
	}

	//printf("%d %d %d %d %d %d\n", f[1], f[2], f[3], f[4], f[5], f[6]);

	ans = 100000;

	for (i=1;i<=s;++i)
	{
		for (j=q;j>=1;--j)
		{
			if(x[j]==i)break;
			if (f[j]<ans) ans =f[j];
		}
		if (j==0) ans = 0;
	}
	return ans;
}

int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);

	int n;
	int i;

	scanf("%d",&n);

	for (i=1;i<=n;++i)
	{		
		printf("Case #%d: %d\n",i,solve());
	}

	return 0;
}