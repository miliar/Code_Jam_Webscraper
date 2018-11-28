#include <cstdio>
#include <map>

using namespace std;

const int maxn = 100;
const int maxAlt = 10001;
const int shift = maxn * maxn + 1;
const int dire[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int casei, cases, cnt, H, W;
int tmpx, tmpy;
int board[maxn + 2][maxn + 2];
int label[maxn + 2][maxn + 2];
map<int, int> tag;

inline void init() {
	scanf("%d%d", &H, &W);
	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j) scanf("%d", &board[i][j]);
	for (int i = 0; i <= H + 1; ++i) {
		board[i][0] = maxAlt; board[i][W + 1] = maxAlt;
	}
	for (int i = 0; i <= W + 1; ++i) {
		board[0][i] = maxAlt; board[H + 1][i] = maxAlt;
	}
}

inline int flowDFS(int nowx, int nowy) {
	int newx = nowx, newy = nowy;
	for (int i = 0; i < 4; ++i) {
		tmpx = nowx + dire[i][0]; tmpy = nowy + dire[i][1];
		if (board[tmpx][tmpy] < board[newx][newy]) {
			newx = tmpx; newy = tmpy;
		}
	}
	if (newx != nowx || newy != nowy) label[nowx][nowy] = flowDFS(newx, newy);
	return label[nowx][nowy];
}

inline void process() {
	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j) label[i][j] = (i - 1) * W + j - 1 + shift;
		
	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j) if (board[i][j] != -1) flowDFS(i, j);
		
	tag.clear();
	cnt = 0;
	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j) {
			if (tag.find(label[i][j]) == tag.end()) tag[label[i][j]] = cnt++;
			label[i][j] = tag[label[i][j]];
		}
}

inline void print() {
	printf("Case #%d:\n", casei);
	for (int i = 1; i <= H; ++i) {
		for (int j = 1; j < W; ++j) printf("%c ", label[i][j] + 'a');
		printf("%c\n", label[i][W] + 'a');
	}
}

int main() {
	//freopen("Bin.txt", "r", stdin);
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}

	return 0;
}
