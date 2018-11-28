#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,to[101],tb[101],co,cb,p,po,pb;
	char c;
	scanf("%d\n",&t);
	for(int ii=1;ii<=t;ii++)
	{
		for(int i=0;i<=100;i++)to[i]=tb[i]=0;
		co=cb=0;
		po=pb=1;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf(" %c %d",&c,&p);
			if(c=='O')
			{
				to[co+1]=max(to[co]+abs(p-po),tb[cb])+1;
				co++;
				po=p;
			}
			if(c=='B')
			{
				tb[cb+1]=max(to[co],tb[cb]+abs(p-pb))+1;
				cb++;
				pb=p;
			}
		}
		scanf("%c",&c);
		printf("Case #%d: %d\n",ii,max(to[co],tb[cb]));
	}
}
