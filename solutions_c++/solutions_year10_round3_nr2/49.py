#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int t;
	int i;
	long long j;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		int l, p, c;
		int tot = 0;
		scanf("%d %d %d", &l, &p, &c);
		for (j = l; j < p; j*=c)
		{
			tot++;
		}
		int ans = 0;
		for (; tot > 1; tot = (tot+1)/2)
		{
			ans++;
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
}