#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	const int MAX_N = 800;
	static int v1[MAX_N], v2[MAX_N+2];
	int T, n;
	long long z;
	scanf("%d", &T);
	for(int k = 1; k <= T; ++k) {
		//fprintf(stderr, " k = %d\n", k);
		scanf("%d", &n);
	//	fprintf(stderr, " n = %d\n", n);
		for(int i = 0; i < n; ++i)
			scanf("%d", v1 + i);
		sort(v1, v1 + n);
		
		for(int i = 0; i < n; ++i)
			scanf("%d", v2 + i);
		sort(v2, v2 + n, greater<int>());
		
		z = 0;
		for(int i = 0; i < n; ++i)
			z += v1[i] * v2[i];

		printf("Case #%d: %lld\n", k, z);

	}
	return 0;
}

