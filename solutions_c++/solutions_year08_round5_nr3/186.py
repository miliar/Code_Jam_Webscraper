#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <cassert>
#include <numeric>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

int t, n, m, b[20][20];
int mem[20][1<<10];

int count(int x) {
	int res=0;
	while (x) res+=x%2, x/=2;
	return res;
}

int solve(int x, int mask) {
	if (x>=n) {
		return 0;
	}
	int &res=mem[x][mask];
	if (res!=-1) return res;
	res=0;
	REP(i,1<<m) {
		bool ok=true;
		REP(j,m) {
			if (i&(1<<j)) {
				if (b[x][j]==1) ok=false;
				if (j-1>=0 && mask&(1<<(j-1))) ok=false;
				if (j-1>=0 && i&(1<<(j-1))) ok=false;
				if (j+1<m && mask&(1<<(j+1))) ok=false;
				if (j+1<m && i&(1<<(j+1))) ok=false;
			}
		}
		if (ok) {
			res=max(res,count(i)+solve(x+1,i));
		}
	}
	return res;
}
				
int main()
{
	scanf("%d", &t);
	FOR(tCase,1,t) {
		scanf("%d %d", &n, &m);
		CLR(b,0); CLR(mem,-1);
		REP(i,n) {
			char tmp[20];
			scanf("%s", tmp);
			REP(j,m) if (tmp[j]=='x') b[i][j]=1;
		}
		printf("Case #%d: %d\n", tCase, solve(0,0));
	}
	return 0;
}
