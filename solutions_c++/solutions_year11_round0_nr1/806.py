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

const int MAXN = 100 + 10;
int n;
vector<PII> gp;
 
int main(int argc, char *argv[]){
	freopen("A-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas; cin >> cas;
	FOR(tc, cas){
		cin >> n;
		gp.clear();
		FOR(i, n){
			string id; int pos;
			cin >> id >> pos;
			if(id == "O")gp.PB(MP(0, pos));
			else gp.PB(MP(1, pos));
		}
		int o = 1, b = 1, os = 0, bs = 0, ans = 0;
		FOR(i, gp.size()){
			if(gp[i].X == 0){
				int cnt = max(0, abs(gp[i].Y - o) - os);
				o = gp[i].Y;
				ans += cnt + 1;
				os = 0;
				bs += cnt + 1;
			} else {
				int cnt = max(0, abs(gp[i].Y - b) - bs);
				b = gp[i].Y;
				ans += cnt + 1;
				bs = 0;
				os += cnt + 1;
			}
		}
		printf("Case #%d: %d\n", tc + 1, ans);
	}
}
