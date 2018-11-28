#include <cstdio>
#include <cstdlib>

#include <iostream>

using namespace std;

int task() {
	int n, where, r = 0, orange_time = 0, blue_time = 0, orange_pos = 1, blue_pos = 1;
	char who;
	
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf(" %c %d", &who, &where);
		if (who == 'O') {
			orange_time = min(orange_time - abs(orange_pos - where), 0);
			orange_pos = where;
			blue_time += -orange_time + 1;
			r += -orange_time + 1;
			orange_time = 0;
		} else {
			blue_time = min(blue_time - abs(blue_pos - where), 0);
			blue_pos = where;
			orange_time += -blue_time + 1;
			r += -blue_time + 1;
			blue_time = 0;
		}
	}
	
	return r;
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: %d\n", i, task());
	}
}

