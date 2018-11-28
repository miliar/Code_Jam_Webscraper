#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main (void) {
	int testnum;
	scanf ("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++) {
		int n;
		scanf ("%d", &n);

		int o_time = 0, b_time = 0, o_x = 1, b_x = 1;
		int t = 0;

		for (int i = 0; i < n; i++) {
			char robot[ 10];
			int sw_number;
			scanf("%s %d", robot, &sw_number);
			if (robot[0] == 'O') {
				t = max(o_time + abs(o_x - sw_number) + 1, t + 1);
				o_time = t;
				o_x = sw_number;
			} else {
				t = max(b_time + abs(b_x - sw_number) + 1, t + 1);
				b_time = t;
				b_x = sw_number;
			}
		}
		printf ( "Case #%d: %d\n", testcase, t);
	}
	return 0;
}



