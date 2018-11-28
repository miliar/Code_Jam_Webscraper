#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <ctime>
#include <set>
#include <list>
using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
#define PATH(x) "c:\\Users\\Topsky\\Desktop\\ACM\\"#x
#define CLR(x,a) memset(x,a,sizeof(x))
#define out(x) cerr<<#x<<" "<<x
#define FORN(i, u) for(int i = head[u]; i != -1; i = next[i])
#define FOR(i,n) for(int i=0;i<(n);i++)
#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define DEP(i,a,b) for(int i=(a);i>=(b);i--)
#define FORIT(it,c) for(__typeof((c).begin())it=(c).begin();it!=(c).end();it++)
#define ALL(a) a.begin(),a.end()
#define MP make_pair
#define PB push_back
#define LB(x) (x&(-x))
#define L(x) (x<<1)
#define R(x) ((x<<1)+1)
#define oo 0x3f3f3f3f
#define X first
#define Y second

const int MAXN = 100000 + 10;

LL n, pd, pg;

bool check(int l, int r){
	REP(i, l ,r){
		if((i * pg) % 100 == 0)return true;
	}
	return false;
}

bool solve(){
	if(pg == 0 && pd != 0 || pg == 100 && pd != 100){
		return false;
	}
	REP(i, 1, n){
		if(i * pd % 100 == 0){
			int j = i;
			return true;
			while(1){
				if(j * pg % 100 == 0)return true;
				j ++;
			}
		}
	}
	return false;
}
int main(){
	int cas; cin >> cas;
	FOR(tc, cas){
		printf("Case #%d: ", tc + 1);
		cin >> n >> pd >> pg;
		if(solve())puts("Possible");
		else puts("Broken");
	}
}