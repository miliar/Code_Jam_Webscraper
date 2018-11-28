#include <cstdio>
#include <algorithm>

using namespace std;
int a[20000];
int T,I,n;
int main()
{
	scanf("%d", &T);
	for (I=1;I<=T;++I)
	{
		scanf("%d",&n);
		int t=0;
		for (int i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			t = t xor a[i];
		}
		sort(a,a+n);
		int	ans=0;
		if (t==0) 
		{
			for (int i=1;i<n;++i)
				ans+=a[i];
			printf("Case #%d: %d\n", I,ans);
		}
		else
			printf("Case #%d: NO\n", I);
	}
	return 0;
}
	
