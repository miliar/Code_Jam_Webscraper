#include <stdio.h>
#include <limits.h>
#include <algorithm>

int main()
{
	int t;
	scanf("%d", &t);
	
	for (int k = 0; k < t; ++k) {
		int l, t, n, c;
		scanf("%d %d %d %d", &l, &t, &n, &c);
		
		int* distances = new int[n];
		int* as = new int[c];
		
		for (int i = 0; i < c; ++i)
			scanf("%d", &as[i]);
			
		for (int i = 0; i < n; ++i)
			distances[i] = as[i % c];
			
		int best = INT_MAX;
		if (l == 0) {
			best = 0;
			for (int i = 0; i < n; ++i)
				best += distances[i] * 2;
		} else if (l == 1) {
			for (int i = 0; i < n; ++i) {
				int result = 0;
				for (int j = 0; j < n; ++j) {
					if (i == j) {
						int left = std::min(distances[j] * 2, std::max(0, t - result));
						result += (left + distances[j] - left / 2);
					} else {
						result += distances[j] * 2;
					}
				}
				if (result < best)
					best = result;
			}
		} else if (l == 2) {
			for (int i = 0; i < n; ++i) {
				for (int k = 0; k < n; ++k) {
					int result = 0;
					for (int j = 0; j < n; ++j) {
						if (i == j || j == k) {
							int left = std::min(distances[j] * 2, std::max(0, t - result));
							result += (left + distances[j] - left / 2);
						} else {
							result += distances[j] * 2;
						}
					}
					if (result < best)
						best = result;
				}
			}
		}
		
		printf("Case #%d: %d\n", k + 1, best);
		
		delete [] as;
		delete [] distances;
	}
}

