#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 16;
bool broken[MAXN][MAXN];
int opt[MAXN*MAXN][3*1024];
int cx, cy, mask;

bool getbit(int s, int k) {
	return (s >> k) & 1;
}

void print_bit(int s) {
	for (int i = cy; i >=0 ; i--)
		printf("%d", (int)getbit(s,i));
}

void print_state(int i, int s) {
	printf("opt i=%d, s=", i);
	print_bit(s);
	printf(": %d\n", opt[i][s]);
}

void process() {
	memset(broken, 0, sizeof(broken));
	scanf("%d %d", &cx, &cy);
	for (int x = 0; x < cx; x++)
		for (int y = 0; y < cy; y++) {
			char ch;
			scanf(" %c", &ch);
			if (ch == 'x')
				broken[x][y] = true;
		}

	for (int x = 0; x <= max(cx-1,3); x++)
		for (int y = 0; y <= max(cy-1,3); y++)
			if (x >= cx || y >= cy)
				broken[x][y] = 1;
	cx = max(cx, 3);
	cy = max(cy, 3);

	memset(opt, 0, sizeof(opt));
	for (int s = 0; s < (1<<(cy+1)); s++) {
		int cnt = 0;
		bool bad = false;
		for (int i = 0; i < cy+1; i++) {
			int t = cy-i;
			int x = t/cy, y = t%cy;
			if (getbit(s,i) && broken[x][y]) bad = true;
		}
		if (bad) { opt[cy][s] = -10000; continue; }

		for (int i = 1; i < cy; i++)
			if (getbit(s,i) && getbit(s,i+1)) {
				bad = true;
				break;
			}
		if (bad) { opt[cy][s] = -10000; continue; }
		if (getbit(s,0) && getbit(s,cy-1)) { opt[cy][s] = -10000; continue; }

		for (int i = 0; i < cy+1; i++)
			if (getbit(s,i))
				cnt++;
		opt[cy][s] = cnt;
	}

	for (int i = cy+1; i < cx*cy; i++)
		for (int s = 0; s < (1<<(cy+1)); s++)
			opt[i][s] = -10000;

	mask = (1<<cy+1)-1;
	for (int i = cy; i < cx*cy; i++) {
		int x = i/cy, y = i%cy;
		for (int s = 0; s < (1<<(cy+1)); s++) {
			// print_state(i, s);

			int tx = (i+1)/cy, ty = (i+1)%cy;
			bool bad = broken[tx][ty];
			opt[i+1][(s<<1)&mask] = max(opt[i+1][(s<<1)&mask], opt[i][s]);

			if (ty == 0) {
				if (getbit(s,cy-2))
					bad = true;
			}
			else {
				if (getbit(s,cy) || getbit(s,0))
					bad = true;
				if (ty <= cy-2 && getbit(s,cy-2))
					bad = true;
			}
			// if (i == 7 && s == 4) printf("bad = %d\n", (int)bad);
			if (!bad)
				opt[i+1][((s<<1)+1)&mask] = max(opt[i+1][((s<<1)+1)&mask], opt[i][s]+1);
		}
	}

	int res = 0;
	for (int s = 0; s < (1<<(cy+1)); s++)
		res = max(res, opt[cx*cy-1][s]);
	printf("%d\n", res);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		process();
	}
}
