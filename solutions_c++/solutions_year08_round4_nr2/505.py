#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <assert.h>
using namespace std;
bool solve(int n,int m,int s,int& a1,int& b1,int& a2,int& b2)
{
	for(a1=0;a1<=n;a1++)
	for(a2=0;a2<=n;a2++)
	for(b1=0;b1<=m;b1++)
	for(b2=0;b2<=m;b2++)
		if(abs(a1*b2-a2*b1)==s)
			return true;
	return false;
}
int main()
{
	int t,ca=1;
	for(scanf("%d",&t);t--;)
	{
		int n,m,s,a1,a2,b1,b2;
		scanf("%d %d %d",&n,&m,&s);
		printf("Case #%d: ",ca++);
		if(!solve(n,m,s,a1,b1,a2,b2))
			puts("IMPOSSIBLE");
		else printf("0 0 %d %d %d %d\n",a1,b1,a2,b2);
	}
	return 0;
}
