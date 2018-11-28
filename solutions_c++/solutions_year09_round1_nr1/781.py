#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 11
int hash[100000];
int OK(int a, int b)
{
	int bbb[50];
	int t=a, tmp, ans;
	ans=0;
	memset(hash,0,sizeof(hash));
	while(hash[t]==0)
	{
		if(t==1) return 1;
		hash[t]=1;
		while(t)
		{
			tmp=t%b;
			ans+=tmp*tmp;
			t/=b;
		}
		t=ans;
		ans=0;
	}
	return 0;
}
void solve()
{
	int a[N], len, i, top=0, j, flag;
	char tmp;
	while(1)
	{
		scanf("%d",&a[top++]);
		tmp=getchar();
		if(tmp=='\n') break;
	}
	for(i=2;;i++)
	{
		flag=1;
		for(j=0;j<top;j++)
			if(OK(i,a[j])==0)
			{
				flag=0;
				break;
			}
		if(flag)
		{
			printf("%d\n",i);
			break;
		}
	}
}
int main()
{
//	freopen("asmall.txt","r",stdin);
//	freopen("asmall22222.out","w",stdout);
	int i, t;
	scanf("%d",&t);
	getchar();
	for(i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}

