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
int main()
{
	int cs,n,i,ans,t;
	scanf("%d",&cs);
	for(int dd=1;dd<=cs;dd++)
	{
		scanf("%d",&n);
		for(ans=0,i=1;i<=n;i++)
		{
			scanf("%d",&t);
			if(t!=i)
				ans++;
		}
		printf("Case #%d: %.6f\n",dd,(double)ans);
	}
	return 0;
}