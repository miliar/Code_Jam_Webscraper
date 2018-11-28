#include <cstdio>
#include <cstring>
#include <cstdlib>

int main()
{
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	
	int test=1,T;
	for (scanf("%d",&T);test<=T;++test)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int m=1;
		for (int i=0;i<n;++i)
			m=m*2;
		if (k%m==m-1) printf("Case #%d: ON\n",test);
		else printf("Case #%d: OFF\n",test);
	}
	return 0;
}
