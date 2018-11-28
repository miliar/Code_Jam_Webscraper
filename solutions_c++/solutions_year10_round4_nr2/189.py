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

int P;
int m[1<<11], price[1<<11];
int f[1<<11][11];
bool known[1<<11][11];

int calc(int match, int d, int rd, int L, int R)
{
	int &best=f[match][d];
	if (known[match][d]) return best;
	known[match][d]=true;
	bool end=true;
	for(int i=L; i<=R; ++i) {
		if (m[i]+rd+d<P) return best=-1;
		if (m[i]+d<P) end=false;
	}
	if (end) return best=0;
	best=INT_MAX;
	int mid=(L+R+1)/2, left, right, tmp;
	left=calc(match*2, d, rd-1, L, mid-1);
	right=calc(match*2+1, d, rd-1, mid, R);
	tmp=left+right;
	if (left!=-1 && right!=-1) best=tmp;
	left=calc(match*2, d+1, rd-1, L, mid-1);
	right=calc(match*2+1, d+1, rd-1, mid, R);
	tmp=left+right+price[match];
	if (tmp<best) best=tmp;
	return best;
}

int main()
{
	freopen("b2.in", "rt", stdin);
	freopen("b-large.out", "wt", stdout);
	int T, tt=0;
	scanf("%d", &T);
	for(; tt<T; ) {
		scanf("%d", &P);
		for(int i=0; i<(1<<P); ++i) scanf("%d", &m[i]);
		int x;
		for(int i=P-1; i>=0; --i) {
			for(int j=(1<<i); j<(1<<(i+1)); ++j)
				scanf("%d", &price[j]);
//			f[i][0]=0;
		}
		memset(known, 0, sizeof(known));
		printf("Case #%d: %d\n", ++tt, calc(1, 0, P, 0, (1<<P)-1));
	}
	return 0;
}
