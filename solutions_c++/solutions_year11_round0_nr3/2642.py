#include <cstdio>
#include <algorithm>

using namespace std;

int T, N;
int maxs;

int v[1100];

int main()
{
	scanf(" %d", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		maxs = 0;

		scanf(" %d", &N);
		int x = 0;
		for(int i = 0; i < N; ++i) {
			scanf(" %d", &v[i]);
			x ^= v[i];
		}

		if(x) {
			printf("Case #%d: NO\n", _42);
			continue;
		}

		sort(v, v+N);

		for(int i = N-1; i >= 1; --i) {
			int sean = 0, pat = 0;
			int sum = 0;
			for(int j = i; j < N; ++j) {
				sean ^= v[j];
				sum += v[j];
			}
			for(int j = 0; j < i; ++j) {
				pat ^= v[j];
			}

			if(sean == pat && sum > maxs) maxs = sum;
		}


		printf("Case #%d: %d\n", _42, maxs);
	}
	return 0;
}
