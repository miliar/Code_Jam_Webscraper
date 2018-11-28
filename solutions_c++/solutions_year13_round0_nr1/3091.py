/*Code By Aquariuslt*/  
#include<iostream>  
#include<string>  
#include<algorithm>  
#include<queue>  
#include<stack>  
#include<vector>  
#include<deque>  
#include<set>  
#include<list>  
#include<map>  
#include<iterator>  
#include<numeric>  
#include<memory>  
#include<utility>  
#include<stdio.h>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)    
#define FORD(i,a,b) for(int i=(a);i<=(b);i++)    
#define REP(i,b) FOR(i,0,b)    
  
typedef long long ll;  
using namespace std;  

int chess[4][4];

void inputchess(){
	char ch;
	REP(i,4){
		REP(j,4){
			cin>>ch;
			if(ch=='X')chess[i][j]=1;
			else if(ch=='O')chess[i][j]=2;
			else if(ch=='T')chess[i][j]=3;
			else chess[i][j]=0;
		}
	}
}

int Ocheck(){
	REP(i,4){
		if(chess[i][0]*chess[i][1]*chess[i][2]*chess[i][3]==16||chess[i][0]*chess[i][1]*chess[i][2]*chess[i][3]==24)return 1;
		if(chess[0][i]*chess[1][i]*chess[2][i]*chess[3][i]==16||chess[0][i]*chess[1][i]*chess[2][i]*chess[3][i]==24)return 1;
	}
	if(chess[0][0]*chess[1][1]*chess[2][2]*chess[3][3]==16||chess[0][0]*chess[1][1]*chess[2][2]*chess[3][3]==24)return 1;
	if(chess[0][3]*chess[1][2]*chess[2][1]*chess[3][0]==16||chess[0][3]*chess[1][2]*chess[2][1]*chess[3][0]==24)return 1;
	return 0;
}

int Xcheck(){
	REP(i,4){
		if(chess[i][0]*chess[i][1]*chess[i][2]*chess[i][3]==1||chess[i][0]*chess[i][1]*chess[i][2]*chess[i][3]==3)return 1;
		if(chess[0][i]*chess[1][i]*chess[2][i]*chess[3][i]==1||chess[0][i]*chess[1][i]*chess[2][i]*chess[3][i]==3)return 1;
	}
	if(chess[0][0]*chess[1][1]*chess[2][2]*chess[3][3]==1||chess[0][0]*chess[1][1]*chess[2][2]*chess[3][3]==3)return 1;
	if(chess[0][3]*chess[1][2]*chess[2][1]*chess[3][0]==1||chess[0][3]*chess[1][2]*chess[2][1]*chess[3][0]==3)return 1;
	return 0;
}
//Complete Check
int Ccheck(){
	REP(i,4){
		REP(j,4){
			if(chess[i][j]==0)return 0;
		}
	}
	return 1;
}
int main(){  
	freopen("A-large.in.","r",stdin);
	freopen("loutput.txt","w",stdout);
    int t;
    cin>>t;
    FORD(ti,1,t){
    	inputchess();
    	printf("Case #%d: ",ti);
    	if(Ocheck())printf("O won\n");
    	else if(Xcheck())printf("X won\n");
    	else if(Ccheck())printf("Draw\n");
    	else printf("Game has not completed\n");
    }
    return 0;    
}
