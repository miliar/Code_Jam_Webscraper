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

const int MAXN = 100 + 10;
int n;
char gp[MAXN][MAXN];
double op[MAXN], opp[MAXN], oppp[MAXN];
double c[MAXN][MAXN];

int main(){
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas; cin >>cas;
	FOR(tc, cas){
		printf("Case #%d:\n", tc + 1);
		cin >> n;
		FOR(i, n){
			scanf("%s", gp[i]);
			int tot = 0, win = 0;
			FOR(j, n){
				if(gp[i][j] =='1'){
					win ++;
				}
				if(gp[i][j] != '.'){
					tot ++;
				}
			}
			op[i] = 1.0 * win / tot;
			//cout << op[i] << endl;
		}
		FOR(i, n){
			FOR(j, n){
				int tot = 0, win = 0;
				c[i][j] = 0;
				FOR(k, n){
					if(k == j)continue;
					if(gp[i][k] =='1'){
						win ++;
					}
					if(gp[i][k] != '.'){
						tot ++;
					}
				}
				c[i][j] = 1.0 * win / tot;
			}
		}
		FOR(i, n){
			int tot = 0;
			double win = 0;
			FOR(j, n){
				if(gp[i][j] != '.'){
					tot ++;
					win += c[j][i];
				}
			}
			opp[i] = win / tot;
			//cout << opp[i] << endl;
		}

		FOR(i ,n){
			int tot = 0;
			double win = 0;
			FOR(j, n){
				if(gp[i][j] != '.'){
					tot ++;
					win += opp[j];
				}
			}
			oppp[i] = win / tot;
		}
		FOR(i, n){
			double ans = 0.25 * op[i] + 0.50 * opp[i] + 0.25 * oppp[i];
			//cout << ans << endl;
			printf("%.9lf\n", ans);
		}
	}
}