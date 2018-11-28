#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;
int main()
{
	int T,Ti;
	int n;
	int a[1000];
	int b[1000];

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
//

	scanf("%d",&T);
	Ti=0;
	while(T--)
	{
		Ti++;
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d",&a[i]);
		for(int i=0;i<n;i++) scanf("%d",&b[i]);
		sort(a,a+n,greater<int>());
		sort(b,b+n);

		__int64 sum=0;
		for(int i=0;i<n;i++) sum+=(__int64)a[i]*b[i];

		printf("Case #%d: %I64d\n",Ti,sum);

	}
}