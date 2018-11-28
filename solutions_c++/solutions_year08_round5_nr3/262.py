#include<cstdio>
#include<cstring>

const int maxn=12,maxs=200;

int n,m,T,s[maxs],r[maxn],c[maxs];
long long f[maxn][maxs],ans=0;

void dfs(int p,int last,int now,int cnt)
{
	if(p==n){s[++s[0]]=now,c[s[0]]=cnt;	return;}
	dfs(p+1,0,now*2,cnt);
	if(!last)dfs(p+1,1,now*2+1,cnt+1);
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int tn=1;tn<=T;tn++)
	{
		memset(s,0,sizeof(s));
		memset(c,0,sizeof(c));
		scanf("%d%d",&m,&n);
		memset(r,0,sizeof(r));
		char str[50];
		for(int i=m-1;i>=0;i--)
		{
			scanf("%s",str);
			for(int j=0;j<n;j++)
				if(str[j]=='x')r[i]|=(1<<j);
		}
		dfs(0,0,0,0);
		memset(f,0,sizeof(f));
		ans=0;
		for(int i=m-1;i>=0;i--)
			for(int j=1;j<=s[0];j++)
			{
				if((s[j]&r[i])!=0)continue;
				for(int k=1;k<=s[0];k++)
					if(((s[j]<<1)&s[k])==0 && ((s[j]>>1)&s[k])==0)
						f[i][j]>?=f[i+1][k]+c[j];
				ans>?=f[i][j];
			}
		printf("Case #%d: %I64d\n",tn,ans);
	}

	return 0;
}
