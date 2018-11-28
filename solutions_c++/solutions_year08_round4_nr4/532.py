#include <cstdio>
#include <cstring>
#define inf 100000000
#define oo 10005
bool mk[10];
int Case,Test;
int k;
char s[oo],t[oo];
int c[10];
int ans,len;

inline void check()
{
	for (int i=0;i<len/k;++i)
		for (int j=0;j<k;++j)
			t[i*k+c[j]]=s[i*k+j];
	
	int res=1;
	char b=t[0];
	for (int i=1;i<len;++i)
		if (b!=t[i])
		{
			res++;
			b=t[i];
		}
	ans<?=res;
}

inline void work(int u)
{
	if (u==k)
	{
		check();
		return;
	}
	
	for (int i=0;i<k;++i)
		if (!mk[i])
		{
			mk[i]=true;
			c[u]=i;
			work(u+1);
			mk[i]=false;
		}
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	
	for (scanf("%d",&Test);Test;Test--)
	{
		scanf("%d",&k);
		gets(s);
		gets(s);
		len=strlen(s);
		
		ans=inf;
		work(0);
		
		printf("Case #%d: %d\n",++Case,ans);
	}
	return 0;
}
