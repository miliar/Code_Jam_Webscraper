#include <iostream>
using namespace std;
int sst[30][30];
int main()
{
	int T;
 	freopen("C-large.in","r",stdin);
 	freopen("CCCClarge.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int temp,n,tp,sum=0;

		scanf("%d",&n);
		scanf("%d",&tp);
		sum+=tp;
		int min=tp;
		for(int i=1;i<n;i++)
		{
			scanf("%d",&temp);
			tp=tp^temp;
			if(min>temp)min=temp;
			sum+=temp;
		}
		if(!tp)printf("Case #%d: %d\n",t,sum-min);
		else printf("Case #%d: NO\n",t);
	}
	return 0;
}
