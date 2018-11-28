#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int r;
int k;
int n;
int input[1000];
int next[1000];
int value[1000];

long long f() {
	int left = k;
	bool simple = true;
	for (int i = 0; i < n; i++) {
		left -= input[i];
		if (left < 0) {
			simple = false;
			break;
		}
	}
	if (simple) {
		return ((long long) k - left) * r;
	}
	// complex one
	for (int groupId = 0; groupId < n; groupId++) {
		int currentId = groupId;
		int currentValue = 0;
		int seatLeft = k;
		while (seatLeft >= input[currentId]) {
			seatLeft -= input[currentId];
			currentValue += input[currentId];
			currentId = (currentId + 1) % n;
		}
		next[groupId] = currentId;
		value[groupId] = currentValue;
	}

	long long result = 0;
	int current = 0;
	for (int i = 0; i < r; i++) {
		result += value[current];
		current = next[current];
	}
	return result;
}

int main () {
	freopen("E:/C-large.in","r",stdin);
	freopen("E:/C_out.txt","w",stdout);

	int testNum = 0;
	scanf("%d", &testNum);
	for (int testIndex = 1; testIndex <= testNum; testIndex++) {
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &input[i]);
		}
		long long result = f();
		printf("Case #%d: %I64d\n", testIndex, result);
	}
	fflush(stdout);
	return 0;
}