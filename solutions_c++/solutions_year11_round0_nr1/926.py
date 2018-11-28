#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

const int MXN = 107;

int n;
int id[MXN], x[MXN];

int main()
{
	int T;
	scanf("%d", &T);
	for (int numCase = 1; numCase <= T; ++numCase) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			char op[3];
			scanf("%s%d", op, x + i);
			id[i] = (*op == 'O');
		}
		int u = 1, v = 1;
		int gu = 0, gv = 0;
		for (int j = 0; j < n; ++j)
			if (id[j] == 1) {
				gu = x[j];
				break;
			}
		for (int j = 0; j < n; ++j)
			if (id[j] == 0) {
				gv = x[j];
				break;
			}

		int ret = 0;
		for (int i = 0; i < n; ++i) {
			if (id[i] == 1) {
				int t = abs(gu - u) + 1;
				u = gu;
				if (t >= abs(gv - v)) v = gv;
				else {
					if (gv > v) v += t;
					if (gv < v) v -= t;
				}
				ret += t;
			} else {
				int t = abs(gv - v) + 1;
				v = gv;
				if (t >= abs(gu - u)) u = gu;
				else {
					if (gu > u) u += t;
					if (gu < u) u -= t;
				}
				ret += t;
			}
			for (int j = i + 1; j < n; ++j)
				if (id[j] == 1) {
					gu = x[j];
					break;
				}
			for (int j = i + 1; j < n; ++j)
				if (id[j] == 0) {
					gv = x[j];
					break;
				}
		}
		printf("Case #%d: %d\n", numCase, ret);
	}
}
