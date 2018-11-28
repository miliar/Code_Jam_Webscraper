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
char s[100];
void init()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	RE("%d",&T);
}
map<VI, int> was;
VI ord[50000];
int be, en;
bool ok(VI v){
	int i;
	FA(i,v) if (v[i]>i) return false;
	return true;
}
int bfs(VI v){
	int n = SZ(v), i;
	ord[be=en=1] = v;
	was.clear();
	was[v] = 0;
	while (be<=en){
		VI cur = ord[be++];
		int cd = was[cur];
		if (ok(cur)) return cd;
		FOR(i,1,n-1) {
			swap(cur[i],cur[i-1]);
			if (was.find(cur)==was.end()){
				ord[++en] = cur;
				was[cur] = cd+1;
			}
			swap(cur[i],cur[i-1]);
		}
	}
	ass(false);
	return -1;
}
void sol(){
	int i, j;
	int t;
	int n;
	bool wass = false;
	FOR(t,1,T){
		RE("%d",&n);
		VI v(n);
		gets(s);
		FOR(i,0,n-1) {
			gets(s);
			ass(s[n-1]=='0' || s[n-1]=='1');
			int h = 0;
			DFOR(j,n-1,0) if (s[j]=='1'){
				h = j;
				break;
			}
			v[i] = h;
		}
		int ans = 0;
		FOR(i,0,n-1){
			int tt = -1;
			FOR(j,i,n-1) if (v[j]<=i) {
				tt = j;
				break;
			}
			ass(tt!=-1);
			DFOR(j,tt-1,i) {
				swap(v[j],v[j+1]);
				ans++;
			}
		}
		ass(ok(v));
		if (wass) WR("\n");
		wass = true;
		WR("Case #%d: %d",t,ans);
	}
}
int main()
{
	init();
	sol();
	return 0;
}