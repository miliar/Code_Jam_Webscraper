#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<utility>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;

#define MP make_pair
#define PB push_back
#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)
#define min(a, b) ((a)<(b)?(a):(b))

const int MAXK=200;

int a[MAXK][MAXK];
int k, n;

bool check(int x, int y)
{
	for(int L=y-1, R=y+1; L>0 && R<=n; --L, ++R) {
		for(int i=1; i<=n; ++i) {
//			cout << a[i][L] << ' ' << a[i][R] << endl;
			if (a[i][L]==-1 || a[i][R]==-1) continue;
			else
			if (a[i][L]!=a[i][R]) return false;
		}
	}
	for(int U=x-1, D=x+1; U>0 && D<=n; ++D, --U) 
		for(int i=1; i<=n; ++i) {
//			cout << a[U][i] << ' ' << a[D][i] << endl;
			if (a[U][i]==-1 || a[D][i]==-1) continue;
			else
			if (a[U][i]!=a[D][i]) return false;
	}
	return true;
}	

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int T, tt=0;
	scanf("%d", &T);
	for(; tt<T; ) {
		scanf("%d", &k);
		memset(a, -1, sizeof(a));
		for(int i=1, st=k; i<=k; ++i, --st)
			for(int j=1, y=st; j<=i; ++j, y+=2) {
				scanf("%d", &a[i][y]);
		}
		for(int i=k+1, t=k-1, st=2; t>0; ++i, --t, ++st) 
			for(int j=1, y=st; j<=t; ++j, y+=2)
				scanf("%d", &a[i][y]);
		n=k*2-1;
		int ans=10000000;
		int tot=k*k;
		for(int i=1; i<=k*2-1; ++i) {
			for(int j=1; j<=k*2-1; ++j) {
//				cout << a[i][j];
				int len=abs(k-j)+abs(i-k)+k;
				if (check(i, j)) {
//					cout << i << ' ' << j << endl;
					ans=min(ans, len*len-tot);		
				}
			}
//			cout << endl;
		}
		printf("Case #%d: %d\n", ++tt, ans);
	}
	return 0;
}
