#include<iostream>
using namespace std;
int p[31];
int main()
{
	int a,n,k;
	p[0]=1;
	for(a=1;a<=30;a++) p[a]=p[a-1]*2;
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
	scanf("%d%d",&n,&k);
	if( (k+1)%p[n] ) printf("Case #%d: OFF\n",_);
	else printf("Case #%d: ON\n",_);
}
	return 0;
}
