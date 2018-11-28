#include <algorithm>
#include <cassert>
#include <complex>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> pii;
typedef complex<double> pt;

int N, K;
string board[55];
string rboard[55];

// check rboard to see if c has won
int D = 8;
int xs[8] = {1, 0, 1, 1, -1, -1, -1, 0};
int ys[8] = {0, 1, 1, -1, -1, 1, 0, -1};
bool has_won(char c) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			for (int d = 0; d < D; d++) {
				int k;
				for (k = 0; k < K; k++) {
					int x = i + k*xs[d];
					int y = j + k*ys[d];
					if (x < 0 || x >= N || y < 0 || y >= N || rboard[x][y] != c)
						break;
				}
				if (k == K)
					return true;
			}
		}
	}
	return false;
}

// print board
void print_board() {
	cout << "printing board..." << endl;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			cout << rboard[i][j];
		cout << endl;
	}
	cout << endl;
}

int main() {
	int num_tests; cin >> num_tests;
	for (int test = 1; test <= num_tests; test++) {
		// read in board
		cin >> N >> K;
		getline(cin, board[0]);
		for (int i = 0; i < N; i++)
			getline(cin, board[i]);
		// rotate board
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				rboard[j][N - 1 - i] = board[i][j];
		// let gravity work
		for (int x = 0; x < N; x++) {
			vector<char> v;
			for (int y = N - 1; y >= 0; y--) {
				if (rboard[y][x] != '.')
					v.push_back(rboard[y][x]);
			}
			for (int i = 0; i < int(v.size()); i++)
				rboard[N - 1 - i][x] = v[i];
			for (int i = int(v.size()); i < N; i++)
				rboard[N - 1 - i][x] = '.';
		}
		// check if anyone has won
		bool r = has_won('R');
		bool b = has_won('B');
		string ans = "Neither";
		if (r && b)
			ans = "Both";
		else if (r)
			ans = "Red";
		else if (b)
			ans = "Blue";
		// output answer
		cout << "Case #" << test << ": " << ans << endl;
	}
}

