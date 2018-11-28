#include<iostream>
using namespace std;
int r[10]={100,50,25,20,10,5,4,2,1};
int main()
{
	long long n;
	int a,x,y;
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
	scanf("%I64d%d%d",&n,&x,&y);
	if( y==0 ){ if( x==0 ) printf("Case #%d: Possible\n",_); else printf("Case #%d: Broken\n",_); continue; }
	if( y==100 ){ if( x==100 ) printf("Case #%d: Possible\n",_); else printf("Case #%d: Broken\n",_); continue; }
	if( x==0 || x==100 ){ printf("Case #%d: Possible\n",_); continue; }
	for(a=0;a<10;a++) if( x%r[a]==0 ) break;
	if( 100/r[a]<=n ) printf("Case #%d: Possible\n",_);
	else printf("Case #%d: Broken\n",_);
}
	return 0;
}
