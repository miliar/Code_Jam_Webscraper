#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

const int MAXN = 128;

int n;
int a[MAXN];

int work(int nCase)
{	
	printf("Case #%d: ", nCase);

	int xum = 0, sum = 0, mn = 1 << 30;
	scanf("%d", &n);
	for (int i = 0; i < n; i ++)
	{
		scanf("%d", &a[i]);
		xum ^= a[i];	sum += a[i];
		mn = min(mn, a[i]);
	}
	if (xum != 0)  return printf("NO\n");
	printf("%d\n", sum - mn);

	return 0;
}


int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k ++)
		work(k);
//	fclose(stdin);
//	fclose(stdout);
	return 0;
}