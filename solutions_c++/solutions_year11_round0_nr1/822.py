#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

struct node
{
	char col[5];
	int pos;
}a[105];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		int n;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
			scanf("%s%d",a[i].col,&a[i].pos);
		int or=1,bl=1,time=0,pre=0,to=0,tb=0;
		for (int i=1;i<=n;i++)
		{
			if (a[i].col[0]=='O')
			{
				time=max(time+1,to+abs(a[i].pos-or)+1);
				or=a[i].pos;
				to=time;
			}
			else
			{
				time=max(time+1,tb+abs(a[i].pos-bl)+1);
				bl=a[i].pos;
				tb=time;
			}
		}
		printf("%d\n",time);
	}
}