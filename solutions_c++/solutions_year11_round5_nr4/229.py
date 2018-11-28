#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;
bool find;
int a[200],n,test;
char s[200];

bool Check(long long x)
{
	long long l=0,r=(long long)sqrt(x)+2;
	for (;l+1<r;)
	{
		long long mid=(l+r)>>1;
		if (mid*mid<=x) l=mid; else r=mid;
	}
	return l*l==x;
}

void Dfs(int i,long long x)
{
	if (find) return;
	if (i==n)
	{
		if (Check(x)) find=1;
		return;
	}
	if (s[i+1]=='?')
	{
		a[i+1]=0;
		Dfs(i+1,x<<1);
		if (find) return;
		a[i+1]=1;
		Dfs(i+1,(x<<1)+1);
	}	else
	Dfs(i+1,(x<<1)+s[i+1]-'0');
}

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		printf("Case #%d: ",kase);
		scanf("%s",s+1);
		n=strlen(s+1);
		find=0;
		Dfs(0,0);
		for (int i=1;i<=n;i++)
		if (s[i]=='?') printf("%d",a[i]); else printf("%c",s[i]);
		printf("\n");
	}
	
	return 0;
}
