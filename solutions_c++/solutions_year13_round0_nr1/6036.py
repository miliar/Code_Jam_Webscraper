#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cassert>
#include<vector>
#include<string>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<bitset>
#include<cstdio>
#include<cmath>
#include<climits>
#include<ctime>
#include<string>
#include<fstream>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#define ip(x) scanf("%d",&x)
#define ipLL(x) scanf("%lld",&x)
#define ForInc(var,beg,end) for(int var=beg;var<=end;++var)
#define advForInc(var,beg,end,inc) for(int var=beg;var<=end;var+=inc)
#define ForDec(var,end,beg) for(int var=end;var>=beg;--var)
#define ipArray(arr,size) ForInc(i,0,size-1) ip(arr[i]);
#define print(x) printf("%d\n",x)
#define printLL(x) printf("%lld\n",x)
#define ss(str) scanf("%s",str)
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#include<ctime>
template<typename T> T gcd(T a, T b) { return (b == 0) ? abs(a) : gcd(b, a % b); }
template<typename T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> inline T mod(T a, T b) { return (a % b + b) % b; }
template<typename T> inline T sqr(T x) { return x * x; }
typedef long long LL;
using namespace std;



/* Main Code starts here :) */
char board[4][4];
bool checkWin(char player){
	ForInc(i,0,3){
		bool f=true;
		ForInc(j,0,3)if(!(board[i][j]==player || board[i][j]=='T')){f=false;break;}
		if(f==true)return true;
	}
	ForInc(j,0,3){
		bool f=true;
		ForInc(i,0,3)if(!(board[i][j]==player || board[i][j]=='T')){f=false;break;}
		if(f==true)return true;
	}
	bool f=true;
	for(int i=0,j=0;i<=3;++i,++j)if(!(board[i][j]==player || board[i][j]=='T')){f=false;break;}
	if(f==true)return true;
	f=true;
	for(int i=0,j=3;i<=3;i++,j--)if(!(board[i][j]==player || board[i][j]=='T')){f=false;break;}
	if(f)return true;
	
	return false;
}
bool checkdot(){
	bool f=false;
	ForInc(i,0,3)
		ForInc(j,0,3)
			if(board[i][j]=='.')return true;
	return false;		
}
int main(){
	
	int T;ip(T);
	ForInc(cs,1,T){
		ForInc(i,0,3)ForInc(j,0,3)cin>>board[i][j];
		printf("Case #%d: ",cs);
		if(checkWin('X'))printf("X won");
		else if(checkWin('O'))printf("O won");
		else if(!checkdot())printf("Draw");
		else printf("Game has not completed");
		printf("\n");
	}
	
	return 0;
}


