#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstdio>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define FILL(v,x) memset((v), (x), sizeof(v));
#define INF 0x3f3f3f3f
#define EPS 1E-8
#define debug(x) cerr << #x << " = " << x << "\n"; 
#define debugv(x,n) cerr << #x << " = ["; REP(i,n) cerr << x[i] << ","; cerr << "\b]\n";
typedef long long int64;
typedef pair<int,int> pii;

int cmp(double a, double b){
	if (fabs(a-b)<1E-8) return 0;
	if (a<b) return -1;
	return 1;
}


int main() {
	int nt;
	char m[100][100];

	scanf("%d",&nt);
	for (int ct=1; ct<=nt; ct++) {
		int r,c,d;
		int res=0;
		scanf("%d %d%d",&r,&c,&d);

		REP(i,r)
			REP(j,c) scanf(" %c", &m[i][j]);

		REP(x1,r)
			for (int x2=x1+2; x2<r; x2++) {
				int n = x2-x1;
				REP(y1,c-n) {
					int y2=y1+n;
					double cx=(double)(x1+x2)/2;
					double cy=(double)(y1+y2)/2;
					double px=0,py=0;
					bool pr[200][200];

					memset(pr,0,sizeof(pr));
					pr[x1][y1] = 1;
					pr[x1][y2] = 1;
					pr[x2][y1] = 1;
					pr[x2][y2] = 1;
					
					for (int i=x1; i<=x2; i++)
					for (int j=y1; j<=y2; j++) {
						if (pr[i][j]) continue;
						px += (i-cx)*(d+(m[i][j]-'0'));
						py += (j-cy)*(d+(m[i][j]-'0'));
					}

					if (cmp(px,0)==0 && cmp(py,0)==0)
						res=max(res,n+1);
				}
			}

		printf("Case #%d: ",ct);
		if (!res) printf("IMPOSSIBLE\n");
		else printf("%d\n",res);	
	}

	return 0;
}
