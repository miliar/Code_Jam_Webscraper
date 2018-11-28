#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int test, h = 0;
	cin>>test;
	while(test > h++){
		int flagxxx = 0, flagooo = 0, flagdottt = 0;
		char tictac[4][5];
		cin>>tictac[0]>>tictac[1]>>tictac[2]>>tictac[3];
		for(int i = 0; i < 4; ++i){
			if((tictac[i][0] == 'X' || tictac[i][0] == 'T') && (tictac[i][1] == 'X' || tictac[i][1] == 'T') && (tictac[i][2] == 'X' || tictac[i][2] == 'T') && (tictac[i][3] == 'X' || tictac[i][3] == 'T')){
			
				flagxxx = 1;
				printf("Case # %d : X won\n", h);
				//cout<<"Case #"<<h<<": X won\n";
				break;
			}else if((tictac[i][0] == 'O' || tictac[i][0] == 'T') && (tictac[i][1] == 'O' || tictac[i][1] == 'T') && (tictac[i][2] == 'O' || tictac[i][2] == 'T') && (tictac[i][3] == 'O' || tictac[i][3] == 'T')){
			
				flagooo = 1;
				printf("Case # %d : X won\n", h);
				//cout<<"Case #"<<h<<": O won\n";
				break;
			}
			else if(tictac[i][0] == '.' || tictac[i][1] == '.' || tictac[i][2] == '.' || tictac[i][3] == '.'){
			
				flagdottt = 1;
				break;
			}
		}
		if(flagxxx == 0 && flagooo == 0)
		for(int i = 0; i < 4; ++i){
			if((tictac[0][i] == 'X' || tictac[0][i] == 'T') && (tictac[1][i] == 'X' || tictac[1][i] == 'T') && (tictac[2][i] == 'X' || tictac[2][i] =='T') && (tictac[3][i]== 'X' || tictac[3][i] == 'T')){
				flagxxx = 1;
				printf("Case # %d : X won\n", h);
				//cout<<"Case #"<<h<<": X won\n";
				break;
			}
			if((tictac[0][i] == 'O' || tictac[0][i] == 'T') && (tictac[1][i] == 'O' || tictac[1][i] == 'T') && (tictac[2][i] == 'O' || tictac[2][i] =='T') && (tictac[3][i]== 'O' || tictac[3][i] == 'T')){
				flagooo = 1;
				printf("Case # %d : O won\n", h);
				//cout<<"Case #"<<h<<": O won\n";
				break;
			}
			
		}
		if(flagxxx == 0 && flagooo == 0){
		if((tictac[0][0] == 'O' || tictac[0][0] == 'T') && (tictac[1][1] == 'O' || tictac[1][1] == 'T') && (tictac[2][2] == 'O' || tictac[2][2] =='T') && (tictac[3][3]== 'O' || tictac[3][3] == 'T')){
			flagooo = 1;
			printf("Case # %d : O won\n", h); //cout<<"Case #"<<h<<": O won\n";
		}
		else if((tictac[0][0] == 'X' || tictac[0][0] == 'T') && (tictac[1][1] == 'X' || tictac[1][1] == 'T') && (tictac[2][2] == 'X' || tictac[2][2] =='T') && (tictac[3][3]== 'X' || tictac[3][3] == 'T')){
			flagxxx = 1;
			printf("Case # %d : X won\n", h); //cout<<"Case #"<<h<<": X won\n";
		}else if((tictac[3][0] == 'X' || tictac[3][0] == 'T') && (tictac[2][1] == 'X' || tictac[2][1] == 'T') && (tictac[1][2] == 'X' || tictac[1][2] =='T') && (tictac[0][3]== 'X' || tictac[0][3] == 'T')){
			flagxxx = 1;
			printf("Case # %d : X won\n", h); //cout<<"Case #"<<h<<": X won\n";
		}else if((tictac[3][0] == 'O' || tictac[3][0] == 'T') && (tictac[2][1] == 'O' || tictac[2][1] == 'T') && (tictac[1][2] == 'O' || tictac[1][2] =='T') && (tictac[0][3]== 'O' || tictac[0][3] == 'T')){
			flagooo = 1;
			printf("Case # %d : O won\n", h); //<"Case #"<<h<<": O won\n";
		}
		}
		if(flagooo == 0 && flagxxx == 0){
			if(flagdottt == 1) cout<<"Case #"<<h<<": Game has not completed\n";
			else printf("Case # %d : Draw\n", h);
		}
		
	}

	return 0;
}
