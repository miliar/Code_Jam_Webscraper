#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<set>
#include<map>
#include<sstream>
#include<queue>
#include<climits>
#include<cmath>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

int K, H;

const int FREE = -1;

int data[1024][1024];

int temp[1024][1024];
int LEN;

bool flood(int r, int c, int d) {
	if(temp[r][c] == d) return true;
	if(temp[r][c] != FREE) return false;
	temp[r][c] = d;
	{
		// flip diagonal 1
		int fr = LEN - r - 1;
		int fc = LEN - c - 1;
		if(!flood(fr, fc, d)) return false;
	}
	{
		// flip diagonal 2
		int fr = c;
		int fc = r;
		if(!flood(fr, fc, d)) return false;
	}
	return true;
}

inline bool check(int diff, int offr, int offc) {
	LEN = K + diff;
	for(int r = 0; r < LEN; ++r) {
		for(int c = 0; c < LEN; ++c) {
			temp[r][c] = FREE;
		}
	}
	for(int dr = 0; dr < K; ++dr) {
		for(int dc = 0; dc < K; ++dc) {
			const int d0 = data[dr][dc];
			// actual coord
			int r = dr + offr;
			int c = dc + offc;
			if(!flood(r, c, d0)) return false;
		}
	}
	return true;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> K;
		H = 2 * K - 1;
		for(int i = 0; i < K; ++i) {
			for(int c = 0; i - c >= 0; ++c) {
				cin >> data[i - c][c];
				// cout << ' ' << data[i - c][c];
			}
			// cout << endl;
		}
		for(int i = K; i < H; ++i) {
			for(int c = i - K + 1; c < K; ++c) {
				cin >> data[i - c][c];
				// cout << ' ' << data[i - c][c];
			}
			// cout << endl;
		}
		/*
		   for(int r = 0; r < K; ++r) {
		   for(int c = 0; c < K; ++c) {
		   cout << data[r][c] << " ";
		   }
		   cout << endl;
		   }
		 */
		int diff;
		for(diff = 0; ; ++diff) {
			for(int offr = 0; offr <= diff; ++offr) {
				for(int offc = 0; offc <= diff; ++offc) {
					if(check(diff, offr, offc)) {
						goto here;
					}
				}
			}
		}
here:
		int len = K + diff;
		int ans = len * len - K * K;
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}

