#include <iostream>
using namespace std;

const int maxn = 10000 + 10;
const int maxl = 10 + 3;

int tcase, n, m, cur;
char dic[maxn][maxl], seq[26 + 3];
int len[maxn], pos[maxn][26 + 3], ord[maxn], point[maxn];

bool comp1(const int &u, const int &v) {
	return len[u] < len[v];
}

bool comp2(const int &u, const int &v) {
	return pos[u][cur] < pos[v][cur];
}

void init() {
	scanf("%d%d\n", &n, &m);
	memset(pos, 0, sizeof(pos));
	for (int i = 0; i < n; ++i) {
		cin >> dic[i];
		len[i] = strlen(dic[i]);
		for (char c = 'a'; c <= 'z'; ++c)
			for (int j = 0; j < len[i]; ++j)
				if (dic[i][j] == c) pos[i][c - 'a'] ^= 1 << j;
		ord[i] = i;
	}
}

void work(int l, int r, int c) {
	cur = seq[c] - 'a';
	int cur2 = cur;
	sort(ord + l, ord + r, comp2);
	if (pos[ord[r - 1]][cur2]) {
		//cout << "add "<< char('a' + cur2) << " :" <<endl;
		for (int k = l; pos[ord[k]][cur2] == 0; ++k) {
			++point[ord[k]];
			//cout << dic[ord[k]] << endl;
		}
	}
	if (c == 25) return;
	for (int i = l, j = i + 1; i < r; i = j++) {
		while (j < r && pos[ord[j]][cur2] == pos[ord[i]][cur2]) ++j;
		work(i, j, c + 1);
	}
}

void solve() {
	cin >> seq;
	memset(point, 0, sizeof(point));
	sort(ord, ord + n, comp1);
	for (int i = 0, j = 1; i < n; i = j++) {
		//cout << "len = "<< len[ord[i]]<<"---------------\n";
		while (j < n && len[ord[j]] == len[ord[i]]) ++j;
		work(i, j, 0);
	}
}

void print() {
	int maxp = point[0], rank = 0;
	for (int i = 1; i < n; ++i)
		if (point[i] > maxp)
			maxp = point[i], rank = i;
	printf(" %s", dic[rank]);
//	for (int i = 0; i < n; ++i)
//		cout << point[i];
}	

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcase);
	for (int k = 1; k <= tcase; ++k) {
		init();
		printf("Case #%d:", k);
		for (int i = 0; i < m; ++i) {
			solve();
			print();
		}
		printf("\n");
	}
	return 0;
}
