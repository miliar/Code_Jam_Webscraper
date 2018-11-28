#include <stdio.h>
#include <algorithm>
#define M 1002

int a[M];

int main()
{
	int t,T=0,i,j,n;

	freopen("C-small-attempt0.in","r",stdin);
	//freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		scanf("%d",&n);
		j=0;
		for(i=1;i<=n;++i) scanf("%d",&a[i]), j^=a[i];
		printf("Case #%d: ",++T);
		if(j)
			printf("NO\n");
		else
		{
			std::sort(a+1,a+n+1);
			j=0;
			for(i=2;i<=n;++i) j+=a[i];
			printf("%d\n",j);
		}
	}
	return 0;
}
