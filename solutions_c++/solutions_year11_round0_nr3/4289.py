#include<cstdio>
#include<climits>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int index=0;
	while (t--)
	{
		index=index+1;
		int n;
		scanf("%d",&n);
		int ans=0;
		int min=INT_MAX;
		int st=0;
		while (n--)
		{
			int x;
			scanf("%d",&x);
			st=st+x;
			if (x<min)
				min=x;
			ans=ans^x;
		}
		if (ans!=0)
			printf("Case #%d: NO\n",index);
		else
			printf("Case #%d: %d\n",index,st-min);
	}
}
