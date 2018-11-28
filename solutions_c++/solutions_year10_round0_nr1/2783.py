#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <memory.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
int main() {
	int jtc;
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	scanf("%d", &jtc);
	for (int tc = 0; tc < jtc; tc++) {
		int N, K;
		scanf("%d %d", &N, &K);
		bool benar = true;
		for (int i = 0; i < N; i++) {
			if (!(K & (1 << i))) {
				benar = false;
				break;
			}
		}
		if (benar)
			printf("Case #%d: ON\n", tc+1);
		else
			printf("Case #%d: OFF\n", tc+1);
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
