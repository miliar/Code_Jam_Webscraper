#include<cstdio>
#include<algorithm>

using namespace std;

int cases;
int n,x;

int main()
{
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t)
	{
		scanf("%d",&n);
		int sum=0,p=0,xr=0;
		while(n--)
		{
			scanf("%d",&x);
			sum+=x;
			if(!p||x<p) p=x;
			xr^=x;
		}
		printf("Case #%d: ",t);
		if(xr) puts("NO"); else printf("%d\n",sum-p);
	}
	return 0;
}
