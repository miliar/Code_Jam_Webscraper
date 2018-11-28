#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	int nTests;
	scanf("%d", &nTests);
	for (int testCase = 1; testCase <= nTests; testCase++) {
		char str[1000];
		scanf("%s", str);
		int N = strlen(str);
		vector<char> seq(str, str+N);
		if (!next_permutation(seq.begin(), seq.end())) {
			seq.insert(seq.begin(), '0');
			int j;
			for (j = 1; seq[j] == '0'; j++);
			swap(seq[0], seq[j]);
		}
		printf("Case %d: %s\n", testCase, (string(seq.begin(), seq.end())).c_str());
	}
	return 0;
}