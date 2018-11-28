#include <cstdio>	
#include <cstdlib>

int main(int argc, char const* argv[])
{
	int case_no = 1, case_left;
	scanf("%d", &case_left);
	while (case_left--) {
		int n, p[128];
		char r[128];
		scanf("%d", &n);

		int robot_positions[2] = { 1, 1 };
		int robot_times[2] = { 0, 0 };
		int time = 0;

		for (int i = 0; i < n; i++) {
			scanf(" %c %d", r + i, p + i);
			int id = (r[i] == 'B');
			// move that robot takes time
			robot_times[id] += abs(robot_positions[id] - p[i]);
			robot_positions[id] = p[i];
			// wait another robot ?
			if (i && r[i] != r[i-1] && robot_times[id] < robot_times[!id]) {
				robot_times[id] = robot_times[!id];
			}
			// push button
			time = ++robot_times[id];
		}
		printf("Case #%d: %d\n", case_no++, time);
	}
	return 0;
}
