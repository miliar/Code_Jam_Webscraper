#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
using namespace std;



bool dotFound;
char board[4][4],winner;

int check(){

	int X[4][4]={0},O[4][4]={0},xC,oC,j,i;
	bool hasD=false;


	//Check Right

	for(j=0;j<4;j++){
		oC=0;
		xC=0;
		for(i=0;i<4;i++){
			if(board[j][i]=='X'){
				X[j][i]++;
				xC++;
			}else if(board[j][i]=='O'){
				O[j][i]++;
				oC++;
			}else if(board[j][i]=='T'){
				X[j][i]++;
				xC++;
				O[j][i]++;
				oC++;
			}else{
				dotFound=true;
			}
		}

		if(xC==4){
			return 1;
		}else if(oC==4){
			return 2;
		}
	}

	//Check Down
	for(i=0;i<4;i++){
		if(X[0][i]+X[1][i]+X[2][i]+X[3][i] == 4){
			return 1;
		}else if(O[0][i]+O[1][i]+O[2][i]+O[3][i] == 4){
			return 2;
		}
	}


	if(X[0][0]+X[1][1]+X[2][2]+X[3][3]==4){
		return 1;
	}else if(O[0][0]+O[1][1]+O[2][2]+O[3][3] == 4){
		return 2;
	}


	if(X[0][3]+X[1][2]+X[2][1]+X[3][0]==4){
		return 1;
	}else if(O[0][3]+O[1][2]+O[2][1]+O[3][0] == 4){
		return 2;
	}


	return 0;


}



void ini(){

	int j;

	dotFound=false;

	for(j=0;j<4;j++){
		scanf("%s",board[j]);
	}

}

int main(){

	int cases,i,res;

	freopen("1.in","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&cases);

	for(i=1;i<=cases;i++){
		ini();
		res=check();

		if(res==0){
			if(dotFound){
				printf("Case #%d: Game has not completed\n",i);
			}else{
				printf("Case #%d: Draw\n",i);
			}
		}else if(res==1){
			printf("Case #%d: X won\n",i);
		}else{
			printf("Case #%d: O won\n",i);
		}
	}

	return 0;

}