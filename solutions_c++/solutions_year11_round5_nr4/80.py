#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int T;
char s[200];

bool gao(long long n) {
	long long x = sqrt((double)n);
	for (; x * x < n; ++x);
	return x * x == n;
}

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%s", s);
		int len = strlen(s);
		int count = 0;
		vector <int> pos;
		for (int i = 0; i < len; ++i) {
			if (s[i] == '?') {
				pos.push_back(i);
				++count;
			}
		}
		int N = 1 << count;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < count; ++j) {
				s[pos[j]] = (i & 1 << j) ? '1' : '0';
			}
			long long cur = 0;
			for (int j = 0; j < len; ++j) {
				cur = (cur << 1) | (s[j] - '0');
			}
			if (gao(cur)) {
				break;
			}
		}
		printf("Case #%d: %s\n", caseNum, s);
	}
	return 0;
}
