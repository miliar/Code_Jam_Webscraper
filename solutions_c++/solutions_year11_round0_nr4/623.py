#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int expected_hits() {
	int N;
	cin >> N;
	int r = 0;
	for (int i = 1; i <= N; i++) {
		int c;
		cin >> c;
		if (c != i) r++;
	}
	return r;
}

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int r = expected_hits();
		printf("Case #%d: %d\n", i, r);
	}
	return 0;
}

