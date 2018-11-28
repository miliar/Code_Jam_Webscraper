#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>

#define FOR(i,a,b) for(int i=(a), _b=(int)(b); i<_b; ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

const int nMax = 10;

int tabN[nMax][nMax];
bool tabB[nMax][nMax];
int N,M;

void testcase(int tNum) {
	printf("Case #%d: ",tNum);	
	scanf("%d %d",&N,&M);
	FOR(i,0,N) FOR(j,0,M) scanf("%d",&tabN[i][j]);
	int res = 0;
	int maxi = N*M - (N/2)*(M-1);
	FOR(mask,0,(1<<maxi)) {
		memset(tabB,0,sizeof(tabB));
		int cur = 0;
		for(int i=0; i<N; i+=2) FOR(j,0,M) {
			if(mask&(1<<(cur++)))
				tabB[i][j] = 1; else
				tabB[i][j] = 0;
		}
		for(int i=1; i<N; i+=2) {
			if(mask&(1<<(cur++)))
				tabB[i][0] = 1; else
				tabB[i][0] = 0;
			FOR(j,1,M) {
				int num = 0;
				FOR(x,max(i-1,0),min(i+2,N)) FOR(y,max(0,j-2),j+1) if(tabB[x][y]) num++;
				if(num == tabN[i][j-1])
					tabB[i][j] = 0; else
					tabB[i][j] = 1;
			}
		}
		bool isOk = true;
		FOR(i,0,N) FOR(j,0,M) {
			int num = 0;
			FOR(x,max(i-1,0),min(i+2,N)) FOR(y,max(0,j-1),min(j+2,M)) if(tabB[x][y]) num++;
			if(num!=tabN[i][j]) isOk = false;
		}
		if(isOk) {
			/*printf("mask=%d\n",mask);
			FOR(i,0,N) {
				FOR(j,0,M) printf("%d",tabB[i][j]);
				printf("\n");
			}*/
			int cur = 0;
			FOR(j,0,M) cur += tabB[N/2][j];
			res = max(res,cur);
		}
	}
	printf("%d\n",res);
}

int main() {

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
