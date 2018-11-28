#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;

int main()
{
	int T, R, k, N;
	int tmp;
	int money;
	queue<int> g, q;
	scanf("%d", &T);

	for(int i=1; i<=T; i++) {
		money = 0;
		while(g.size() > 0) {
			g.pop();
		}
		scanf("%d", &R);
		scanf("%d", &k);
		scanf("%d", &N);

		for(int j=0; j<N; j++) {
			scanf("%d", &tmp);
			g.push(tmp);
		}
		//----------Calculate the Money----------------
		for(int j=0; j<R; j++) {
			tmp = 0;
			while(tmp+g.front() <= k) {
				tmp += g.front();
				q.push(g.front());
				g.pop();
				if(g.size() == 0) {
					break;
				}
			}
			money += tmp;
			while(q.size() > 0) {
				g.push(q.front());
				q.pop();
			}
		}
		//---------------------------------------------
		printf("Case #%d: %d\n", i, money);
	}
	return 0;
}