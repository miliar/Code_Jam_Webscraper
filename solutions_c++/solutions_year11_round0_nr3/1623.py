#include<stdio.h>
#include<vector>
#include<utility>
#include<stack>
using namespace std;

int main()
{
	int T, ks, i;
	int sum, min, xor, n, a;
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small-attempt0.out","w",stdout);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d",&n);
		scanf("%d",&a);
		sum=xor=min=a;

		for(i=2;i<=n;i++)
		{
			scanf("%d",&a);
			xor^=a;
			sum+=a;
			if(min>a) min=a;
		}

		printf("Case #%d: ",ks);
		if(xor) printf("NO\n");
		else printf("%d\n",sum-min);
	}

	return 0;
}