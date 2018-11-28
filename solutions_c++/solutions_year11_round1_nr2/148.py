


/*
	Prob: (Google code jam 2011 - Round 1A - B)
	Author: peanut
	Time: 21/05/11 09:44
	Description: T T
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MaxN = 222;
const int MaxM = 22;

int N, M, T, c, s;
char D[MaxN][MaxM], L[MaxN];
bool v[MaxN], contain[MaxN][MaxN];

int check(int k) {
	int len = strlen(D[k]), res = 0;
	memset(v, 1, sizeof(v));
	for (int i = 1; i <= N; ++ i)
		if (strlen(D[i]) != len) v[i] = false;
	for (int i = 0; i < 26; ++ i) {
		bool cc = false;
		for (int j = 1; j <= N; ++ j)
			if (v[j] && contain[j][L[i]]) cc = true;
		if (!cc) continue;
		if (contain[k][L[i]]) {
			for (int j = 1; j <= N; ++ j)
				for (int r = 0; r < len; ++ r)
					if (D[k][r] == L[i] && D[j][r] != L[i] ||
					    D[k][r] != L[i] && D[j][r] == L[i])
					v[j] = false;
		}
		else {
			++ res;
			for (int j = 1; j <= N; ++ j)
				if (contain[j][L[i]]) v[j] = false;
		}
	}
	return res;
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	cin >> T;
	for (int cs = 1; cs <= T; ++ cs) {
		cin >> N >> M;
		printf("Case #%d: ", cs);
		memset(contain, 0, sizeof(contain));
		for (int i = 1; i <= N; ++ i) {
			cin >> D[i];
			for (int j = 0; j < strlen(D[i]); ++ j)
				contain[i][D[i][j]] = true;
		}
		for (int i = 1; i <= M; ++ i) {
			cin >> L;
			c = s = -1;
			for (int j = 1; j <= N; ++ j) {
				int tmp = check(j);
				if (tmp > s) {c = j; s = tmp;}
			}
			cout << D[c];
			if (i < M) cout << " "; else cout << endl;
		}
	}
	
	return 0;
}
