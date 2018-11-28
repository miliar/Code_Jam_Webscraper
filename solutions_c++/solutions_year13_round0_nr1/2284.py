#include <string>
#include <vector>
#include <map>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <time.h>
using namespace std;
char s[10][10];
int pan(int x,int y,int dx,int dy,char c){
	int i;
	for(i=1;i<=4;i++){
		if(s[x][y]!=c&&s[x][y]!='T') return(0);
		x=x+dx;
		y=y+dy;
	}
	return(1);
}
int win(char c){
	int i,j;
	for(i=1;i<=4;i++){
		if(pan(i,1,0,1,c)) return(1);
	}
	for(i=1;i<=4;i++){
		if(pan(1,i,1,0,c)) return(1);
	}
	if(pan(1,1,1,1,c)) return(1);
	if(pan(4,1,-1,1,c)) return(1);
	return(0);
}
void check(){
	int i,j,dot=0;
	for(i=1;i<=4;i++){
		for(j=1;j<=4;j++){
			if(s[i][j]=='.') dot++;
		}
	}
	if(win('X')){
		printf("X won\n");
	}
	else if(win('O')){
		printf("O won\n");
	}
	else{
		if(dot>0) printf("Game has not completed\n");
		else printf("Draw\n");
	}
}
int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("a.out","w",stdout);
    int T,i,j;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
		for(j=1;j<=4;j++) scanf("%s",&s[j][1]);
		printf("Case #%d: ",i);
		check();
	}
}
