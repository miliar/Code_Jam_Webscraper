#include <iostream>
#include <deque>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

/**
 * NMAX max nodes
 * w[][] weights
 * c[][] is filled by maxflow()
 * src, dest: source, destination for maxflow
 * num: number of used nodes (0 <= src, dest < num)
 * return: total maximum flow from src to dest
 */

#define NMAX 100

int w[NMAX][NMAX];
int c[NMAX][NMAX];

int maxflow(int src, int dest, int num) {
	int i, j;
	int a, b;
	for (i=0;i<num;i++) for (j=0;j<num;j++) c[i][j] = 0;
	int done = 0;
	while (!done) {
		done = 1;
		deque <int> x(1, src);
		vector <int> used(num, 0);
		used[src] = 1;
		vector <int> last(num, 0);
		while (x.size() > 0) {
			a = x.front();
			x.pop_front();
			for (j = 0; j < num; j++) if (!used[j]) {
				if (w[a][j] - c[a][j] > 0) {
					x.push_back(j);
					used[j] = 1;
					last[j] = a;
				}
			}
			if (used[dest]) break;
		}
		if (used[dest]) {
			done = 0;
			a = last[dest];
			int cmin = w[a][dest] - c[a][dest];
			while (a != src) {
				b = last[a];
				j = w[b][a] - c[b][a];
				if (j < cmin) cmin = j;
				a = b;
			}
			a = dest;
			while (a != src) {
				b = last[a];
				c[b][a] += cmin;
				c[a][b] = - c[b][a];
				a = b;
			}
		}
	}
	int res = 0;
	for (i = 0; i < num; i++) res += c[src][i];
	return res;
}

int w2[100][100];

// w2[i][j] = 1/0 going from i to j allowed/not allowed. 0 <= i < num1, 0 <= j < num2
int bipartiteMatching(int num1, int num2) {
	int i, j;
	int a, b;
	int num = num1 + num2 + 2;
	int src = 0;
	int dest = num1 + num2 + 1;
	for (i = 0; i < num; i++) for (j = 0; j < num; j++) w[i][j] = 0;
	for (i = 0; i < num; i++) for (j = 0; j < num; j++) c[i][j] = 0;
	for (i = 1; i <= num1; i++) w[0][i] = 1;
	for (i = 0; i < num1; i++) for (j = 0; j < num2; j++) if (w2[i][j]) {
		w[i + 1][j + num1 + 1] = 1;
	}
	for (i = num1 + 1; i <= num1 + num2; i++) w[i][dest] = 1;
	int done = 0;
	// while (!done) { }
	for (int start = 1; start <= num1; start++) {
		done = 1;
		if (w[0][start] == 0) continue;
		deque <int> x(1, start);
		vector <int> used(num, 0);
		used[src] = 1;
		used[start] = 1;
		vector <int> last(num, 0);
		last[start] = src;
		while (x.size() > 0) {
			a = x.front();
			x.pop_front();
			for (j = 0; j < num; j++) if (!used[j]) {
				if (w[a][j] - c[a][j] > 0) {
					x.push_back(j);
					used[j] = 1;
					last[j] = a;
				}
			}
			if (used[dest]) break;
		}
		if (used[dest]) {
			done = 0;
			a = last[dest];
			int cmin = w[a][dest] - c[a][dest];
			while (a != src) {
				b = last[a];
				j = w[b][a] - c[b][a];
				if (j < cmin) cmin = j;
				a = b;
			}
			a = dest;
			while (a != src) {
				b = last[a];
				c[b][a] += cmin;
				c[a][b] = - c[b][a];
				a = b;
			}
		}
	}
	int res = 0;
	for (i = 0; i < num; i++) res += c[src][i];
	return res;
}


int doit() {
	int dx[] = {-1, -1, 1, 1};
	int dy[] = {-1, 0, -1, 0};
	int M;
	int N;
	cin >> M >> N;
	vector <string> x;
	for (int i = 0; i < M; i++) {
		string s;
		cin >> s;
		x.push_back(s);
	}
	int num1 = 0;
	int num2 = 0;
	int pos[100][100];
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (x[i][j] == 'x') continue;
			if (j % 2 == 0) {
				pos[i][j] = num1;
				num1++;
			} else {
				pos[i][j] = num2;
				num2++;
			}
		}
	}
	for (int i = 0; i < num1; i++) {
		for (int j = 0; j < num2; j++) {
			w2[i][j] = 0;
		}
	}
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (x[i][j] == 'x') continue;
			for (int d = 0; d < 4; d++) {
				int i2 = i + dy[d];
				int j2 = j + dx[d];
				if (i2 < 0 || j2 < 0 || i2 >= M || j2 >= N) continue;
				if (x[i2][j2] == 'x') continue;
				if (j % 2 == 0) {
					w2[pos[i][j]][pos[i2][j2]] = 1;
				} else {
					w2[pos[i2][j2]][pos[i][j]] = 1;
				}
			}
		}
	}
	int r = bipartiteMatching(num1, num2);
	return r + (num1 - r) + (num2 - r);
}

int main() {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		int res = doit();
		printf("Case #%d: %d\n", i, res);
	}
}

