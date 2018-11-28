#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long lol;

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

lol N;
int pD, pG;

void solve(int testcase)
{
	printf("Case #%d: ", testcase);
	cin >> N >> pD >> pG;
	for (int D = 1; D <= N; ++D) {
		if (D * pD % 100 != 0) continue;
		int win = D * pD / 100;
		int lose = D - win;
		for (lol G = 1ll; G <= 100ll; ++G) {
			if (G * pG % 100 != 0) continue;
			G *= 1e9;
			if (G * pG / 100 < win) break;
			if (G - G * pG / 100 < lose) break;
			puts("Possible");
			return;
		}
		break;
	}
	puts("Broken");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) solve(i);
	return 0;
}
