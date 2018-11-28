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

#define LL long long

const int maxn = 600;

struct Sum {
	LL s[maxn][maxn], v[maxn][maxn];
	int n, m;
	int clear(int _n=0,int _m=0) {
	//	memset(s,0,sizeof(s));
	//	memset(v,0,sizeof(v));
		n=_n;m=_m;
	}
	int set(int x, int y,int k) {
		v[x][y]=k;
	}
	int init(){
		for(int i=1;i<=n;++i)
			for(int j=1;j<=m;++j)
				s[i][j] = s[i-1][j] + s[i][j-1] + v[i][j] - s[i-1][j-1];
	}
	LL get(int x1, int x2, int y1, int y2) {
		return s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1];
	}
}LY, RY, UX, DX, G;

int N, M, D;

int g[maxn][maxn];

char buf[maxn];

int run() {
	scanf("%d %d %d", &N, &M, &D);
	LY.clear(N,M), RY.clear(N,M), UX.clear(N,M), DX.clear(N,M), G.clear(N,M);
	for(int i=0;i<N;++i){
		scanf("%s", buf);
		for(int j=0;j<M;++j) {
			int k = buf[j] - '0' + D;
			g[i+1][j+1]=k;
		}
	}
	
	for(int i=1;i<=N;++i)
		for(int j=1;j<=M;++j) {
			int k = g[i][j];
			UX.set(i,j,k*i);
			DX.set(i,j,k*(N-i+1));
			LY.set(i,j,k*j);
			RY.set(i,j,k*(M-j+1));
			G.set(i,j,k);
		}
	UX.init();DX.init();LY.init();RY.init();G.init();

	int res = 2;
	for(int a=1;a<=N;++a)
		for(int b=1;b<=M;++b) 
			for(int k=res+1;a+k-1<=N&&b+k-1<=M;++k){
				if(k & 1) {
				int c = a + k - 1, d = b + k - 1;
				LL h = k / 2;
				LL Ysum = -(RY.get(a,c,b,b+h-1) - G.get(a,c,b,b+h-1) * (M-b-h+1))
					    + LY.get(a,c,d-h+1,d) - G.get(a,c,d-h+1,d) * (d-h);
				Ysum -= g[a][b] * (-h) + g[c][b] * (-h) + g[a][d] * h + g[c][d] * h;
				if(Ysum) continue;
				LL Xsum = -(DX.get(a,a+h-1,b,d) - G.get(a,a+h-1,b,d) * (N-a-h+1))
				   		+ UX.get(c-h+1,c,b,d) - G.get(c-h+1,c,b,d) * (c-h);
				Xsum -= g[a][b] * (-h) + g[a][d] * (-h) + g[c][b] * h + g[c][d] * h;
				if(Xsum == 0) res = max(res, k);
				} else {
					
					
					
					///////////////////////////////////////  even k 
					int c = a + k - 1, d = b + k - 1;
				LL h = k / 2;
				LL Ysum = -(RY.get(a,c,b,b+h-1) - G.get(a,c,b,b+h-1) * (M-b-h+1))
					    + LY.get(a,c,d-h+1,d) - G.get(a,c,d-h+1,d) * (d-h);
				
				Ysum *= 2;
				
				Ysum -= -G.get(a,c,b,b+h-1) + G.get(a,c,d-h+1,d);
				
				Ysum -= -g[a][b] * (2*h-1) -g[c][b] * (2*h-1) + g[a][d] * (2*h-1) + g[c][d] * (2*h-1);
				if(Ysum) continue;
				LL Xsum = -(DX.get(a,a+h-1,b,d) - G.get(a,a+h-1,b,d) * (N-a-h+1))
				   		+ UX.get(c-h+1,c,b,d) - G.get(c-h+1,c,b,d) * (c-h);
				
				Xsum *= 2;
				Xsum -= - G.get(a,a+h-1,b,d) + G.get(c-h+1,c,b,d);
				
				Xsum -= -g[a][b] * (2*h-1) - g[a][d] * (2*h-1) + g[c][b] * (2*h-1) + g[c][d] * (2*h-1);
				
				if(Xsum == 0) res = max(res, k);
				}
			}
	return res;
}


int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int test; scanf("%d", &test);
	for(int no=1;no<=test;++no){
		printf("Case #%d: ", no);
		int ret = run();
		if(ret < 3) puts("IMPOSSIBLE");
		else printf("%d\n", ret);
	}
}
