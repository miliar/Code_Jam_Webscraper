#include <cstdio>
#include <cstring>

const int maxn = 150;
const int maxm = 1200;
const int maxlen = 120;

int casei, cases, n, m, ans, cnt;
bool avai[maxn];
int num[maxm];
char st[maxlen];
char engine[maxn][maxlen], que[maxm][maxlen];

inline void init() {
	scanf("%d", &n);
	gets(st);
	for (int i = 0; i < n; ++i) gets(engine[i]);
	scanf("%d", &m);
	gets(st);
	for (int i = 0; i < m; ++i) gets(que[i]);
}

inline void process() {
	for (int i = 0; i < m; ++i)
		for (int j = 0; j < n; ++j) if (strcmp(que[i], engine[j]) == 0)	{
			num[i] = j;
			break;
		}

	ans = 0;
	cnt = 0;
	memset(avai, true, sizeof avai);
	for (int i = 0; i < m; ++i)
		if (avai[num[i]]) {
			avai[num[i]] = false;
			if (++cnt == n) {
				--i;
				++ans;
				cnt = 0;
				memset(avai, true, sizeof avai);
			}
		}
}

inline void print() {
	printf("Case #%d: %d\n", casei, ans);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);

//	freopen("in.txt", "r", stdin);
//	freopen("", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
