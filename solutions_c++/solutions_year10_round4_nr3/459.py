#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <ctime>
#include <memory.h>

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,Be,En) for(int (i)=(Be);(i)<=(En);++(i))
#define DFOR(i,Be,En) for(int (i)=(Be);(i)>=(En);--(i))
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a,0,sizeof(a))

#define LL  long long
#define VI  vector<int>
#define PAR pair<int ,int> 

using namespace std;
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}



int T, n;
bool graf[1024][1024];
PAR p1[1024], p2[1024];
bool flag[1024];
int m[1024];
int cc = 0;
bool over(PAR a1, PAR a2, PAR b1, PAR b2){
	int x1 = max(a1.FI,b1.FI);
	int x2 = min(a2.FI,b2.FI);
	int y1 = max(a1.SE,b1.SE);
	int y2 = min(a2.SE,b2.SE);
	if (x2>x1 && y2>=y1) return true;
	if (y2>y1 && x2>=x1) return true;
	if (x1==x2 && y1==y2){
		if (make_pair(a2.FI,a1.SE)==make_pair(b1.FI,b2.SE)) return true;
		swap(a1,b1);swap(a2,b2);
		if (make_pair(a2.FI,a1.SE)==make_pair(b1.FI,b2.SE)) return true;
	}
	return false;
}
void dfs(int num){
	flag[num] = true;
	m[cc++] = num;
	FOR(i,0,n-1) if (!flag[i] && graf[num][i]) dfs(i);
}
void init()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
}
void sol(){	
	cin >> T;
	int INF = 100000000;
	FOR(t,1,T){
		RE("%d",&n);
		//WR("test %d\n",t);
		//cout.flush();
		FOR(i,0,n-1) {
			RE("%d %d %d %d",&p1[i].FI,&p1[i].SE,&p2[i].FI,&p2[i].SE);
			p2[i].first++;
			p2[i].second++;
		}
		FOR(i,0,n-1) FOR(j,0,n-1) graf[i][j] = over(p1[i],p2[i],p1[j],p2[j]);
		FOR(i,0,n-1) {
			FOR(j,0,n-1) {
				ass(graf[i][j] == graf[j][i]);
				//WR(" %d",graf[i][j]);
			}
			//WR("\n");
		}
		CLR(flag);
		int ans = -INF;
		FOR(I,0,n-1) if (!flag[I]){
			cc = 0;
			dfs(I);
			int x = -INF;
			int y = -INF;
			FOR(i,0,cc-1) {
				x = max(x, p2[m[i]].FI);
				y = max(y, p2[m[i]].SE);
			}
			int ma = -INF;
			FOR(i,0,cc-1) ma = max(ma, x-p1[m[i]].FI + y - p1[m[i]].SE - 1);
			ans = max(ans, ma);
		}
		WR("Case #%d: %d\n",t,ans);
	}
}
int main()
{
	init();
	sol();
	return 0;
}