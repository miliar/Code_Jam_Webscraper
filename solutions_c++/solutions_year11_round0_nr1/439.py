#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		int n, pos[2] = {1, 1}, times[2] = {0, 0};
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char op[2];
			int newpos;
			scanf("%s%d", op, &newpos);
			times[op[0] == 'O'] += abs(newpos - pos[op[0] == 'O']) + 1;
			times[op[0] == 'O'] = max(times[op[0] == 'O'], times[op[0] != 'O'] + 1);
			pos[op[0] == 'O'] = newpos;
		}
		printf("Case #%d: %d\n", oo + 1, max(times[0], times[1]));
	}
}
