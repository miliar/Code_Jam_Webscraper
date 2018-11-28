#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define n 10005
int N,T;
int a[n],b[n];
char buf[2];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int Te=1;Te<=T;++Te)
	{
		scanf("%d",&N);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		int pa=1,pb=1,ret=0;
		for (int i=0;i<N;++i)
		{
			scanf("%s%d",buf,&a[i]);
			if (buf[0]=='B')	b[i]=1;
		}
		for (int i=0;i<N;++i)
		if (b[i])
		{
			int time=abs(a[i]-pb)+1;
			ret+=time,pb=a[i];
			int na=0;
			for (int j=i+1;j<N;++j)
			if (!b[j])	{na=j;break;}
			if (!na)	continue;
			if (a[na]>=pa)	pa=min(a[na],pa+time);
			else	pa=max(a[na],pa-time);
		}
		else
		{
			int time=abs(a[i]-pa)+1;
			ret+=time,pa=a[i];
			int nb=0;
			for (int j=i+1;j<N;++j)
			if (b[j])	{nb=j;break;}
			if (!nb)	continue;
			if (a[nb]>=pb)	pb=min(a[nb],pb+time);
			else	pb=max(a[nb],pb-time);
		}
		printf("Case #%d: %d\n",Te,ret);
	}
	return 0;
}
