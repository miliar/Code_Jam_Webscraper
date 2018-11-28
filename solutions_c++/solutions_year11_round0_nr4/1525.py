#include <cstdio>

using namespace std;

int main() {
	int n;
	scanf("%d\n",&n);
	
	for (int i = 1; i <= n; i++)
	{
		int k;
		scanf("%d",&k);
		int ans = 0;
		for (int q = 1; q <= k; q++)
		{
			int a;
			scanf("%d",&a);
			if (q != a)
				ans++;
		}
		printf("Case #%d: %lf\n",i,(double)ans);
	}
	return 0;
}
