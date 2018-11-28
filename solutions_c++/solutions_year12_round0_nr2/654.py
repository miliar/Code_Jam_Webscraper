/*
 * Author: Fish@UESTC_Oblivion
 * Created Time:  2012/04/14 09:31:52
 * Project: 
 *    Type: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 105;
int s[MaxN], N, S, P;
int DP[MaxN][MaxN];

void checkmax(int& a, int b) {
	if (a < b) a = b;
}

bool check(int s, int d) {
	return s - d >= 0 && s <= 10 && s >= P;
}

//x = 1 y = 2 z = 3
bool sol(int s, bool fd) {
	int tmp;
	
	if (fd) {
		//x z z
		if ((s + 2) % 3 == 0) {
			tmp = (s + 2) / 3;
			if (check(tmp, 2)) return true;
		}
		//x y z
		if (s % 3 == 0) {
			tmp = s / 3 + 1;
			if (check(tmp, 2)) return true;
		}
		//x x z
		if ((s - 2) % 3 == 0) {
			tmp = (s - 2) / 3 + 2;
			if (check(tmp, 2)) return true;
		}
	} else {
		//z z z
		if (s % 3 == 0) {
			tmp = s / 3;
			if (check(tmp, 0)) return true;
		}
		//y z z
		if ((s + 1) % 3 == 0) {
			tmp = (s + 1) / 3;
			if (check(tmp, 1)) return true;
		}
		//y y z
		if ((s + 2) % 3 == 0) {
			tmp = (s + 2) / 3;
			if (check(tmp, 1)) return true;
		}
	}
	return false;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 1;
	
	scanf("%d", &T);
	while (T--) {
		memset(DP, -1, sizeof(DP));
		DP[0][0] = 0;
		scanf("%d%d%d", &N, &S, &P);
		for (int i = 0; i < N; i++)
			scanf("%d", &s[i]);
		for (int i = 0; i < N; i++)
			for (int j = 0; j <= S; j++)
				if (DP[i][j] != -1) {
					checkmax(DP[i + 1][j], DP[i][j] + sol(s[i], false));
					if (j < S) checkmax(DP[i + 1][j + 1], DP[i][j] + sol(s[i], true));
				}
		printf("Case #%d: %d\n", cas++, DP[N][S]);
	}
	
	return 0;
}
