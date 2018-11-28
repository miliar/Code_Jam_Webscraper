#include <iostream>
using namespace std;

#define MAXN 110
#define MAXK 30

int price[MAXN][MAXK];

int a[MAXN][MAXN];

int x, y, m, n, k, nTest;
int mX[MAXN],mY[MAXN];
bool visit[MAXN];

bool Match(int u) {	
	if (u==-1) return true;
	for (int v=0; v<n; ++v)
		if (a[u][v] && !visit[v]) {
			visit[v]=true;
			if (Match(mY[v])) {
				mX[u]=v;
				mY[v]=u;
				return true;
			}			
		}
	return false;
}
	
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	cin >> nTest;
	for (int test=1; test<=nTest; ++test) {
		cin >> n >> k;
		for (int i=0; i<n; ++i) 
			for (int j=0; j<k; ++j)
				cin >> price[i][j];


		memset(a,0,sizeof(a));
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j) {
				a[i][j]=true;
				for (int t=0; t<k; ++t) {
					if (price[i][t] >= price[j][t]) {
						a[i][j]=false;
						break;
					}
				}
			}
	
		memset(mX,-1,sizeof(mX));
		memset(mY,-1,sizeof(mY));		
		int cnt=0;
		for (int i=0; i<n; ++i)
		if (mX[i]==-1) {			
			memset(visit,0,sizeof(visit));
			if (Match(i)) {
				++cnt;
			}
		}
		printf("Case #%d: %d\n",test, n-cnt);	
	}
	
	return 0;
}
