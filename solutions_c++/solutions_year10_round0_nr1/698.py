#include <iostream>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;++test)
	{
		int k,n;
		scanf("%d%d",&n,&k);
		if ((k+1)%(1LL<<n)==0)
			printf("Case #%d: ON\n",test); else
			printf("Case #%d: OFF\n",test);
	}
	return 0;
}