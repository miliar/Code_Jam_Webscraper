#include <cstdio>

int values[30], input[30];
bool changeable[30];

int main() {
	int N;
	scanf("%d", &N);

	for(int c = 1; c <= N; ++c) {
		int m, v;
		scanf("%d %d", &m, &v);
		for(int i = 0; i < (m-1)/2; ++i) {
			int type, ch;
			scanf("%d %d", &type, &ch);
			input[i] = type;
			changeable[i] = ch;
		}
		for(int i = (m-1)/2; i < m; ++i) {
			scanf("%d", &input[i]);
			values[i] = input[i];
		}
		int mcount = -1;
		for(int mask = 0; mask < (1<<((m-1)/2))-1; ++mask) {
			bool ok = true;
			int count = 0;
			for(int i = 0, b = 1; b <= mask; ++i, b <<= 1) {
				if(mask & b) {
					++count;
					if(!changeable[i]) {
						ok = false;
						break;
					}
				}
			}
			if(!ok) continue;
			for(int i = (m-1)/2-1; i >= 0; --i) {
				int cur = input[i], li = (i+1)*2-1, ri = (i+1)*2;
				if(mask & (1<<i)) {
					cur = 1-cur;
				}
				if(cur == 0) {
					values[i] = values[li] || values[ri];
				} else {
					values[i] = values[li] && values[ri];
				}
			}
			if(values[0] == v) {
				if(mcount == -1 || mcount > count) {
					mcount = count;
				}
			}
		}
		if(mcount == -1) {
			printf("Case #%d: IMPOSSIBLE\n", c, mcount);
		} else {
			printf("Case #%d: %d\n", c, mcount);
		}
	}
}
