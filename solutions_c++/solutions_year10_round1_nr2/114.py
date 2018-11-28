#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;
#define PII pair<int,int>
#define mkp(a,b) make_pair(a,b)
#define x first
#define y second
#define LL long long
#define CPX complex<double>
#define ME(a) memset(a,0,sizeof(a))
#define MM(a,b) memset(a,b,sizeof(a))
#define MCP(a,b) memcpy(a,b,sizeof(a))

const int MaxN = 200;
const int MaxV = 256;

int no;

int N, M, I, D;

int opt[MaxN][MaxV], A[MaxN];
bool vst[MaxN][MaxV];

int check(int i, int j, int d) {
	if(d<opt[i][j]){opt[i][j]=d;return true;}return false;
}

int run() {
	printf("Case #%d: ",++no);
	scanf("%d %d %d %d",&D,&I,&M,&N);
	for(int i=1;i<=N;++i)
		scanf("%d",A+i);
	int res = N * D;
	memset(opt,-1,sizeof(opt));
	queue<PII > Q;
	for(int i=1;i<=N;++i)
		for(int v=0;v<MaxV;++v) {
			opt[i][v] = min(i * D + I, (i - 1)*D + abs(v - A[i]));
			Q.push(mkp(i,v));
			vst[i][v]=true;
		}
	while(!Q.empty()){
		PII t = Q.front();
		Q.pop();
		vst[t.x][t.y] = false;
		int d = opt[t.x][t.y];
		if(t.x == N) res=min(res,d);
		else 
			if(check(t.x+1,t.y,d+D))
				if(!vst[t.x+1][t.y]){
					vst[t.x+1][t.y]=true;
					Q.push(mkp(t.x,t.y));
				}
		int k = t.x, v = t.y;
		for(int u=0;u<MaxV;++u){
			if(abs(v-u)>M)continue;
			if(check(k,u,d+I))
				if(!vst[k][u]){
					vst[k][u]=true;
					Q.push(mkp(k,u));
				}
			if(check(k,u,d+abs(u-v)))
				if(!vst[k][u]){
					vst[k][u]=true;
					Q.push(mkp(k,u));
				}
			if(check(k,u,d+abs(u-v)))
				if(!vst[k][u]){
					vst[k][u]=true;
					Q.push(mkp(k,u));
				}
			if(k<N&&check(k+1,u,d+abs(u-A[k+1])))
				if(!vst[k+1][u]){
					vst[k+1][u]=true;
					Q.push(mkp(k+1,u));
				}
		}
	}
	printf("%d\n",res);
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int test;
	scanf("%d", &test);
	while(test--)run();
}
