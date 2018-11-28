#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[]) {
	if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}
	int numTestCases;
	scanf("%d", &numTestCases);
	for (int testCase = 1; testCase <= numTestCases; testCase++) {
		int n;
		scanf("%d", &n);
		vector<int> lastOne(n, 0);
		for (int i = 0; i < n; i++) {
			char str[5000];
			scanf("%s", str);
			for (int j = 0; j < n; j++) {
				if (str[j] == '1') {
					lastOne[i] = j;
				}
			}
		}
		int res = 0;
		for (int i = 0; i < n; i++) {
			int j;
			for (j = i; lastOne[j] > i; j++) {}
			for (; j != i; j--) {
				res++;
				swap(lastOne[j], lastOne[j-1]);
			}
		}
		printf("Case #%d: %d\n", testCase, res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
