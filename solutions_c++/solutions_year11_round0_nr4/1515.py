#include <iostream>
using namespace std;
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int T,sum,temp,i;
	int cnt=0;
	scanf("%d",&T);
	while(T--)
	{
		cnt++;
		int n;
		scanf("%d",&n);
		int sum;
		sum=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&temp);
			sum+=!(i==temp);
		}
		printf("Case #%d: %d.000000\n",cnt,sum);
	}
}