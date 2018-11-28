#include<iostream>
using namespace std;
int main()
{
	int a,n,i,sm,mn,t;
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
	scanf("%d",&n);
	t=0;
	sm=0;
	mn=0;
	for(a=0;a<n;a++)
	{
		scanf("%d",&i);
		t^=i;
		sm+=i;
		if( i<mn || a==0 ) mn=i;
	}
	if( t ) printf("Case #%d: NO\n",_);
	else printf("Case #%d: %d\n",_,sm-mn);
}
	return 0;
}
