#include<iostream>
using namespace std;
int cas,test=1,list[10],flag[10],k,len,minm;
char s[2000],temp[2000];
void solve()
{
	int i,j,ans,l=strlen(s),t=0 ;
	for(i=0;i<l;)
	{
		for(j=0;j<len;j++)
			temp[i++]=s[list[j]+t-1];
		t+=k;
	}
	for(i=0,ans=0;i<l;j++,i=j,ans++)
	{
		j=i;
		while(j+1<l&&temp[j]==temp[j+1]) j++;
	}
	if(minm>ans)
	minm=ans;
}
void dfs()
{
	int i;
	if(len==k)
	{
		solve();
		return ;
	}
	for(i=1;i<=k;i++)
	{
		if(flag[i]) continue ;
		flag[i]=1;
		list[len++]=i;
		dfs();
		len--;
		flag[i]=0;
	}
}
int main()
{
	freopen("D-small-attempt4.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&cas);
	while(cas--)
	{
		scanf("%d %s",&k,s);
		memset(flag,0,sizeof(flag));
		len=0,minm=1000000000;
		dfs();
		printf("Case #%d: %d\n",test++,minm);
	}
	return 0;
}