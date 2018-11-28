#include <cstdio>
#include <set>
#include <cstring>

int res;

struct S {
	int who;
	int to;
};

S mass[105];

int pos1;
int pos2;
int n;

int give(int who, int from) {
	for (int i = from;i < n;++i)
		if (mass[i].who == who)
			return i;
	return -1;
}

int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int t;
	
	char str[10];
	scanf("%d", &t);

	for (int i = 0;i < t;++i) {
		res = 0;
		scanf("%d", &n);
		for (int i = 0;i < n;++i) {
			scanf("%s%d", str, &mass[i].to);
			mass[i].who = strcmp(str, "O") == 0 ? 1 : 2;
		}
		pos1 = pos2 = 1;
		int cur = 0;

		while (cur < n) {
			int A = give(1, cur);
			int B = give(2, cur);
			
			if (A == cur) {
				if (pos1 == mass[cur].to) {
					cur++;
				} else {
					if (pos1 < mass[cur].to)
						pos1++;
					else
						pos1--;
				}
				if (B != -1) {
					if (pos2 > mass[B].to) pos2--;
					if (pos2 < mass[B].to) pos2++;
				}
				++res;
			}
			else {
				if (pos2 == mass[cur].to) {
					cur++;
				} else {
					if (pos2 < mass[cur].to)
						pos2++;
					else
						pos2--;
				}
				if (A != -1) {
					if (pos1 > mass[A].to) pos1--;
					if (pos1 < mass[A].to) pos1++;
				}
				++res;
			}
		}
		printf("Case #%d: %d\n", i + 1, res);
	}

	return 0;
}