#include <cstdio>
#include <cstring>

using namespace std;

int a[1002];
int v[1002];

int main()
{
	int n;
	scanf("%d", &n);
	
	//precompute
	
	for (int i=1; i<=n; i++)
	{
		int m;
		scanf("%d", &m);
		int cnt = 0;
		for (int j=1; j<=m; j++)
		{
			scanf("%d", &a[j]);
			if (j != a[j]) cnt++;
		}
		if (cnt < 2) cnt = 0;
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}