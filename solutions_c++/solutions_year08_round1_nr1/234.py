#include<cstdio>
#include<algorithm>
using namespace std;
int n;
long long a[1000],b[1000];
long long ans;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf("%d",&cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d",&n);
		for (int i = 0; i < n; ++i)
			scanf("%I64d", a + i);
		for (int i = 0; i < n; ++i)
			scanf("%I64d", b + i);
		sort(a , a + n);
		sort(b , b + n);
		reverse(b , b + n);
		ans = 0;
		for (int i = 0 ; i < n; ++i)
			ans += a[i] * b[i];
		printf("Case #%d: %I64d\n",ca,ans);
	}
}
