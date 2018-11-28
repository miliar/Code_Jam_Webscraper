#include <cstdio>
#include <queue>
#include <memory.h>
using namespace std;
int T,g[2000],r,k,n,ans;
int t[2000];
queue <int> que;
int run() {
	int man=0,ride=0,dep=0,i;
	while(1) {
		if(que.empty() || man+que.front()>k) {
			ride++;
			ans+=man;
			man=0;
			for(i=0;i<dep;i++) {
				que.push(t[i]);
			}
			dep=0;
			if(ride==r) break;
		}
		man+=que.front();
		t[dep++]=que.front();
		que.pop();
	}
	while(!que.empty()) que.pop();
	return 0;
}
int scan(FILE *fi,FILE *fo) {
	fscanf(fi,"%d",&T);
	int Ti;
	for(Ti=0;Ti<T;Ti++) {
		fscanf(fi,"%d%d%d",&r,&k,&n);
		int i;
		for(i=0;i<n;i++) {
			fscanf(fi,"%d",&g[i]);
			que.push(g[i]);
		}
		run();
		fprintf(fo,"Case #%d: %d\n",Ti+1,ans);
		ans=0;
		memset(g,0,sizeof(g));
	}
	return 0;
}
int main() {
	scan(fopen("INPUT.TXT","rt"),fopen("OUTPUT.TXT","wt"));
	return 0;
}