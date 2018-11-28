#pragma comment(linker,"/STACK:64000000")

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <sstream>
#include <cmath>
#include <ctime>

#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);++i)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);--i)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define LL long long
using namespace std;
typedef vector<int>    VI;
typedef vector<string> VS;
typedef pair<int ,int> PAR;

#define ass(s) \
if (!(s)) { \
	int ln = __LINE__;\
	char * s1 = __FILE__, * s2 = __FUNCTION__;\
	fprintf(stderr,"\n(!)ASSERTION FAILED: %s, %s, %d.\n",s1,s2,ln);\
	printf("\n(!)ASSERTION FAILED: %s, %s, %d.\n",s1,s2,ln);\
	cout.flush(), cerr.flush();\
	exit(1);\
}


int T;
int n, k;
int m[200][200];
bool graf[200][200];
bool flag[200];
int ord[200], col[200];
int be, en;
bool f[200];
void init()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	RE("%d",&T);
}
int SIGN(int a){
	if (a<0) return -1;
	if (a>0) return 1;
	return 0;
}
void bfs(int num){
	ass(flag[num]==false);
	flag[ord[be=en=1]=num]=true;
	col[num] = 1;
	while(be<=en){
		int cur = ord[be++], i;
		CLR(f);
		FOR(i,0,n-1) if (graf[cur][i]) f[col[i]] = true;
		FOR(i,1,n+1) if (!f[i]) {
			col[cur] = i;
			break;
		}
		FOR(i,0,n-1) if (graf[cur][i] && !flag[i]){
			ord[++en] = i;
			flag[i] = true;
		}
	}
}
int cli(int mask){
	int i, j;
	VI v;
	FOR(i,0,n-1) if (mask & (1<<i)) v.PB(i);
	FOR(i,0,SZ(v)-1) FOR(j,i+1,SZ(v)-1) if (!graf[v[i]][v[j]]) return 0;
	return SZ(v);
}
void sol(){
	int t, i, j, w;
	FOR(t,1,T){
		RE("%d %d",&n,&k);
		CLR(graf);
		FOR(i,0,n-1) FOR(j,0,k-1) RE("%d",&m[i][j]);
		FOR(i,0,n-1) FOR(j,i+1,n-1) {
			bool ok = false;
			FOR(w,0,k-1){
				if (m[i][w]==m[j][w]) {
					ok = true;
					break;
				}
			}
			if (!ok){
				FOR(w,1,k-1){
					int h = SIGN(m[i][w-1]-m[j][w-1]) * SIGN(m[i][w]-m[j][w]);
					ass(h!=0);
					if (h<0){
						ok = true;
						break;
					}
				}
			}
			graf[i][j] = graf[j][i] = ok;
		}
		int ans = 0;
		/*CLR(flag);
		CLR(col);
		DFOR(i,n-1,0) if (!flag[i]) bfs(i);
		FOR(i,0,n-1) {
			ass(col[i]>0);
			ans = max(ans,col[i]);
			//WR(" %d",col[i]);
		}*/
		FOR(i,0,(1<<n)-1){
			ans = max(ans,cli(i));
		}
		WR("Case #%d: %d",t,ans);
		if (t<T) WR("\n");
	}
}
int main()
{
	init();
	sol();
	return 0;
}