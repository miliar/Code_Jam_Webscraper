/*
 * B.cpp
 *
 *  Created on: 2010-5-22
 *      Author: Allie
 */

#include <vector>
#include <stack> 
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <sstream> 
#include <iostream> 
#include <cmath>
#include <cassert>

using namespace std; 

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;

int delCost;
int insCost;
int M;
int N;
int a[128];

int minimumCost()
{
	vector<vi> best(N + 1, vi(257, INF));
	best[0][256] = 0;
	for (int i = 0; i < N; ++i) {
		vi &b = best[i];
		bool fix[257];
		memset(fix, 0, sizeof(fix));
		while (true) {
			int bj = -1;
			for (int j = 0; j < 257; ++j)
				if (!fix[j] && b[j] < INF && (bj == -1 || b[j] < b[bj]))
					bj = j;
			if (bj == -1)
				break;
			fix[bj] = true;
			for (int j = 0; j < 256; ++j)
				if ((bj == 256 || abs(j - bj) <= M) && b[bj] + insCost < b[j])
					b[j] = b[bj] + insCost;
		}
		for (int j = 0; j < 257; ++j)
			if (b[j] < INF) 
				best[i + 1][j] = min(best[i + 1][j], best[i][j] + delCost);
		for (int j = 0; j < 257; ++j)
			if (b[j] < INF) 
				for (int k = 0; k < 256; ++k)
					if (j == 256 || abs(k - j) <= M)
						best[i + 1][k] = min(best[i + 1][k], b[j] + abs(k - a[i]));
	}
	int res = INF;
	for (int i = 0; i < 257; ++i)
		res = min(res, best[N][i]);
	return res;
}

int main() 
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++icase) {
		cin >> delCost >> insCost >> M >> N;
		for (int i = 0; i < N; ++i)
			cin >> a[i];
		printf("Case #%d: %d\n", icase, minimumCost());
	}
	return 0;
}
