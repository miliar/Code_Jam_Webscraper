#include <stdio.h>
#include <algorithm>
using namespace std;
int a[10000];
int main()
{
	int T;
	scanf("%d",&T);
	for(int _=1;_<=T;_++)
	{
		int n;
		scanf("%d",&n);
		int i;
		int t=0;
		int sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			t^=a[i];
			sum+=a[i];
		}
		sort(a,a+n);
		sum-=a[0];
		if(t==0)
			printf("Case #%d: %d\n",_,sum);
		else
			printf("Case #%d: NO\n",_);
	}
	return 0;
}