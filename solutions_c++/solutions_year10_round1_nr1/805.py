#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <queue>
#include <iostream>
#include <cmath>
#include <memory.h>
#include <string>
#include <cstring>
#include <stack>
#include <utility>
using namespace std;
#define pb push_back
#define mp make_pair
#define MAXN 55
typedef long long ll;
int db[4] = {-1, 0, -1, 1};
int dk[4] = {0, 1, 1, 1};
int N, K;
vector <char> map[MAXN];
bool cek(int b, int k, char x, int dapat, int arah) {
	if (dapat >= K)
		return true;
	if (b < 0 || b >= N)
		return false;
	if (k < 0 || k >= N)
		return false;
	if (map[b][k] != x)
		return false;
	return cek (b + db[arah], k + dk[arah], x, dapat + 1, arah);
}
int main() {
	int jtc;
	scanf("%d", &jtc);
	for (int tc = 0; tc < jtc; tc++) {
		scanf("%d %d", &N, &K);
		scanf("%*c");
		int i, j;
		for (i = 0; i < N; i++) {
			int byk = 0;
			vector <char> tmp;
			for (j = 0; j < N; j++) {
				char dum;
				scanf("%c", &dum);
				if (dum != '.')
					tmp.pb(dum);
				else
					byk++;
			}
			scanf("%*c");
			for (j = 0; j < byk; j++)
				map[i].pb('.');
			for (j = 0; j < tmp.size(); j++)
				map[i].pb(tmp[j]);
		}
		bool merah, biru;
		merah = false;
		biru = false;
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				bool lho;
				if (map[i][j] != '.') {
					if (merah && map[i][j] == 'R')
						continue;
					if (biru && map[i][j] == 'B')
						continue;
					for (int k = 0; k < 4; k++) {
						lho = cek(i, j, map[i][j], 0, k);
						if (lho) {
							if (map[i][j] == 'R') {
								merah = true;
								break;
							}
							else if (map[i][j] == 'B') {
								biru = true;
								break;
							}
						}
					}
				}
			}
		}
		printf("Case #%d: ", tc + 1);
		if (merah && biru)
			printf("Both\n");
		else if (merah)
			printf("Red\n");
		else if (biru)
			printf("Blue\n");
		else
			printf("Neither\n");
		for (i = 0; i < N; i++)
			map[i].clear();
	}
	return 0;
}
