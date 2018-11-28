#include <stdio.h>
#include <algorithm>
using namespace std;

int solve() {
	int N;
	scanf("%d", &N);
	int orange_pos = 1, orange_time = 0,
	 blue_pos = 1, blue_time = 0;
	int latest_time = 0;
	for (int i = 0; i < N; i++) {
		char name[2]; int pos;
		scanf("%s%d", name, &pos);
		if (name[0] == 'O') {
			// Orange
			latest_time = max(
			    latest_time + 1,
			    orange_time + abs(orange_pos - pos) + 1);
			orange_pos = pos;
			orange_time = latest_time;
		} else {
			// Blue
			latest_time = max(
			    latest_time + 1,
			    blue_time + abs(blue_pos - pos) + 1);
			blue_pos = pos;
			blue_time = latest_time;
		}
	}
	return latest_time;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}

