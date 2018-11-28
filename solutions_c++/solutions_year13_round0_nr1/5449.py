#include<iostream>

using namespace std;
int main()
{
	int t, h = 0;
	cin>>t;
	while(t > h++){
		int flagx = 0, flago = 0, flagdot = 0;
		char tic[4][5];
		cin>>tic[0]>>tic[1]>>tic[2]>>tic[3];
		for(int i = 0; i < 4; ++i){
			if((tic[i][0] == 'X' || tic[i][0] == 'T') && (tic[i][1] == 'X' || tic[i][1] == 'T') && (tic[i][2] == 'X' || tic[i][2] == 'T') && (tic[i][3] == 'X' || tic[i][3] == 'T')){
			
				flagx = 1;
				cout<<"Case #"<<h<<": X won\n";
				break;
			}else if((tic[i][0] == 'O' || tic[i][0] == 'T') && (tic[i][1] == 'O' || tic[i][1] == 'T') && (tic[i][2] == 'O' || tic[i][2] == 'T') && (tic[i][3] == 'O' || tic[i][3] == 'T')){
			
				flago = 1;
				cout<<"Case #"<<h<<": O won\n";
				break;
			}
			else if(tic[i][0] == '.' || tic[i][1] == '.' || tic[i][2] == '.' || tic[i][3] == '.'){
			
				flagdot = 1;
				break;
			}
		}
		if(flagx == 0 && flago == 0)
		for(int i = 0; i < 4; ++i){
			if((tic[0][i] == 'X' || tic[0][i] == 'T') && (tic[1][i] == 'X' || tic[1][i] == 'T') && (tic[2][i] == 'X' || tic[2][i] =='T') && (tic[3][i]== 'X' || tic[3][i] == 'T')){
				flagx = 1;
				cout<<"Case #"<<h<<": X won\n";
				break;
			}
			if((tic[0][i] == 'O' || tic[0][i] == 'T') && (tic[1][i] == 'O' || tic[1][i] == 'T') && (tic[2][i] == 'O' || tic[2][i] =='T') && (tic[3][i]== 'O' || tic[3][i] == 'T')){
				flago = 1;
				cout<<"Case #"<<h<<": O won\n";
				break;
			}
			
		}
		if(flagx == 0 && flago == 0){
		if((tic[0][0] == 'O' || tic[0][0] == 'T') && (tic[1][1] == 'O' || tic[1][1] == 'T') && (tic[2][2] == 'O' || tic[2][2] =='T') && (tic[3][3]== 'O' || tic[3][3] == 'T')){
			flago = 1;
			cout<<"Case #"<<h<<": O won\n";
		}
		else if((tic[0][0] == 'X' || tic[0][0] == 'T') && (tic[1][1] == 'X' || tic[1][1] == 'T') && (tic[2][2] == 'X' || tic[2][2] =='T') && (tic[3][3]== 'X' || tic[3][3] == 'T')){
			flagx = 1;
			cout<<"Case #"<<h<<": X won\n";
		}else if((tic[3][0] == 'X' || tic[3][0] == 'T') && (tic[2][1] == 'X' || tic[2][1] == 'T') && (tic[1][2] == 'X' || tic[1][2] =='T') && (tic[0][3]== 'X' || tic[0][3] == 'T')){
			flagx = 1;
			cout<<"Case #"<<h<<": X won\n";
		}else if((tic[3][0] == 'O' || tic[3][0] == 'T') && (tic[2][1] == 'O' || tic[2][1] == 'T') && (tic[1][2] == 'O' || tic[1][2] =='T') && (tic[0][3]== 'O' || tic[0][3] == 'T')){
			flago = 1;
			cout<<"Case #"<<h<<": O won\n";
		}
		}
		if(flago == 0 && flagx == 0){
			if(flagdot == 1) cout<<"Case #"<<h<<": Game has not completed\n";
			else cout<<"Case #"<<h<<": Draw\n";
		}
		
	}

	return 0;
}
