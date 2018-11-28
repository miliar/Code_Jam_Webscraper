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

const int MAXN = (1 << 21), MAXM = 1000 + 10;
int n, m, ans, sum;
int dp[2][MAXN], gp[MAXM];

int main(int argc, char *argv[]){
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas; cin >> cas;
	FOR(tc, cas){
		cin >> n;
		ans = sum = 0;
		FOR(i, n){
			cin >> gp[i];
			ans ^= gp[i];
			sum += gp[i];
		}
		int pre = 0, cur, mm = 0;
		CLR(dp, oo);
		FOR(i, n){
			cur= pre ^ 1;
			FOR(j, mm + 1)dp[cur][j] = dp[pre][j];
			dp[cur][gp[i]] = min(dp[cur][gp[i]], gp[i]);
			int tm = max(gp[i], mm);
			FOR(j, mm + 1){
				tm = max(tm, j ^ gp[i]);
				if(dp[pre][j] != oo)dp[cur][j ^ gp[i]] = min(dp[cur][j ^ gp[i]], dp[pre][j] + gp[i]);
			}
			mm = max(tm, mm);
			pre = cur;
		}
		int res = -1;
		FOR(i, mm + 1){
			//cout << dp[cur][i] << endl;
			if(i == (i ^ ans)){
				if(dp[cur][i] == 0 || dp[cur][i] == sum)continue;
				res = max( res, sum - dp[cur][i] ); 
			}
		}
		printf("Case #%d: ", tc + 1);
		if(res == -1)puts("NO");
		else printf("%d\n", res);
	}
}
