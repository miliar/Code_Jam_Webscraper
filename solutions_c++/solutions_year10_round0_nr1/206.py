#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		int n, k;
		scanf("%d %d", &n, &k);
		int sum = 1<<n;
		printf("Case #%d: %s\n", t+1, k%sum == sum-1 ? "ON" : "OFF");
	}
	return 0;
}

