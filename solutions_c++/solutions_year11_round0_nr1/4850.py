#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int T, N;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &N);
		int ox = 1, bx = 1;
		int ot = 0, bt = 0;
		int res;
		for (int n = 1; n <= N; n++) {
			int x;
			char c[2];
			scanf("%s %d", c, &x);
			if (c[0] == 'O') {
				int temp = x - ox;
				if (temp < 0) temp *= -1;
				if (bt >= ot) {
					if (temp <= bt - ot) ot = bt + 1;
					else ot = temp + ot + 1;
				}else {
					ot += temp + 1;
				}
				ox = x;
				res = ot;
			}else {
				int temp = x - bx;
				if (temp < 0 ) temp *= -1;
				if (ot >= bt) {
					if (temp <= ot - bt) bt = ot + 1;
					else bt = temp + bt + 1;
				}else bt += temp + 1;
				bx = x;
				res = bt;
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
