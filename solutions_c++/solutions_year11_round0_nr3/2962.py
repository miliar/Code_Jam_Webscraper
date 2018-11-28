#include <stdio.h>
#include <algorithm>
using namespace std;
const int INF=100000001;
int main()
{
	freopen("c.in","r",stdin);
	freopen("my_c.out","w",stdout);
	int CASE;
	scanf("%d",&CASE);
	for(int cas=1;cas<=CASE;cas++)
	{
		int n;
		scanf("%d",&n);
		int nim_sum=0,sum=0,lin=INF;
		for(int i=0;i<n;i++)
		{
			int tmp;
			scanf("%d",&tmp);
			lin=min(lin,tmp);
			sum+=tmp;
			nim_sum^=tmp;
		}
		printf("Case #%d: ",cas);
		if(nim_sum==0)
			printf("%d\n",sum-lin);
		else 
			printf("NO\n");
	}
}
