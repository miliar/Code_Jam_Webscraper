#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
using namespace std;
#define FOR(i, n) for (int i = 0; i < (int) (n); i++)

int ro[128], po[128], n;

int findNext(int robot, int curPos)
{
	for (int i = curPos; i < n; i++) if (ro[i] == robot) return i;
	return -1;
}

int solve(void)
{
	scanf("%d", &n);
	FOR(i, n) {
		char t[20];
		scanf("%s%d", t, &po[i]);
		ro[i] = (t[0] == 'O');
	}
	int x[2] = { 1, 1 };
	int c = 0;
	int script = 0;
	while (script < n) {
		c++;
		bool incScript = false;
		FOR(ri, 2) {
			if (ro[script] == ri && po[script] == x[ri]) {
				// push da button
				incScript = true;
			} else {
				int next = findNext(ri, script);
				if (next != -1 && po[next] < x[ri]) {
					x[ri]--;
				} else if (next != -1 && po[next] > x[ri]) {
					x[ri]++;
				}
			}
		}
		if (incScript) script++;
	}
	return c;
}

int main(void)
{
	int T;
	scanf("%d", &T);
	FOR(i, T) {
		int r = solve();
		printf("Case #%d: %d\n", i + 1, r);
	}
	return 0;
}
