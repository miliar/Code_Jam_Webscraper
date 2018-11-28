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
#include <list>
#include <set>
using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
#define PATH(x) "c:\\Users\\Topsky\\Desktop\\ACM\\"#x
#define CLR(x,a) memset(x,a,sizeof(x))
#define out(x) cerr<<#x<<" "<<x
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

const int MAXN = 100000, MAXM = 1000 + 10;
int n, m;

double dp[MAXN];
int main(){
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas; cin >> cas;
	FOR(tc, cas){
		double ans = 0;
		cin >> n;
		FOR(i, n){
			int v;
			cin >> v;
			if(v != i + 1) ans += 1;
		}
		printf("Case #%d: %.9lf\n",tc + 1, ans);
	}
}