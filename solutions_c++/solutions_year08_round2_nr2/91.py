#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b) x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) c.begin(), c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for (VAR(i,c.begin()); i != c.end(); ++i)
#define PB push_back
#define ST first
#define ND second

const int MAXN = 1000000+1;
bool p[MAXN];

void sieve() {
	fill_n(p,MAXN,1);
	p[0] = p[1] = 0;
	for (int i = 2; i*i < MAXN; ++i) if (p[i])
		for (int j = i*i; j < MAXN; j += i)
			p[j] = 0;
}
int rk[MAXN], rp[MAXN];
void ms(int i) { rp[i] = i; rk[i] = 0; }
int fs(int i) { if (rp[i] == i) return i; return rp[i] = fs(rp[i]); }
void ls(int i, int j) { if (rk[i] < rk[j]) rp[i] = rp[j]; else { rp[j] = rp[i]; if (rk[i] == rk[j]) rk[i]++; } }
void us(int i, int j) { int r1 = fs(i), r2 = fs(j); if (r1 != r2) ls(r1,r2); }

int dr[MAXN];
int main()
{
	int c;
	scanf("%d",&c);
	int pc = c;
	sieve();
	while (c--) {
		LL a,b,P;
		scanf("%lld%lld%lld",&a,&b,&P);
		REP(i,b-a+1) ms(i);
		REP(i,MAXN) if (p[i] && i >= P) { 
			LL st = ((a+i-1)/i+1)*i;
			for(int j = st-a; j < b-a+1; j += i) us(j,j-i);
		}
		fill_n(dr,b-a+1,0);
		int res = 0;
		REP(i,b-a+1) if (dr[fs(i)] == 0) { dr[fs(i)] = 1; res++; }
		printf("Case #%d: %d\n",pc-c,res);
	}
	return 0;
}
