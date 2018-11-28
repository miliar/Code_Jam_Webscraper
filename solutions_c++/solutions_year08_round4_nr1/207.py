#include <cstdio>
#include <string>
#include <iostream>
#pragma comment (linker, "/STACK:10000000")
using namespace std;
const int c=20000;
const int inf=1000000000;
int n,m,v;
int g[c+1],r[c+1],t[c+1];
int d1[c+1],d0[c+1];
bool q;
int k;
int min(int a, int b) {
	return a<b ? a : b;
}
int go1(int i) {
	int p;
	if (d1[i]>=0) return d1[i];
	if (r[i]) d1[i]=0; else
	if (i>(m-1)/2) d1[i]=inf; else
	if (!g[i]) d1[i]=min(go1(i*2),go1(i*2+1)); else {
	if (g[i]) p=go1(i*2)+go1(i*2+1);
	if (t[i]) p=min(p,min(go1(i*2),go1(i*2+1))+1);
	d1[i]=p;
	}
	return d1[i];
}
int go0(int i) {
	int p;
	if (d0[i]>=0) return d0[i];
	if (!r[i]) d0[i]=0; else
	if (i>(m-1)/2) d0[i]=inf; else 
	if (g[i]) d0[i]=min(go0(i*2),go0(i*2+1)); else {
	if (!g[i]) p=go0(i*2)+go0(i*2+1);
	if (t[i]) p=min(p,min(go0(i*2),go0(i*2+1))+1);
	d0[i]=p;
	}
	return d0[i];
}
int main() {
	int i,j,ans;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&n);
	for (i=1; i<=n; ++i) {
		scanf("%d%d",&m,&v);
		memset(d0,-1,sizeof(int)*(m+1));
		memset(d1,-1,sizeof(int)*(m+1));
		for (j=1; j<=(m-1)/2; ++j) scanf("%d%d",&g[j],&t[j]);
		for (j=(m+1)/2; j<=m; ++j) scanf("%d",&r[j]);
		for (j=(m-1)/2; j>=1; --j) {
			if (g[j]) r[j]=r[j*2] && r[j*2+1]; else r[j]=r[j*2] || r[j*2+1];
		}
		cerr << r[1] << '\n';
		if (r[1]==v) ans=0; else {
			if (v) ans=go1(1); else ans=go0(1);
		}
		printf("Case #%d: ",i);
		if (ans<inf) printf("%d\n",ans); else printf("IMPOSSIBLE\n");
	}
	return 0;
}
