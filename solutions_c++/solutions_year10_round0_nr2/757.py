//#include "BigInt.h"
#include <algorithm>
using namespace std;
long gcd(long x,long y)
{
	//long r,tmp;
	//if(x<y)
	//{
	//	tmp=x;
	//	x=y;
	//	y=tmp;
	//}
	//if(y==0)return y;
	//r=x%y;
	//while(r>0)
	//{
	//	x=y;
	//	y=r;
	//	r=x%y;
	//}
	//return y;
	
	while(x!=y )
	{
		if(x>y)
			x-=y;
		else
			y-=x;
	}
	return x;
}
void solve(int nCase)
{
	int n;
	long events[1000];
	long dvalue[1000],a,b,t,y;
	int i,j;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&events[i]);
	}
	sort(events,events+n);
	for(i=0;i<n-1;i++)
	{
		dvalue[i]=events[i+1]-events[i];
	}
	dvalue[i]=events[n-1]-events[0];
	j=0;
	while(a=dvalue[j++],a==0);
	for(i=j;i<n;i++)
	{
		b=dvalue[i];
		if(b>0)
			a=gcd(a,b);
	}
	t=a;
	while(t<events[0])
	{
		t+=a;
	}
	y=t-events[0];
	printf("Case #%d: %ld\n",nCase,y);
}
int main()
{
	int i,nCase;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.in.out","w",stdout);
	scanf("%d",&nCase);
	for(i=0;i<nCase;i++)
	{
		solve(i+1);
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}