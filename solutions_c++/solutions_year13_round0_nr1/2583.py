#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#define maxl 1000000000
using namespace std;

char g[10][10];

bool check(char ch){
	int i,j;
	for(i=1;i<=4;++i){
		for(j=1;j<=4;++j)if(g[i][j]!=ch && g[i][j]!='T')break;
		//cout<<j<<endl;
		if(j>4)return true;
		for(j=1;j<=4;++j)if(g[j][i]!=ch && g[j][i]!='T')break;
		if(j>4)return true;
	}
	for(j=1;j<=4;++j)if(g[j][j]!=ch && g[j][j]!='T')break;
	if(j>4)return true;
	for(j=1;j<=4;++j)if(g[j][5-j]!=ch && g[j][5-j]!='T')break;
	if(j>4)return true;
	return false;
}

bool checkDraw(){
	int i,j;
	for(i=1;i<=4;++i)
		for(j=1;j<=4;++j)if(g[i][j]=='.')return false;
		
	return true;
}


void solve(){
	int i;
	for(i=1;i<=4;++i)scanf("%s",g[i]+1);
	if(check('X'))printf("X won\n");else if(check('O'))printf("O won\n");else if(checkDraw())printf("Draw\n");else printf("Game has not completed\n");
}

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}