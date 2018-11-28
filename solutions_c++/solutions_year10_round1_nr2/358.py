#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)
#define min(a, b) ((a)<(b)?(a):(b))

const int MAXN=111, MAXP=256;
const int inf=MAXP*MAXN*MAXN*MAXN;

int f[MAXN][256];
int a[MAXN];
int del, ins, n, m;

int main()
{
	freopen("b-small.in", "rt", stdin);
	freopen("b-small.out", "wt", stdout);
	int T, tt=0;
	scanf("%d", &T);
	while (tt<T) {
		scanf("%d%d%d%d", &del, &ins, &m, &n);
		memset(f, 126, sizeof(f));
		REP(i, n) scanf("%d", &a[i]);
		REP(i, MAXP) f[0][i]=abs(a[0]-i);
		for(int i=1; i<n; ++i) {
			REP(j, MAXP) f[i][j]=abs(a[i]-j)+del*i;
			int best=inf;
			for(int j=i-1, r=0; j>=0; --j, ++r) {
				REP(k, MAXP) 
					REP(w, MAXP) {
						if (abs(k-w)<=m) {
							f[i][k]=min(f[i][k], f[j][w]+del*r+abs(k-a[i]));
//							cout << f[i][k] << endl;
						} else {
							if (m==0) continue;
							if (k>w) {
								int cIns;
								cIns=(k-w-1)/m;
	 							f[i][k]=min(f[i][k], f[j][w]+del*r+abs(k-a[i])+cIns*ins);
//								cout << f[i][tk] << endl;
							} else {
								int cIns;
								cIns=(w-k-1)/m;
								f[i][k]=min(f[i][k], f[j][w]+del*r+abs(k-a[i])+cIns*ins);

//								cout << f[
							}
						}
				}
			}
			REP(p, MAXP) 
				if (f[i][p]<best) best=f[i][p];
//			printf("%d\n", best);
		}
		int ans=inf;
		REP(i, MAXP) 
			if (f[n-1][i]<ans) ans=f[n-1][i];
		printf("Case #%d: %d\n", ++tt, ans);
	}
	return 0;
}
