#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

const int nMax = 1001;

bool vis[nMax];
bool edge[nMax][nMax];
int primes[nMax];
int pNum;
int n;

void dfs(int v) {
	if(vis[v]) return;
	vis[v] = true;
	FOR(i,0,n) if(edge[v][i]) dfs(i);
}

void testcase(int tNum) {
	
	int A,B,P;
	scanf("%d %d %d",&A,&B,&P);
	n = B-A+1;
	FOR(i,0,n) FOR(j,0,n) edge[i][j] = false;
	
	FOR(i,A,B+1) FOR(j,i+1,B+1) {
		bool isOk = false;
		for(int k=0; k<pNum; ++k) if(primes[k]>=P && i%primes[k]==0 && j%primes[k]==0) {
			isOk = true;
			break;
		}
		edge[i-A][j-A] = edge[j-A][i-A] = isOk;
	}
	
	int res = 0;
	FOR(i,0,n) vis[i] = false;
	FOR(i,0,n) if(!vis[i]) {
		dfs(i);
		res++;
	}
	printf("Case #%d: %d\n",tNum,res);
}

int main() {
	
	pNum = 0;
	FOR(i,2,1000) {
		bool isP = true;
		for(int j=0; j<pNum && primes[j]*primes[j]<=i; ++j) if(i%primes[j]==0) {
			isP = false;
			break;
		}
		if(isP) primes[pNum++] = i;
	}

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
