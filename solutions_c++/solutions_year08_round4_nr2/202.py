#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<cassert>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define i64 __int64

vector< pair<int,int> > v;

int n,m;
i64 A;

int main() {
	int i,j,T;
	i64 x1,y1,x2,y2,x3,y3;
	bool flag;
	i64 dx,a,t;
	int kase=1;

	scanf("%d",&T);

	while(T--) {
		scanf(" %d %d %I64d",&n,&m,&A);
		v.clear();
		for(i=0;i<=n;i++) {
			v.push_back( make_pair(i,0) );
			v.push_back( make_pair(i,m) );
		}
		for(j=1;j<m;j++) {
			v.push_back( make_pair(0,j) );
			v.push_back( make_pair(n,j) );
		}
		
		flag = 0;
		printf("Case #%d: ",kase++);
		rep(i,v.size()) {
			x1 = v[i].first;
			y1 = v[i].second;
			
			for(x2=0;x2<=n;x2++) if(x2 != x1) {
				for(y2=0;y2<=m;y2++) {
					t = x1 * y2  - x2 * y1;
					dx = x2 - x1;
					for(x3=0;x3<=n;x3++) {
						a = A - t - x3 * (y1 - y2);
						if(a % dx == 0) {
							y3 = a / dx;
							if(y3 >=0 && y3 <= m) {
								flag = 1;
								printf("%I64d %I64d %I64d %I64d %I64d %I64d\n",x1,y1,x2,y2,x3,y3);
								goto label;
							}
						}
					}
				}
			}
		}
label:
		if(!flag) printf("IMPOSSIBLE\n");
		else {
			t = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3;
			assert(t== A);
		}
		

	}
	return 0;
}