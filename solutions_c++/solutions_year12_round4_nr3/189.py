#include<stdio.h>
#include<vector>
using namespace std;

vector<pair<int,int> > l[2048];
int p[2048];
int b[2048];
int a[2048];
int c[2048];
int n;

void dfs(int k,int h) {
	a[k]=h,b[k]=1;
	for(int i=0;i<l[k].size();i++) if (!b[l[k][i].first]) {
		dfs(l[k][i].first,h+l[k][i].second*(l[k][i].first-k));
	}
}

int dfs1(int s,int t,int d) {
	for(int i=s;i<t-1;i=p[i]) {
		l[i].push_back(make_pair(p[i],d));
		l[p[i]].push_back(make_pair(i,d));
		if (!dfs1(i+1,p[i],d+1)) return 0;
		if (p[i]==i+1) continue;
		if (p[p[i]-1]!=p[i]) return 0;
		l[p[i]-1].push_back(make_pair(p[i],d+1));
		l[p[i]].push_back(make_pair(p[i]-1,d+1));
	}
	return 1;
}

int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;) {
		scanf("%d",&n);
		for(int i=0;i<n-1;i++) scanf("%d",&p[i]),p[i]--;
		for(int i=0;i<n;i++) l[i].clear();
		if (!dfs1(0,n-1,0)) {
			printf("Case #%d: Impossible\n",++cs);
			continue;
		}
		memset(b,0,sizeof(b));
		dfs(0,0);
		int mn=1000000000;
		for(int i=0;i<n;i++) if (a[i]<mn) mn=a[i];
		printf("Case #%d:",++cs);
		for(int i=0;i<n;i++) printf(" %d",a[i]-mn);
		puts("");
	}
	return 0;
}
