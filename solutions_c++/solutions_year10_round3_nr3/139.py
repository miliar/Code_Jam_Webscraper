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


int T;
int w[512][512];
int n, m;
map<int,int> ans;
void init()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
}
int f(int x, int y){
	if (w[x][y]==2) return 0;
	int ans = 1;
	FOR(i,2,n+m){
		if (x+i-1>=n || y+i-1>=m) break;
		int pre = w[x][y+i-2];
		bool ok = true;
		FOR(j,x,x+i-1) {
			pre = 1 - pre;
			if (w[j][y+i-1]!=pre) ok = false;
		}
		DFOR(j,y+i-2,y) {
			pre = 1 - pre;
			if (w[x+i-1][j]!=pre) ok = false;
		}
		if (ok) ans = i;
		else break;
	}
	return ans;
}
void des(int x, int y, int s){
	FOR(i,x,x+s-1) FOR(j,y,y+s-1) {
		ass(w[i][j]!=2);
		ass(0<=i && i<n && 0<=j && j<m);
		w[i][j] = 2;
	}
}
void sol(){	
	cin >> T;
	FOR(t,1,T){
		cin >> n >> m;
		string s;
		FOR(i,0,n-1) {
			cin >> s;
			ass(SZ(s)==m/4);
			FA(j,s){
				int h;
				if ('0'<=s[j] && s[j]<='9') h = s[j] - '0';
				else if ('A'<=s[j] && s[j]<='F') h = s[j] - 'A' + 10;
				else ass(false);
				FOR(k,0,3) {
					w[i][j*4 + 3 - k] = h&1;
					h>>=1;
				}
			}
		}
		ans.clear();
		while (1){
			int ma = 0, x = -1, y = -1;
			FOR(i,0,n-1) FOR(j,0,m-1) {
				int h = f(i,j);
				if (h>ma) {
					ma = h;
					x = i;
					y = j;
				}
			}
			if (ma==0) break;
			des(x,y,ma);
			ans[ma]++;
		}
		FOR(i,0,n-1) FOR(j,0,m-1) ass(w[i][j]==2);
		vector<PAR> Ans(ans.rbegin(),ans.rend());
		WR("Case #%d: %d\n",t,SZ(Ans));
		FA(i,Ans) WR("%d %d\n",Ans[i].FI,Ans[i].SE);
	}
}
int main()
{
	init();
	sol();
	return 0;
}