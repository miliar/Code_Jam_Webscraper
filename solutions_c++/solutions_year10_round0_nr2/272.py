#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define REP(i, n) for(int i=0, __n=(n); i<__n; ++i)

const int MAXN = 1001;

int a[MAXN], b[MAXN];
int N;

int gcd(int x, int y)
{
	if (y==0) return x;
	return gcd(y, x%y);
}

int main()
{
	freopen("B-small.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
	int tt, T;
	for(tt=0, scanf("%d", &T); tt<T;) {
		printf("Case #%d: ", ++tt);
		scanf("%d", &N);
		REP(i, N) scanf("%d", &a[i]);
		REP(i, N-1) {
			b[i]=abs(a[i+1]-a[i]);
		}
		int g=b[0];
		for(int i=1; i<N-1; ++i) {
			if (g<b[i]) {
				int tmp=g; g=b[i]; b[i]=tmp;
			}
			int x=gcd(g, b[i]);
			g=x;
		}
		if ((a[0]%g)==0) cout << 0 << endl;
		else 
		cout << g-(a[0]%g) << endl;
	}
	return 0;
}
