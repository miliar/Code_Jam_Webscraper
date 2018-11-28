#include <iostream>
#include <map>

using namespace std;

int stepx[4] = {-1, 0, 0, 1}; 
int stepy[4] = {0, -1, 1, 0}; 

int par[10001];
int wei[10001];
int A[101][101];
int B[101][101];

int H,W;

int FindSet(int x) {
	if (par[x] != x) {
		par[x] = FindSet(par[x]);
	}
	return par[x];
}

void UnionSet(int x, int y) {
	x = FindSet(x); 
	y = FindSet(y);
	if (x == y)
		return;
	if (x > y) {
		swap(x, y); 
	}
	par[y] = par[x];
}

void Input() {
	cin >> H >> W;
	for (int i = 0;i < H; ++i)
		for (int j = 0; j < W; ++j) {
			cin >> A[i][j];
			par[i * W + j] = i * W + j;
		}
}

bool CheckVal(int x, int y) {
	return (0 <= x && x < H && 0 <= y && y < W && A[x][y] != -1);
}
void Solve() {
	bool flag = true;
	while (flag) {
		flag = false;
		for (int i = 0; i < H; ++i)
			for (int j = 0; j < W; ++j) {
				if (A[i][j] == -1)
					continue;
				bool can_flow = false;
				int minatt = A[i][j];
				int dir = -1;
				for (int step = 0; step < 4; ++step) {
					int tx = i + stepx[step];	
					int ty = j + stepy[step];
					if (!CheckVal(tx, ty) || A[tx][ty] >= minatt)
						continue;
					can_flow = true;
					minatt = A[tx][ty];
					dir = step;
				}
				if (!can_flow)
					continue;
				flag = true;
				int tx = i + stepx[dir];	
				int ty = j + stepy[dir];
				B[i][j] = -1;
				UnionSet(i * W + j, tx * W + ty);
			}
		for (int i = 0; i < H; ++i)
			for (int j = 0; j < W; ++j)
				A[i][j] = B[i][j];
	}
	map<int, int> lex;
	int lex_count = 0;
	for (int i = 0; i < H * W; ++i) {
		int x = FindSet(i);
		if (lex.find(x) == lex.end()) {
			lex[x] = lex_count++;
		}
		wei[i] = lex[x];
	}
}

void Output(int ncase) {
	cout << "Case #" << ncase << ":" << endl;
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j)
			printf("%c ", wei[i * W + j] + 'a');
		cout << endl;
	}

}

int main() {
	// freopen("B-large.in","r",stdin);
	// freopen("B-large.out","w",stdout);
	int T;
	cin >> 	T;
	for (int ncase = 1; ncase <= T; ++ncase) {
		Input();
		Solve();
		Output(ncase);
	}
	return 0;
}