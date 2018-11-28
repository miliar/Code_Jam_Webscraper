//Bismillahir Rahmanir Rahim
//#pragma warning(disable:4786)
//#pragma comment(linker,"/STACK:514850816")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <climits>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
using namespace std;
char in[10][10];

bool XOCheck(char c){
	int i,j;
	bool f;
	//row check
	for(i=0;i<4;i++){
		f = 1;
		for(j=0;j<4;j++)if(in[i][j]!=c && in[i][j]!='T'){f=0;break;}
		if(f)return true;
	}
	//column check
	for(i=0;i<4;i++){
		f = 1;
		for(j=0;j<4;j++)if(in[j][i]!=c && in[j][i]!='T'){f=0;break;}
		if(f)return true;
	}
	//diagonal check
	f = 1;
	for(i=0;i<4;i++){
		if(in[i][i]!=c && in[i][i]!='T'){f=0;break;}
	}
	if(f)return true;
	f = 1;
	for(i=0;i<4;i++){
		if(in[i][3-i]!=c && in[i][3-i]!='T'){f=0;break;}
	}
	if(f)return true;
	return false;
}

bool DrawCheck(){
	int i,j;
	for(i=0;i<4;i++)for(j=0;j<4;j++)if(in[i][j]=='.')return false;
	return true;
}

int main(){
	freopen("G:\\Coding\ 4\ Contest\\contests\\codejam13\\A-large.in","r",stdin);
	freopen("G:\\Coding\ 4\ Contest\\contests\\codejam13\\A-large.out","w",stdout);
	int t, cas, i;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		for(i=0;i<4;i++)scanf("%s",in[i]);
		printf("Case #%d: ",cas);
		if(XOCheck('X'))puts("X won");
		else if(XOCheck('O'))puts("O won");
		else if(DrawCheck())puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}