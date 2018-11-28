#include <stdio.h>

int process() {
	int n;
	int oPos = 1, bPos = 1;
	int oExt = 0, bExt = 0;
	int res = 0;
	char rob;
	int pos;
	int step;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf(" %c %d", &rob, &pos);
		if (rob == 'O') {
			step = pos - oPos;
			if (step < 0) step = -step;
			if (step <= oExt) {
				bExt = 1;
				res++;
			} else {
				bExt += (step - oExt) + 1;
				res += (step - oExt) + 1;
			}
			oExt = 0;
			oPos = pos;
		} else {
			step = pos - bPos;
			if (step < 0) step = -step;
			if (step <= bExt) {
				oExt = 1;
				res++;
			} else {
				oExt += (step - bExt) + 1;
				res += (step - bExt) + 1;
			}
			bExt = 0;
			bPos = pos;
		}
	}
	return res;
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		int res = process();
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}
