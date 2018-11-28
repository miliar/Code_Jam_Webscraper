#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

inline int abs(int x) { return x > 0 ? x : -x; }
inline int max(int a, int b) { return a > b ? a : b; }

int btns[101];
int role[101];

int solve() {
	int l;
	scanf("%d", &l);
	for (int i = 0; i < l; ++i) {
		char c;
		scanf(" %c%d", &c, btns + i);
		role[i] = (c == 'B');
	}

	int res = 0;
	int pos[] = {1, 1};
	int i = 0;
	while (i < l) {
		int j = i;
		int crole = role[i];
		int p = pos[crole];
		int a = 0, b = 0;
		while (j < l && role[j] == crole) {
			a += abs(btns[j] - p) + 1;
			p = btns[j];
			j++;
		}
		pos[crole] = p;
		if (j < l) {
			b = abs(btns[j] - pos[1-crole]);
			pos[1-crole] = btns[j];
		}
		if (a < b) {
			int k = j;
			while (k < l && role[k] != crole) k++;
			if (k < l) {
				if (b - a > abs(btns[k] - pos[crole]))
					pos[crole] = btns[k];
				else {
					if (btns[k] > pos[crole]) pos[crole] += b-a;
					else pos[crole] -= b-a;
				}
			}
		}
		res += max(a, b);
		i = j;
	}
	return res;
}

int main() {
	int cc;
	scanf("%d", &cc);
	for (int i = 1; i <= cc; ++i) {
		printf("Case #%d: %d\n", i, solve());
	}
}
