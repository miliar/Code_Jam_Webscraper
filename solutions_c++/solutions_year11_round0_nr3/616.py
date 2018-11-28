#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

int a[1050];
int main()
{
	int cases;
	scanf("%d",&cases);
	int n;
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%d",&n);
		int now=0,tot=0;
		for (int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			now ^= a[i];
			tot += a[i];
		}
		sort(a,a+n);
		printf("Case #%d: ",tcase);
		if (now!=0) printf("NO\n");
		else printf("%d\n",tot-a[0]);
	}
	return 0;
}
