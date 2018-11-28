//#pragma comment(linker, "/STACK:134217728,134217728") /*128Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
#include <algorithm>
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;

/*--in common define-----*/
#define N  100010
#define E  100010
#define ll long long
const ll PRIME =999983;
const ll MOD   =1000000007;
const ll MULTI =1000000007;
/*--end in common define-*/

/*--in common use--------*/
#define cube(x) ((x)*(x)*(x))
#define sq(x)     ((x)*(x))
#define all(x)     x.begin(),x.end()
#define lp(a,s,t)   int (a)=(s);(a)<(t);(a)++
#define lpe(a,s,t) int (a)=(s);(a)<=(t);(a)++
inline bool isodd(int x){return x&1;}
inline bool isodd(ll x) {return x&1;}
/*--end in common use----*/


char g[5][5];

bool checkX()
{
	for(int i=0;i<4;i++){
		int cnt=0;
		for(int j=0;j<4;j++){
			if(g[i][j]=='X' || g[i][j]=='T') cnt++;
		}
		if(cnt==4) return true;
	}
	for(int j=0;j<4;j++){
		int cnt=0;
		for(int i=0;i<4;i++){
			if(g[i][j]=='X' || g[i][j]=='T') cnt++;
		}
		if(cnt==4) return true;
	}
	int cnt=0;
	for(int i=0;i<4;i++)
		if(g[i][i]=='X' || g[i][i]=='T') cnt++;
	if(cnt==4) return true;
	cnt=0;
	for(int i=0;i<4;i++)
		if(g[i][3-i]=='X' || g[i][3-i]=='T') cnt++;
	if(cnt==4) return true;
	return false;
}
bool checkO()
{
	for(int i=0;i<4;i++){
		int cnt=0;
		for(int j=0;j<4;j++){
			if(g[i][j]=='O' || g[i][j]=='T') cnt++;
		}
		if(cnt==4) return true;
	}
	for(int j=0;j<4;j++){
		int cnt=0;
		for(int i=0;i<4;i++){
			if(g[i][j]=='O' || g[i][j]=='T') cnt++;
		}
		if(cnt==4) return true;
	}
	int cnt=0;
	for(int i=0;i<4;i++)
		if(g[i][i]=='O' || g[i][i]=='T') cnt++;
	if(cnt==4) return true;
	cnt=0;
	for(int i=0;i<4;i++)
		if(g[i][3-i]=='O' || g[i][3-i]=='T') cnt++;
	if(cnt==4) return true;
	return false;
}
bool checkDraw()
{
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(g[i][j]=='.') return false;
		}
	}
	return true;
}

int main() {

	int re,Case=1;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&re);
	while(re--){
		for(int i=0;i<4;i++)
			scanf("%s",g[i]);
		printf("Case #%d: ",Case++);
		if(checkX()) puts("X won");
		else if(checkO()) puts("O won");
		else if(checkDraw()) puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}