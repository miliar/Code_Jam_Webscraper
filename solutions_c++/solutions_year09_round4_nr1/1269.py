#include<set>
#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define FORE(i,a) for(typeof(a.begin()) i = a.begin(); i!= a.end(); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
#define cs c_str()
#define sz size()
#define mp make_pair
#define pb push_back

typedef long long ll;

char dat[52][52];
int last[52];
int nn;
map<int, vector<int> > mapper[8];
map<vector<int>, int> inverse_mapper[8];
int mini[50012];
int vis[50012], qu[50012];
bool done(vector<int>& now) {
	FOR(i,0,nn)
		if(last[now[i]]>i) return false;
	return true;
}
int doit(int n) {
	int ans = 0;
	SET(mini, 1);
	FOR(i,0,n) {
		last[i] = 0;
		FOR(j,0,n) if(dat[i][j]=='1') last[i] = j;
	}
	nn = n;
	int front = 0, rear = 0;
	SET(vis, 0);
	qu[rear++] = 0;
	mini[0] = 0;
	vis[0] = 1;	
	if(done(mapper[nn-1][0])) return 0;
	for(;front<rear;front++) {
		int stat = qu[front];
		int curr = mini[stat];
		vector<int> now = mapper[nn-1][stat];
		FOR(i,1,n) {
			vector<int> next = now;
			next[i] = now[i-1];
			next[i-1] = now[i];
			int next_stat = inverse_mapper[nn-1][next];
			if(vis[next_stat]) continue;			
			mini[next_stat] = curr + 1;
			vis[next_stat] = 1;
			qu[rear++] = next_stat;
			if(done(next)) return curr+1;
		}
	}
	return ans;
}
void pre(int n) {
	mapper[n-1].clear();
	vector<int> dat;
	FOR(i,0,n) dat.pb(i);
	int cnt = 0;
	do{
		mapper[n-1][cnt] = dat;
		inverse_mapper[n-1][dat] = cnt;
		cnt++;
	} while(next_permutation(dat.begin(), dat.end()));
}
int main() {
	int T, e = 0, n;
	scanf("%d",&T);
	FOR(i,1,9) {
		pre(i);
	}
	while(T--) {
		scanf("%d",&n);
		FOR(i,0,n) scanf("%s",dat[i]);
		int ans = doit(n);
		printf("Case #%d: %d\n",++e, ans);
	}
	return 0;
}

