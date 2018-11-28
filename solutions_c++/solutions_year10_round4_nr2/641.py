#include <stdio.h>
#include <string.h>

int m[4100];
int i_c;
//int ms[1024][1024];

void fill(int v) {
	if (v >= i_c) m[v] --;
	else {
		fill (v * 2);
		fill (v * 2 + 1);
	}
}

int main(int argc, char const* argv[])
{
	int tc, p;

	scanf("%d", &tc);
	for (int ti = 0; ti < tc; ti++) {
		scanf("%d", &p);
		i_c = (1 << p);
		memset(m, 0, sizeof(m));
		m[0] = 1;
		for (int i = 0; i < i_c; i++) {
			scanf("%d", &m[i + i_c]);
			m[i + i_c] = p - m[i + i_c];
		}
		for (int l = 0; l < p; l++) {
			int j_c = 1 << (p - 1 - l);
			for (int j = 0; j < j_c; j++) {
				scanf("%*d"); // small: 1
			}
		}
		// scan
		int r = 0;
		bool b;
		do {
			b = false;
			for (int i = 0; i < i_c; i++) {
				if (m[i_c + i] > 0) {
					b = true;
					// elimate
					int v = i + i_c;
					for (; m[v / 2] == 0; v /= 2);
					m[v] = 1;
					fill(v);
					r++;
				}
			}
		} while(b);
		printf("Case #%d: %d\n", ti + 1, r);
	}
	return 0;
}
