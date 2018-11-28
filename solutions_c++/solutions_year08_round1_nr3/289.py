#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	int i,l,ncase,n,a,b,last,now;
	scanf("%d",&ncase);
	for(l=1;l<=ncase;l++)
	{
		scanf("%d",&n);
		a=3;b=1;
		for(i=2;i<=n;i++)
		{
			last=a*3+b*5;now=3*b+a;
			a=last%1000;b=now%1000;
		}
		printf("Case #%d: %03d\n",l,a*2%1000-1);
	}
	return 0;
}
