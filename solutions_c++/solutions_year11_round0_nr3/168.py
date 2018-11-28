#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
#define MAX 1010
const int BIG=0x3f3f3f3f;
int a[MAX];
int main()
{
	int cs,n,i,x,t,mx,sum;
	scanf("%d",&cs);
	for(int dd=1;dd<=cs;dd++)
	{
		scanf("%d",&n);
		for(sum=x=i=0,mx=BIG;i<n;i++)
		{
			scanf("%d",&t);
			x^=t;
			mx=min(mx,t);
			sum+=t;
		}
		if(x==0)
			printf("Case #%d: %d\n",dd,sum-mx);
		else
			printf("Case #%d: NO\n",dd);
	}
}