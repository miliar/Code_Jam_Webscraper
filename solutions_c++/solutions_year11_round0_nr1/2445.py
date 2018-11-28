#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int k = 0; k < n; ++k) {
		int m;
		scanf("%d ", &m);
		vector<int> b(m);
		vector<char> r(m);
		for (int i = 0; i < m; ++i) {
			scanf("%c %d ", &r[i], &b[i]);
		}
		scanf("\n");
		int time = 0, time_O = 0, time_B = 0, pos_O = 1, pos_B = 1;
		for (int i = 0; i < m; ++i) {
			if (r[i] == 'O') {
				time_O += abs(pos_O - b[i]) + 1;
				pos_O = b[i];
				if (time_O <= time) {
					time_O = time + 1;
				}
				time = max(time, time_O);
			} else {
				time_B += abs(pos_B - b[i]) + 1;
				pos_B = b[i];
				if (time_B <= time) {
					time_B = time + 1;
				}
				time = max(time, time_B);
			}
		}
		printf("Case #%d: %d\n", k + 1, time);
	}
	return 0;
}
