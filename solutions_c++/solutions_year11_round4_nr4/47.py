#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int P,W;
vector<int> conn[1024];

int dist[1024];
int used[1024];

int T=1;
void calcD() {
	vector<int> cur,next;
	cur.push_back(1);
	++T;
	used[1]=T;
	int d=0;
	while(!cur.empty()) {
		for(size_t i=0; i<cur.size(); ++i) {
			int a = cur[i];
//			cout<<"label "<<a<<' '<<d<<' '<<conn[a].size()<<'\n';
			dist[a] = d;
			for(size_t j=0; j<conn[a].size(); ++j) {
				int t = conn[a][j];
				if (used[t]==T) continue;
				used[t]=T;
				next.push_back(t);
			}
		}
		cur.clear();
		cur.swap(next);
		++d;
	}
}

const int MN = 402;
int dp[402][MN][MN];
bool done[MN][MN][MN];
int setU(int n) {
	int r=0;
	for(size_t i=0; i<conn[n].size(); ++i) {
		int t = conn[n][i];
		if (used[t]!=T) used[t]=T, ++r;
	}
	return r;
}
int dfs(int n, int f, int f2) {
//	cout<<"dfs "<<n<<' '<<f<<'\n';
	if (n==1) return 1;
	if (done[n][f][f2]) return dp[n][f][f2];
	++T;
	used[f] = T;
	used[f2] = T;
	if (f2!=f) setU(f2);
	if (f!=n) setU(f);
	int r = setU(n) - 1;

	int rr=-1;
	for(size_t i=0; i<conn[n].size(); ++i) {
		int t = conn[n][i];
//		cout<<"trying: "<<n<<' '<<t<<" : "<<dist[n]<<' '<<dist[t]<<'\n';
		if (dist[t] >= dist[n]) continue;
		rr = max(rr, dfs(t, n, f));
	}
//	cout<<"rrr "<<n<<' '<<f<<' '<<f2<<" : "<<r<<' '<<rr<<'\n';

	done[n][f][f2] = 1;
	return dp[n][f][f2] = r + rr;
}

int main() {
	int t;
	scanf("%d",&t);
	for(int a=1; a<=t; ++a) {
		scanf("%d%d",&P,&W);
		for(int i=0; i<P; ++i) conn[i].clear();
		for(int i=0; i<W; ++i) {
			int x,y;
			scanf("%d,%d",&x,&y);
			conn[x].push_back(y);
			conn[y].push_back(x);
		}

		calcD();
		memset(done,0,sizeof(done));
		int r = dfs(0,0,0);

		cout<<"Case #"<<a<<": "<<dist[0]-1<<' '<<r<<'\n';
	}
}
