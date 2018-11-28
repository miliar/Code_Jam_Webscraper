#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int tests,n,m;

vector<int> next[10];
int a[10][10];
int c[10];

int colors, ok;
int cyc;
int v[10];

int allCol() {
	int f[10];
	for (int i=1;i<=colors;i++) f[i]=0;
	for (int i=1;i<=n;i++) if (v[i]) f[c[i]]++;
	for (int i=1;i<=colors;i++) if (f[i]==0) return 0;
	return 1;
}

void check(int id, int prev=-1) {
	if (!cyc) return;
	if (v[id]) {
		//for (int id=1;id<=n;id++) if (v[id]) printf("%d:%d ",id,c[id]);
		if (!allCol()) {
			//printf("fail\n");
			cyc=0;
		}
	} else {
		v[id]=1;
		for (int i=0;i<next[id].size();i++) if (next[id][i]!=prev) check(next[id][i],id);
		v[id]=0;
	}
}

vector<int> sol;
void solve(int x) {
	if (ok) return;
	if (x>n) {
		cyc=1;
		for (int id=1;id<=n && cyc;id++) {
			//printf("source=%d\n",id);
			check(id);
		}
		if (cyc) {
			//for (int id=1;id<=n;id++) printf("%d ",c[id]);
			//printf("\n");
			ok=1;
			sol.clear();
			for (int id=1;id<=n;id++) sol.push_back(c[id]);
		}
	} else {
		for (int i=1;i<=colors;i++) {
			c[x]=i;
			solve(x+1);
		}
	}
}

int xx[10];
int yy[10];

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
    	fprintf(stderr,"%d/%d\n",test,tests);
    	scanf("%d %d",&n,&m);
    	for (int i=1;i<=n;i++) {
    		next[i].clear();
    		c[i]=0;
    	}
    	memset(a,0,sizeof(a));
    	for (int i=1;i<n;i++) {
    		next[i].push_back(i+1);
    		next[i+1].push_back(i);
    	}
    	next[n].push_back(1); next[1].push_back(n);
    	for (int i=0;i<m;i++) scanf("%d",&xx[i]);
    	for (int i=0;i<m;i++) scanf("%d",&yy[i]);
    	for (int i=0;i<m;i++) {
    		int x=xx[i],y=yy[i];
    		next[x].push_back(y);
    		next[y].push_back(x);
    		a[x][y]=1; a[y][x]=1;
    	}

    	for (colors=5;colors>=1;colors--) {
    		ok=0;
			c[1]=1;
			solve(2);
			if (ok) {
				printf("Case #%d: %d\n",test,colors);
				printf("%d",sol[0]);
				for (int i=1;i<n;i++) printf(" %d",sol[i]);
				printf("\n");
				break;
			}
    	}
    }
    return 0;
}
