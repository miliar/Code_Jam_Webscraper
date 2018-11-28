#include <cstdio>
#include <vector>

#define abs(x) ((x) < 0 ? (-(x)) : (x))

using namespace std;

vector < int > tasks1, tasks2;
vector < int > all;

int main() {
	int tests; scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		tasks1.clear(); tasks2.clear();
		all.clear();

		int n; scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char c; int x; scanf(" %c %d", &c, &x);
			if (c == 'O') {
				tasks1.push_back(x);
				all.push_back(1);
			}
			else {
				tasks2.push_back(x);
				all.push_back(2);
			}
		}

		int ans = 0, curr = 0, curr1 = 0, curr2 = 0, pos1 = 1, pos2 = 1;
		while (curr < n) {
			//printf("pos1 %d pos2 %d\n", pos1, pos2);
			
			bool pressed = false;
			if (all[curr] == 1 && pos1 == tasks1[curr1])
				pressed = true, curr1++;
			else if (curr1 < (int) tasks1.size() && pos1 != tasks1[curr1])
				pos1 += (tasks1[curr1] - pos1) / abs(tasks1[curr1] - pos1);
			
			if (all[curr] == 2 && pos2 == tasks2[curr2])
				pressed = true, curr2++;
			else if (curr2 < (int) tasks2.size() && pos2 != tasks2[curr2])
				pos2 += (tasks2[curr2] - pos2) / abs(tasks2[curr2] - pos2);

			if (pressed)
				curr++;
			ans++;
		}

		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}
