#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define MAXP 10
int P;
struct node{
	int val;
	int index;
};
node M[1<<MAXP];
bool play[1<<MAXP][1<<MAXP];
void input() {
	scanf("%d", &P);
	for (int i=0; i<(1<<P); ++i) {
		scanf("%d", &M[i].val);
		M[i].index = i;
	}
	for (int i=0; i<P; ++i) {
		for (int j=0; j<(1<<(P-1-i)); ++j) {
			int k;
			scanf("%d", &k);
		}
	}
}
bool cmp(node a, node b) {
	return a.val < b.val;
}
int solve() {
	sort(M, M+(1<<P), cmp);
	memset(play, false, sizeof(play));
	for (int i=0; i<(1<<P); ++i) {
		int index = M[i].index;
		int val = M[i].val;
		// printf("id val: %d %d\n", index, val);
		for (int k=val; k<P; ++k) {
			int t = index/(1<<(k+1));
			play[k][t] = true;
			//printf("  k t %d %d\n", k, t);
		}
	}
	int ans = 0;
	for (int i=0; i<P; ++i) {
		int len = 1<<(P-i-1);
		for (int j=0; j<len; ++j) {
			if (play[i][j]) {
				ans++;
			}
		}
		//printf("ans: %d\n", ans);
	}
	return ans;
}
int main(int argc, char* argv[]) {
	int T;
	scanf("%d", &T);
	int cas = 1;
	while (T--) {
		input();
		printf("Case #%d: %d\n", cas++, solve());
	}
}