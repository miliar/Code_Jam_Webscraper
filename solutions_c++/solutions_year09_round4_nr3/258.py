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

int price[110][50];
int mat[110][110];
int used[110], vpair[110];

bool matching(int pos, int p, int n) {
	if(pos == -1) return true;
	for(int i = 0; i < n; ++i) if(mat[pos][i] && used[i] < p) {
		used[i] = p;
		if(matching(vpair[i], p, n)) {
			vpair[i] = pos;
			return true;
		}
	}
	return false;
}

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		int n, K;
		cin >> n >> K;
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < K; ++j) cin >> price[i][j];
			used[i] = 0;
			vpair[i] = -1;
		}
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j) if(i != j) {
				bool ok = true;
				for(int k = 0; k < K; ++k) ok = ok && price[i][k] < price[j][k];
				mat[i][j] = ok;
			}
		}
		int res = 0, p = 0;
		for(int i = 0; i < n; ++i) {
			if(matching(i, ++p, n)) ++res;
		}
		printf("Case #%d: %d\n", t + 1, n - res);
	}
	return 0;
}
