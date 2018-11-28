#include<cstdio>
#include<cstring>
char str[10000];
char tmp[10000];
bool mark[100];
int a[100];
int r,len;
void dfs(int dep,int k)
{
	int sum,i;
	if(dep==k)
	{
		for(i=0;i<len;i++)
		tmp[i]=str[i-i%k+a[i%k]];
		tmp[len]='/0';
		sum=1;
		for(i=1;i<len;i++)
		if(tmp[i]==tmp[i-1])continue;
		else sum++;
		r<?=sum;
	}
	for(i=0;i<k;i++)
	{
		if(!mark[i])
		{
			mark[i]=1;
			a[dep]=i;
			dfs(dep+1,k);
			mark[i]=0;
		}
	}
}
		
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("dd.out","w",stdout);
	int t,cc,k,i;
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		r=0x7fffffff;
		scanf("%d%s",&k,str);
		len=strlen(str);
		for(i=0;i<k;i++)mark[i]=0;
		dfs(0,k);
		printf("Case #%d: %d\n",cc,r);
	}
	return 0;
}
