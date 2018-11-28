#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define SIZE 105
#define EPS 1e-11
#define INF 1e11

vector<int>v[SIZE],v2[SIZE],t[SIZE];
int n,m;

bool ok(vector<int> p) {
	int i,j,k;
	bool f;
	rep(i,n+1) t[i].clear();
	for(i=1;i<=n;i++) {
		rep(j,v[i].size()) {
			t[p[i-1]].push_back(p[v[i][j]-1]);
		}
	}

	for(i=1;i<=m;i++) {
		rep(j,v2[i].size()) {
			f = 0;
			for(k=0;k<t[i].size();k++) {
				if(v2[i][j] == t[i][k]) {
					f = 1;
					break;
				}
			}
			if(!f) return 0;
		}
	}
	return 1;
}

int main() {
	int T,kase=1;
	bool flag;
	int i,a,b;
	freopen("C:\\Documents and Settings\\codejam\\Desktop\\Projects\\Problem D\\Problem D\\d.in.txt","r",stdin);
	freopen("C:\\Documents and Settings\\codejam\\Desktop\\Projects\\Problem D\\Problem D\\d.out","w",stdout);
	scanf("%d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf("%d",&n);
		rep(i,n+1) v[i].clear();
		rep(i,n-1) {
			scanf("%d%d",&a,&b);
			v[a].push_back(b);
			v[b].push_back(a);
		}

		scanf("%d",&m);
		rep(i,m+1) v2[i].clear();
		rep(i,m-1) {
			scanf("%d%d",&a,&b);
			v2[a].push_back(b);
			v2[b].push_back(a);
		}

		vector<int>p;
		rep(i,n) p.push_back(i+1);

		flag = 0;
		do {
			if(ok(p)) {
				flag = 1;
				break;
			}
		}while(next_permutation(p.begin(),p.end()));
		if(flag) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}