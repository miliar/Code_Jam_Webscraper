#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define REP(i, n) for(int i=0, __n=(n); i<__n; ++i)

const int MAXN = 2001;

int g[MAXN], nt[MAXN], c[MAXN];
int dfn[MAXN], sq[MAXN];
int R, N, k;

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	int tt, T;
	for(tt=0, scanf("%d", &T); tt<T;) {
		printf("Case #%d: ", ++tt);
		scanf("%d%d%d", &R, &k, &N);
		REP(i, N) {
			scanf("%d", &g[i]);
			g[i+N]=g[i];
		}
		LL ans=0;
//		cout << N << endl;
		REP(i, N) {
			int j, n;
//			cout << i << ' ' << g[i] << endl;
			if (g[i]>k) {
				nt[i]=-1; c[i]=0; continue;
			}
			for(j=i, n=N, c[i]=0; n>0 && c[i]+g[j]<=k; ++j, --n) {
				c[i]+=g[j];
//				cout << c[i] << ' ' << j << endl;
			}
			nt[i]=j % N;
//			cout << nt[i] << endl;
		}
		/*
		REP(i, N)
			cout << nt[i] << endl;
		*/
		memset(dfn, 0, sizeof(dfn));
		int x=0, cnt=0;
		if (x==-1) {
			cout << ans << endl; continue;
		}
		while (R && !dfn[x]) {
			sq[++cnt]=x;
			dfn[x]=cnt;
			ans+=c[x];
			x=nt[x];
			if (x==-1) break;
			--R;
		}	
		
		if (R<=0 || x==-1) {
			cout << ans << endl; continue;
		}
		int r=cnt-dfn[x]+1;
		LL tmp=0;
		for(int i=dfn[x]; i<=cnt; ++i)
			tmp+=c[sq[i]];
		ans+=tmp*(R/r);
//		cout << r << endl;
		tmp=0;
		r=R%r;
		for(int i=dfn[x], j=0; j<r; ++i, ++j)
			ans+=c[sq[i]];
		cout << ans << endl;
	}
	return 0;
}
