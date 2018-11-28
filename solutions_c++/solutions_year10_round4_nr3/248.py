#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

int bac[110][110];
int dx[2] = {0, -1}, dy[2] = {-1, 0};

int move(int t) {
	vector<vector<int> > next(110, vector<int>(110, 0));
	for(int i = 0; i < 100; ++i) {
		for(int j = 0; j < 100; ++j) {
			int num = 0;
			for(int k = 0; k < 2; ++k) {
				int ii = i + dx[k], jj = j + dy[k];
				if(ii < 0 || jj < 0) continue;
				if(bac[ii][jj]) ++num;
			}
			next[i][j] = bac[i][j] && num || num == 2;
		}
	}
	int res = 0;
	for(int i = 0; i < 100; ++i) {
		for(int j = 0; j < 100; ++j) {
			bac[i][j] = next[i][j];
			res += bac[i][j];
		}
	}
	return res;
}

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		printf("Case #%d: ", t + 1);
		int r;
		cin >> r;
		for(int i = 0; i < r; ++i) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for(int j = x1 - 1; j < x2; ++j) {
				for(int k = y1 - 1; k < y2; ++k) bac[j][k] = 1;
			}
		}
		int res = 1;
		while(move(t)) ++res;
		cout << res << endl;
	}
	return 0;
}
