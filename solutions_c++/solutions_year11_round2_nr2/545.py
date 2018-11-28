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

const double eps = 1e-10;
const int MAXN = 200 + 10;
int C, D;
PII gp[MAXN];
int cmp(double x){
	return x < -eps ? -1 : x > eps;
}

bool check(double t){
	double l = -1e20;
	FOR(i, C){
		FOR(j, gp[i].Y){
			double cur = gp[i].X;
			l += D;
			if(cmp(l - cur) <= 0){
				l = max(l, cur - t);
			}else{
				if(cmp(cur + t - l) < 0)return false;
			}
		}
	}
	return true;
}
int main(){
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas; cin >>cas;
	FOR(tc, cas){
		cin >> C >> D;
		FOR(i, C){
			cin >> gp[i].X >> gp[i].Y;
		}
		double l = 0, r = 1e10, ans;
		while(l + eps < r){
			double md = (l + r) / 2.0;
			if(check(md)){
				ans = md;
				r = md;
			}else l = md;
		}
		printf("Case #%d: %.9lf\n", tc + 1, ans);
		
	}
}