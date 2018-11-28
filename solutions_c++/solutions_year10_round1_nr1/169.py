#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

char S[1 << 10][1 << 10];

void solve(int numTst) {
	int N, K;
	cin >> N >> K;
	for (int i = 0; i < N; ++i) {
		cin >> S[i];
		int p = N - 1;
		for (int j = N - 1; j >= 0; --j) {
			if (S[i][j] != '.') {
				S[i][p--] = S[i][j];
			}
		}
		for (int j = 0; j <= p; ++j) {
			S[i][j] = '.';
		}
		//cout << S[i] << endl;
	}

	bool isRed = false;
	bool isBlue = false;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			for (int di = -1; di <= 1; ++di) {
				for (int dj = -1; dj <= 1; ++dj) {
					if (!di && !dj) continue;
					int red = 0, blue = 0;
					for (int k = 0; k < K; ++k) {
						int ni = i + di * k;
						int nj = j + dj * k;
						if (ni < 0 || ni >= N) break;
						if (nj < 0 || nj >= N) break;
						if (S[ni][nj] == 'R') ++red;
						if (S[ni][nj] == 'B') ++blue;
					}
					if (red == K) isRed = true;
					if (blue == K) isBlue = true;
				}
			}
		}
	}

	string ans;
	if (isRed && isBlue) ans = "Both";
	else if (isRed && !isBlue) ans = "Red";
	else if (!isRed && isBlue) ans = "Blue";
	else ans = "Neither";
	printf("Case #%d: %s\n", numTst, ans.c_str());


}

int main() {	
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}

