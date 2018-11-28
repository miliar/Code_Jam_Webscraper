#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;
#define N 10000
#define MOD 1000000007
#define inf 1<<28
#define LL long long
#define abs(a) (a)<0?(-a):(a)
#define CLR(a) memset((a),0,sizeof((a)))
#define FRIN freopen("A-large.in","r",stdin)
#define FROUT freopen("Alarge.txt","w",stdout)
int rw[4][4],col[4][4],dig[2][4];
inline int find(char c){
	if(c=='X') return 0;
	else if(c=='O') return 1;
	else if(c=='T') return 2;
	else return 3;
}
bool find_win(int c){
	int i;
	for(i=0;i<4;i++){
		if(rw[i][c]==4||(rw[i][c]==3&&rw[i][2]==1)) return true;
		else if(col[i][c]==4||(col[i][c]==3&&col[i][2]==1)) return true;
	}
	if(dig[0][c]==4||(dig[0][c]==3&&dig[0][2]==1)) return true;
	else if(dig[1][c]==4||(dig[1][c]==3&&dig[1][2]==1)) return true;
	else return false;
}  
bool find_draw(){
	int i;
	for(i=0;i<4;i++){
		if(rw[i][3]) return false;
		else if(col[i][3]) return false;
	}
	return true;
}  
int main(){
	FRIN;
	FROUT;
	int tst,k,i,j,p;
	char brd[5][5];
	scanf("%d",&tst);
	for(k=1;k<=tst;k++){
		for(i=0;i<4;i++) {
		  scanf("%s",brd[i]);
		}
		CLR(rw);
		CLR(col);
		CLR(dig);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				p=find(brd[i][j]);
				rw[i][p]++;
				p=find(brd[j][i]);
				col[i][p]++;
			}
			p=find(brd[i][i]);
			dig[0][p]++;
			if(i==0) p=find(brd[i][3]);
			else if(i==1) p=find(brd[i][2]);
			else if(i==2) p=find(brd[i][1]);
			else p=find(brd[i][0]);
			dig[1][p]++;
		}
		printf("Case #%d: ",k);
		if(find_win(0)) printf("X won\n");
		else if(find_win(1)) printf("O won\n");
		else if(!find_draw()) printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;	
}
