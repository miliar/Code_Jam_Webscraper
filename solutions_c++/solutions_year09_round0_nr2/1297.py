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

int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};


int T, N, M;
int cc;
int m[400][400];
int H[400][400];
bool flag[100];
int let[100];
void init()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	RE("%d",&T);
}
void sol(){
	int t, i, j;
	FOR(t,1,T){
		RE("%d %d",&N,&M);
		vector< pair <int , PAR> > v(N*M);
		FOR(i,0,N-1) FOR(j,0,M-1) {
			RE("%d",&H[i][j]);
			v[i*M + j] = make_pair(H[i][j], make_pair(i, j));
		}
		sort(v.begin(), v.end());
		cc = 0;
		FA(i, v){
			int x = v[i].SE.FI, y = v[i].SE.SE;
			int ind = -1, mi = 1000000000;
			FOR(j,0,3) {
				int hx = x + dx[j], hy  = y + dy[j];
				if (hx>=0 && hx<N && hy>=0 && hy<M) if (H[hx][hy]<H[x][y] && H[hx][hy]<mi) mi = H[hx][hy], ind = m[hx][hy];
			}
			if (ind==-1)	m[x][y] = cc++;
			else m[x][y] = ind;
		}
		int cc2 = 0;
		CLR(flag);
		FOR(i,0,N-1) FOR(j,0,M-1) if (!flag[m[i][j]]) {
			flag[m[i][j]]=true;
			let[m[i][j]] = cc2 + 'a';
			cc2++;
		}
		if (t>1) WR("\n");
		WR("Case #%d:", t);
		FOR(i,0,N-1) {
			WR("\n%c", let[m[i][0]]);
			FOR(j,1,M-1) WR(" %c", let[m[i][j]]);
		}
	}
}
int main()
{
	init();
	sol();
	return 0;
}