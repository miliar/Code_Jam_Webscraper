#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<set>
#include<cmath>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		int n, goal, curO = 1, curB = 1, ans = 0, leftO = 0, leftB = 0;
		char way[2];
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s%d", way, &goal);
			if (way[0] == 'O') {
				if (leftO >= abs(curO - goal)) {
					leftO = 0;
					ans += 1;
					leftB += 1;
				} else {
					ans += abs(curO - goal) - leftO + 1;
					leftB += abs(curO - goal) - leftO + 1;
					leftO = 0;
				}
				curO = goal;
			} else {
				if (leftB >= abs(curB - goal)) {
					leftB = 0;
					ans += 1;
					leftO += 1;
				} else {
					ans += abs(curB - goal) - leftB + 1;
					leftO += abs(curB - goal) - leftB + 1;
					leftB = 0;
				}
				curB = goal;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
