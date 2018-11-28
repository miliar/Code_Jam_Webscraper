#include <iostream>
using namespace std;
int main()
{
	int T;
	freopen("D-large.in","r",stdin);
	freopen("bb.txt","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int n;
		double sum=0;
		int temp;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&temp);
			if(temp!=i)sum++;
		}
		printf("Case #%d: %.6lf\n",t,sum);
	}



}