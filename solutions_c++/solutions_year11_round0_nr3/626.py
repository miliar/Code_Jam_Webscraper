#include <cstdio>
#include <algorithm>

using namespace std;

int c[1100];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,ca=1;
	int n;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		int sum=0;
		int i;
		for(i=0;i<n;i++)
		{
			scanf("%d",&c[i]);
			sum^=c[i];
		}
		printf("Case #%d: ",ca++);
		if(sum!=0) printf("NO\n");
		else
		{
			sort(c,c+n);
			int total=0;
			for(i=1;i<n;i++)
				total+=c[i];
			printf("%d\n",total);
		}
	}
	return 0;
}