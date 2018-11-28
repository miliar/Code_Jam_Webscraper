#include <iostream>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(a,b,c) for(int a=b;a<=c;a++)

int n,m,a;
int X1,Y1,X2,Y2;
bool f;

void solve(){
	FOR(x1,0,n)FOR(y1,0,m)FOR(x2,0,n)FOR(y2,0,m)if( x1*y2-x2*y1 == a ){
		f = true;
		X1 = x1;
		Y1 = y1;
		X2 = x2;
		Y2 = y2;
		return;
	}	
}

int main(){
	int d;
	scanf("%d",&d);
	REP(test,d){
		scanf("%d %d %d",&n,&m,&a);
		f = false;
		solve();
		if( f )printf("Case #%d: 0 0 %d %d %d %d\n",test+1,X1,Y1,X2,Y2);
		else printf("Case #%d: IMPOSSIBLE\n",test+1);
	}
	return 0;
}
