#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,m,n,mm,k=1,i;
	__int64 l,p,c;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%I64d%I64d%I64d",&l,&p,&c);
		for(i=1;;i++)
		{
			l=l*c;
			if(l>=p)break;
		}
		n=i-1;
		mm=0;
		while(n>0)
		{
			n=n/2;
			mm++;
		}
		printf("Case #%d: %d\n",k++,mm);
	}
	return 0;
}