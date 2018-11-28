#include "stdio.h"
#include "string.h"
#include "math.h"
#include <algorithm>
using namespace std;
#define M 1100000

bool notp[M];//素数判定
int pr[110000],pn,ans;//pr存放素数,pn当前素数个数。
void getprime()
{
	pn=0;
	memset(notp,0,sizeof(notp));
	for(int i=2;i<M;i++) 
	{
		if(!notp[i])
			pr[pn++]=i;
		for(int j=0;j<pn && pr[j]*i<M;j++) 
		{
			notp[pr[j]*i]=1;
			if(i%pr[j]==0)break;
		}
	}
	//pr[pn++]=M;
}

long long a[62];
char s[150];
bool ok;
int l;

void dfs(int p,long long v)
{
	if(ok)
		return;
	if(p==l)
	{
		long long x=sqrt((double)v);
		if(x*x==v)
		{
			printf("%s\n",s);
			ok=1;
		}
		return;
	}
	if(s[p]=='?')
	{
		for(int i=0;i<2;i++)
		{
			s[p]=i+'0';
			dfs(p+1,v+a[l-1-p]*i);
		}
		s[p]='?';
		return;
	}
	if(s[p]=='0')
		dfs(p+1,v);
	else
		dfs(p+1,v+a[l-1-p]);
}

int main()
{
	int i,j,k,t,tc=1;
	freopen("gcj/2011.6.11/D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	a[0]=1;
	for(i=1;i<62;i++)
		a[i]=a[i-1]*2;
	scanf("%d",&t);
	//getprime();
	while(t--)
	{
		printf("Case #%d: ", tc++);
		scanf("%s",s);
		ok=0;l=strlen(s);
		dfs(0,0);
	}
	return 0;
}

/*
2
6 7 2
1111111
1122271
1211521
1329131
1242121
1122211
3 3 7
123
234
345
*/

