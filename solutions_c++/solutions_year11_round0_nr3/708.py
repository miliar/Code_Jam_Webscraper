#include<iostream>
using namespace std;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int cases,n,V;
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		scanf("%d",&n);
		int sum = 0, haveans = 0, min = 1<<20;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&V);
			haveans = haveans^V;
			sum += V;
			if(V < min)min = V;
		}
		if(haveans != 0 )printf("Case #%d: NO\n",cas);
		else printf("Case #%d: %d\n",cas,sum-min);
	}
}
