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

int no;

bool P[130][133], T[133][133];

int run() {
	int n = 120, m = 120;
	int r;
	cin >> r;
	if(!r) return 0;
	ME(T);
	while(r--){
		int x1, y1, x2,y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for(int x=x1;x<=x2;++x)
			for(int y=y1;y<=y2;++y)
				T[x][y] = true;
	}
	int ret=0;
	while(1) {
		++ ret;
		bool flag = false;
		for(int i=1;i<n;++i)
			for(int j=1;j<m;++j) {
				P[i][j] = T[i][j];
				if(!T[i-1][j] && !T[i][j-1] && T[i][j])
					P[i][j] = false;
				else {
					if(!T[i][j] && T[i-1][j] && T[i][j-1])
						P[i][j] = true;
				}
				if(P[i][j]) flag = true;
			}
		if(!flag) break;
		MCP(T,P);
	}
	return ret;
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	
	int test;
	scanf("%d", &test);
	while(test--) 
		printf("Case #%d: %d\n",++no, run());
}
