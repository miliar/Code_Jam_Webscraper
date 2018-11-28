#include <stdio.h>

int main()
{
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int ans = 0;
		int but_o[100];
		int but_b[100];
		int but_r[100];
		int N;
		scanf("%d", &N);
		int but_o_n = 0;
		int but_b_n = 0;
		int but_n = 0;
		while (--N >= 0) {
			char r[2];
			int p;
			scanf("%s %d", r, &p);
			if (r[0] == 'O')
				but_o[but_o_n++] = p;
			else
				but_b[but_b_n++] = p;
			but_r[but_n++] = r[0];
		}
		int i = 0, j = 0;
		int pos_o = 1, pos_b= 1;
		while ((1)) {
			bool t1 = i < but_o_n;
			bool t2 = j < but_b_n;
			if (!t1 && !t2)
				break;

			int k = i + j;

			if (but_o_n) {
				if (pos_o < but_o[i]) {
					++pos_o;
				} else if (pos_o > but_o[i]) {
					--pos_o;
				} else if (pos_o == but_o[i] && but_r[k] == 'O') {
					++i;
				}
			}

			if (but_b_n) {
				if (pos_b < but_b[j]) {
					++pos_b;
				} else if (pos_b > but_b[j]) {
					--pos_b;
				} else if (pos_b == but_b[j] && but_r[k] == 'B') {
					++j;
				}
			}
			++ans;
		}
		printf("Case #%d: %d\n", Case, ans);
	}
	return 0;
}

