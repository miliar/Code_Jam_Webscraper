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
int L, P, c;
int f(int a){
	if (a==0) return 0;
	return 1 + f(a/2);
}
void init()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
}
void sol(){	
	cin >> T;
	FOR(t,1,T){
		cin >> L >> P >> c;
		int h = 0;
		int next = (P+c-1)/c;
		while (next>L){
			h++;
			next = (next+c-1)/c;
		}
		int ans = f(h);
		WR("Case #%d: %d\n",t,ans);
	}
}
int main()
{
	init();
	sol();
	return 0;
}