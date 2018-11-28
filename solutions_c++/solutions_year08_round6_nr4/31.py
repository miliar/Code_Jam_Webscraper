#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define mp make_pair
#define pb push_back
#define two(x) (1<<(x))
#define sq(a) (a)*(a)
#define all(c) (c).begin(),(c).end()
#define For(i,b,e) for(int i = b;i < e;i ++)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
const double PI = acos(-1.0);

const int Max = 1000;

int connA[9][9];
int A[9], B[9], n, m;

void input() {
	scanf("%d", &n);
	memset(connA, 0, sizeof(connA));
	for(int i = 0;i < n-1;i ++) {
		int a, b;
		scanf("%d%d", &a,&b);
		connA[b][a] = connA[a][b] = 1;
	}
	scanf("%d", &m);
	for(int i = 0;i < m-1;i ++) scanf("%d%d", &A[i], &B[i]);
}

void solve() {
	vi pos;
	for(int i = 1;i <= n;i ++) pos.push_back(i);
	do {
		int k = 0;
		for(k = 0;k < m-1;k ++) if(connA[pos[A[k]-1]][pos[B[k]-1]] == 0) break;
		if(k >= m-1) {
			printf("YES\n");
			return ;
		}
	} while(next_permutation(all(pos)));
	printf("NO\n");
}

int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for(int ca = 1;ca <= cas;ca ++) {
		input();
		printf("Case #%d: ", ca);
		solve();
	}
	return 0;
}
