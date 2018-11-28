#include <iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int tt,T,ans,n,k;
	scanf("%d",&T);
	for (tt = 1 ;tt <= T ; tt++)
	{
		scanf("%d%d",&n,&k);
		if((1<<n)-1 == k%(1<<n)) ans=1;
		else ans=0;
		printf("Case #%d: %s\n",tt,ans?"ON":"OFF");
	}
	return 0;
}