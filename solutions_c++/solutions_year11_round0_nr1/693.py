#include <cstdio>
#include <queue>
#define FOR(i,a,b) for(int i=int(a);i<int(b);++i)
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	FOR(z,0,T) {
		int n, cur[] = {1, 1}, res = 0;
		queue<int> Q[2], Moves;
		scanf("%d", &n);
		FOR(i,0,n) {
			char c[2]; int k;
			scanf("%s%d", c, &k);
			if(c[0] == 'B') Q[0].push(k), Moves.push(k);
			else Q[1].push(k), Moves.push(-k);
		}
		while(!Moves.empty()) {
			int ind = int(Moves.front() < 0);
			if(cur[ind] > Q[ind].front()) --cur[ind];
			else if(cur[ind] < Q[ind].front()) ++cur[ind];
			else Q[ind].pop(), Moves.pop();
			ind = 1 - ind;
			if(Q[ind].empty());
			else if(cur[ind] > Q[ind].front()) --cur[ind];
			else if(cur[ind] < Q[ind].front()) ++cur[ind];
			++res;
		}
		printf("Case #%d: %d\n", z + 1, res);
	}
	return 0;
}
