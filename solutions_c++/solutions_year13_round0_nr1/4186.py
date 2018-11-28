#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<vector>
#include<iostream>
#include<map>

using namespace std;

int game[4][4];
map<char,int> m;
int hasPoint;
void solve33(){
	int whoWon=0;
	//try solve X
	for(int i = 0;i<4;i++){
		for(int j = 0;j<4;j++){
			if(game[i][j]!=m['X'] && game[i][j]!=m['T'])
				break;
			if(j==3)
				whoWon=1;
		}
	}
	for(int i = 0;i<4;i++){
		for(int j = 0;j<4;j++){
			if(game[j][i]!=m['X'] && game[j][i]!=m['T'])
				break;
			if(j==3)
				whoWon=1;
		}
	}
	for(int i = 0;i<4;i++){
		if(game[i][i]!=m['X'] && game[i][i]!=m['T'])
			break;
		if(i==3)
			whoWon=1;
	}
	for(int i = 0;i<4;i++){
		if(game[i][3-i]!=m['X'] && game[i][3-i]!=m['T'])
			break;
		if(i==3)
			whoWon=1;
	}
	//try solve O
	for(int i = 0;i<4;i++){
		for(int j = 0;j<4;j++){
			if(game[i][j]!=m['O'] && game[i][j]!=m['T'])
				break;
			if(j==3)
				whoWon=2;
		}
	}
	for(int i = 0;i<4;i++){
		for(int j = 0;j<4;j++){
			if(game[j][i]!=m['O'] && game[j][i]!=m['T'])
				break;
			if(j==3)
				whoWon=2;
		}
	}
	for(int i = 0;i<4;i++){
		if(game[i][i]!=m['O'] && game[i][i]!=m['T'])
			break;
		if(i==3)
			whoWon=2;
	}
	for(int i = 0;i<4;i++){
		if(game[i][3-i]!=m['O'] && game[i][3-i]!=m['T'])
			break;
		if(i==3)
			whoWon=2;
	}
	
	if(!whoWon && hasPoint){
		printf("Game has not completed\n");
	}else if(!whoWon && !hasPoint){
		printf("Draw\n");
	}else{
		printf("%c won\n",whoWon==1 ? 'X' : 'O');
	}
}

int main(){

	m['.']=0; m['X']=1;
	m['O']=2; m['T']=3;

	int tt;
	scanf("%d",&tt);
	for(int kk = 1;kk<=tt;kk++){
		printf("Case #%d: ",kk);
		hasPoint=0;
		
		string line;
		for(int i=0;i<4;i++){
			cin>>line;
			for(int j=0;j<4;j++){
				game[i][j]=m[line[j]];
				if(line[j]=='.') hasPoint=1;
			}
		}
		
		solve33();
	}

	return 0;
}
