#include<cstdio>
#include<cstring>
#define maxn 128
#define maxL 128
int n,s,q;
char engine[maxn][maxL];
int query[maxn];
int mark[maxn];
int getID(char str[])
{
	for(int i=0;i<s;i++)
		if(strcmp(engine[i],str)==0)
			return i+1;
}
int InNeed()
{
	int cnt=0,i;
	for(i=0;i<maxn;i++)
		cnt+=mark[i];
	if(cnt==s-1)
		return 1;
	return 0;
}
int main()
{
	freopen("fa.in","r",stdin);
	freopen("f.out","w",stdout);

	scanf("%d\n",&n);
	for(int cs=1;cs<=n;cs++)
	{
		scanf("%d\n",&s);
		int i;
		for(i=0;i<s;i++)
			gets(engine[i]);
		scanf("%d\n",&q);
		for(i=0;i<q;i++)
		{
			char str[maxL];
			gets(str);
			query[i]=getID(str);
		}
		memset(mark,0,sizeof(mark));
        int ans=0;
		if(q==0)
		{
			printf("Case #%d: 0\n",cs);
			continue;
		}
		for(i=0;i<q;i++)
		{
			if(InNeed() && mark[query[i]]==0)
			{
				ans++;
				memset(mark,0,sizeof(mark));
			}
			mark[query[i]]=1;
		}
		ans--;
		for(i=0;i<maxn;i++)
			if(mark[i])
			{
				ans++;
				break;
			}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}