#include <iostream>
#include <string>
using namespace std;

const char X = 'x';
const char O = '.';

int C, MM, NN, N, M;
 
int  adj_list[7000][7000];
int  adj_size[7000];
int  prev[7000];
bool mark[7000];
int node_num[100][100];

string grid[100];

void add_edge(int n, int x, int y) {
	if (x < 0 || x >= MM || y < 0 || y >= NN) return;
	if (grid[x][y] == X) return;
	adj_list[n][adj_size[n]++] = node_num[x][y];
}

void build_graph() {
	N = M = 0;
	for (int i = 0; i < MM; i++) {
		for (int j = 0; j < NN; j++) {
			if (grid[i][j] == X) continue;
			if (j % 2 == 0) {
				node_num[i][j] = N++;
			} else {
				node_num[i][j] = M++;
			}
		}
	}
	memset(adj_size, 0, sizeof(adj_size));
	for (int i = 0; i < MM; i++) {
		for (int j = 0; j < NN; j += 2) {
			if (grid[i][j] == X) continue;
			add_edge(node_num[i][j], i-1, j-1);
			add_edge(node_num[i][j], i-1, j+1);
			add_edge(node_num[i][j], i, j-1);
			add_edge(node_num[i][j], i, j+1);
			add_edge(node_num[i][j], i+1, j+1);
			add_edge(node_num[i][j], i+1, j-1);
		}
	}
}

bool find_match(int node) {
    if (node == -1) return true;
    for (int i = 0; i < adj_size[node]; i++) {
        int match = adj_list[node][i];
        if (mark[match]) continue;
        mark[match] = true;
        if (find_match(prev[match])) {
            prev[match] = node;
            return true;
        }
    }
    return false;
}

int max_matching() {
    memset(prev, -1, sizeof(prev));
    int matching = 0;
    for (int i = 0; i < N; i++) {
        memset(mark, 0, sizeof(mark));
        if (find_match(i)) matching++;
    }
    return matching;
}

int main() {
	cin >> C;
	for (int tcs = 1; tcs <= C; tcs++) {
		cin >> MM >> NN;
		for (int i = 0; i < MM; i++) cin >> grid[i];
		build_graph();
		int m = max_matching();
		int n = MM*NN;
		for (int i = 0; i < MM; i++) {
			for (int j = 0; j < NN; j++) {
				if (grid[i][j] == X) n--;
			}
		}
		cout << "Case #" << tcs << ": " << n - m << endl;
	}
	return 0;
}
