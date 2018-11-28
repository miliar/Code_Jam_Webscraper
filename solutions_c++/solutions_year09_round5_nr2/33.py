#include <cstdio>
#include <cstring>
#include <cstdlib>
#define base 10009
#define maxLen 35
#define maxn 25

char op[maxLen],s[55];
int cnt[maxn][30],cur[30],ans,n,K,Mul;

inline void Plus(int &a,int b)
{
	a+=b;
	if (a>=base) a-=base;
}

inline void calc()
{
	int sum=0,now=1;
	for (int i=0;op[i];++i)
	{
		if (op[i]=='+') Plus(sum,now),now=1;
		else now=(now*cur[op[i]-'a'])%base;
	}
	Plus(sum,now);
//	sum*=Mul;
//	sum%=base;
//	printf("%d\n",sum);
	Plus(ans,sum);
}

inline void dfs(int last)
{
	if (!last)
	{
		calc();
		return;
	}
	for (int step=0;step<n;++step)
	{
		for (int i=0;i<26;++i)
			cur[i]+=cnt[step][i];
		dfs(last-1);
		for (int i=0;i<26;++i)
			cur[i]-=cnt[step][i];
	}
/*	if (n-step>last) dfs(step+1,last);
	
	for (int i=0;i<26;++i)
		cur[i]+=cnt[step][i];
	dfs(step+1,last-1);
	for (int i=0;i<26;++i)
		cur[i]-=cnt[step][i];*/
}

int main()
{
	freopen("B_small.in","r",stdin);
	freopen("B_small.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%s%d%d",op,&K,&n);
		memset(cnt,0,sizeof(cnt));
		for (int i=0;i<n;++i)
		{
			scanf("%s",s);
			for (int j=0;s[j];++j)
				++cnt[i][s[j]-'a'];
		}
		printf("Case #%d:",test);
		memset(cur,0,sizeof(cur));
		for (int d=1;d<=K;++d)
		{
			Mul=1;
			for (int i=2;i<=d;++i)
				Mul=(Mul*i)%base;
			ans=0;
			dfs(d);
			printf(" %d",ans);
		}
		puts("");
	}
	
	return 0;
}
