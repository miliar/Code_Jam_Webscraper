#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int dr[] = { 1,-1, 0, 0,-1,-1, 1, 1};
const int dc[] = { 0, 0, 1,-1,-1, 1,-1, 1};

char orig[64][64];
char data[64][64];

int N, K;

void gravity() {
	for(int r = 0; r < N; ++r) {
		int at = N-1;
		for(int c = N-1; c >= 0; --c) {
			if(orig[r][c] == '.') continue;
			swap(orig[r][at], orig[r][c]);
			at--;
		}
	}
	/*
	for(int r = 0; r < N; ++r) {
		for(int c = 0; c < N; ++c) {
			cout << orig[r][c];
		}
		cout << endl;
	}
	*/
}

bool canwin(char me) {
	for(int r = 0; r < N; ++r) {
		for(int c = 0; c < N; ++c) {
			if(orig[r][c] != me) continue;
			for(int d = 0; d < 8; ++d) {
				int er = r + dr[d] * (K-1);
				int ec = c + dc[d] * (K-1);
				if(er < 0 || ec < 0 || er >= N || ec >= N) continue;
				for(int k = 0; k < K; ++k) {
					int nr = r + dr[d] * k;
					int nc = c + dc[d] * k;
					if(orig[nr][nc] != me) break;
					if(k == K-1) return true;
				}
			}
		}
	}
	return false;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> N >> K;
		for(int r = 0; r < N; ++r) {
			for(int c = 0; c < N; ++c) {
				cin >> orig[r][c];
			}
		}
		gravity();
		bool b = canwin('B');
		bool r = canwin('R');
		cout << "Case #" << tt << ": ";
		if(b && r) {
			cout << "Both";
		} else if(b) {
			cout << "Blue";
		} else if(r) {
			cout << "Red";
		} else {
			cout << "Neither";
		}
		cout << endl;
	}
	return 0;
}

