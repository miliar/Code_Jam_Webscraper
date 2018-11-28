#include <cstdio>

const int MAX_N = 110;

struct node
{
	char ch;
	int pos;
} a[MAX_N];

int o[MAX_N], b[MAX_N];
int no, nb, cases, n, po, pb, cnt, nowo, nowb, x;
char buf[10];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		scanf("%d", &n);
		no = nb = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%s%d", buf, &x);
			if (buf[0] == 'O') {
				o[no++] = x;
			} else {
				b[nb++] = x;
			}
			a[i].ch = buf[0];
			a[i].pos = x;
		}
		po = pb = 1;
		nowo = nowb = cnt = 0;
		for (int i = 0; i < n; ++i) {
			while (1) {
				if (nowo < no && a[i].ch == 'O' && po == o[nowo]) {
					if (pb != b[nowb]) {
						if (pb < b[nowb]) ++pb;
						else --pb;
					}
					++cnt;
					++nowo;
					break;
				}
				if (nowb < nb && a[i].ch == 'B' && pb == b[nowb]) {
					if (po != o[nowo]) {
						if (po < o[nowo]) ++po;
						else --po;
					}
					++cnt;
					++nowb;
					break;
				}
				if (nowo < no && po != o[nowo]) {
					if (po < o[nowo]) ++po;
					else --po;
				}
				if (nowb < nb && pb != b[nowb]) {
					if (pb < b[nowb]) ++pb;
					else --pb;
				}
				++cnt;
			}
		}
		printf("Case #%d: %d\n", cc, cnt);
	}
	return 0;
}
