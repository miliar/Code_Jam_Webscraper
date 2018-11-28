#include <cstdio>
#include <cassert>

int c[1024];
int n;

int main(int argc, char const* argv[])
{
	int test_count;
	scanf("%d", &test_count);

	for (int test_id = 0; test_id < test_count; test_id++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &c[i]);
		}
		assert(n <= 15);
		int t = 1 << n;
		int result = -1;
		for (int i = 0; i < t; i++) {
			int patrick = 0, sean = 0, sean_sum = 0;
			for (int j = 0; j < n; j++) {
				if (i & (1 << j)) {
					patrick ^= c[j];
					sean_sum += c[j];
				} else {
					sean += c[j];
				}
			}
			if (sean == patrick && sean != 0 && sean_sum > result) {
				result = sean_sum;
			}
		}
		printf("Case #%d: ", test_id + 1);
		if (result >= 0) printf("%d\n", result); else printf("NO\n");
	}
	return 0;
}
