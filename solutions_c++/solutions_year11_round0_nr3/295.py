#include <iostream>

using namespace std;
int candy[10000];
int main()
{
    int tt;
    scanf("%d",&tt);
    for (int tc=1;tc<=tt;tc++)
    {
    	int n,ans=0;
    	scanf("%d",&n);
    	for (int i=0;i<n;i++)
		{
			scanf("%d",&candy[i]);
			ans^=candy[i];
		}
		printf("Case #%d: ",tc);
		if (ans!=0) printf("NO\n");
		else
		{
			sort(candy,candy+n);
			int sum=0;
			for (int i=1;i<n;i++)
				sum+=candy[i];
			printf("%d\n",sum);
		}

    }
    return 0;
}
