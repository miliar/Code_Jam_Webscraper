#include <iostream>
#include <algorithm>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
#define sz(x) (int)(x).size()
#define pb push_back
#define clr(x) (x).clear()
#define all(x) (x).begin(), (x).end()

const int inf = 987654321;
int tn, cc;
int m, v;
int G[10001];
int C[10001];
int S[10001];
int ret;
void input() {
	cin >> m >> v;
	int i;
	int g, c, cnt = 0;
	for(i=0;i<(m-1)/2;++i) {
		++cnt;
		cin >> G[cnt] >> C[cnt];
	}
	for(i=0;i<(m+1)/2;++i) {
		++cnt;
		cin >> G[cnt];
	}
}

bool check() {
	int i;
	for(i=m;i>(m-1)/2;--i) {
		S[i] = G[i];		
	}
	for(i=(m-1)/2;i>=1;--i) {
		if(G[i]) S[i] = S[i*2] * S[i*2+1];
		else S[i] = ( S[i*2] || S[i*2+1] ) ? 1 : 0;
	}
	return S[1] == v;
}
void backtr(int p, int nc) {
	if(nc>=ret) return;
	// fprintf(stderr,"(%d,%d)\n",p,nc);
	if(p>(m-1)/2) {
		if(check()) ret <?= nc;
		return;
	}
	backtr(p+1,nc);
	if(C[p]) {
		G[p] = 1 - G[p];
		backtr(p+1, nc+1);
		G[p] = 1 - G[p];
	}
}
void solve() {
	ret = inf;
	backtr(1,0);
}

void output() {
	printf("Case #%d: ", cc);
	if(ret==inf) printf("IMPOSSIBLE");
	else printf("%d",ret);
	printf("\n");
}

int main() {
	cin >> tn;
	for(cc=1;cc<=tn;++cc) {
		input();
		solve();
		output();
	}
}

