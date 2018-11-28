#include <cstdio>
#include <iostream>

using namespace std;

int Test, num[2], now[2], n, op[2][100], opi[2][100], pos[2];

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	
	scanf("%d", &Test);
	for (int kase = 1; kase <= Test; kase++) {
		num[0] = num[1] = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char c; int p;
			cin >> c; scanf("%d", &p);
			if (c == 'O')
				op[0][num[0]] = p, opi[0][num[0]++] = i;
			else
				op[1][num[1]] = p, opi[1][num[1]++] = i;
		}
		now[0] = now[1] = 0;
		pos[0] = pos[1] = 1;
		int usingTime = 0, turnsTo = 0;
		while (turnsTo < n) {
			usingTime++;
			bool flag = false;
			for (int i = 0; i < 2; i++) {
				if (now[i] == num[i]) continue;
				if (opi[i][now[i]] == turnsTo && pos[i] == op[i][now[i]]) {
					now[i]++; flag = true;
				} else
				if (pos[i] < op[i][now[i]]) {
					pos[i]++;
				} else
				if (pos[i] > op[i][now[i]]) {
					pos[i]--;
				}
			}
			if (flag) turnsTo++;
		}
		printf("Case #%d: %d\n", kase, usingTime);
	}
	
	return 0;
}
