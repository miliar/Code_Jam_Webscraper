#include<iostream>
#include<fstream>
using namespace std;
void main(){
	int T;
	char tic[5][5];
	ifstream cin("A-large.in");
	ofstream cout("2013_gcj_qr_A.out");
	cin >> T;
	for(int i = 0; i < T; i++){
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++)
				cin >> tic[j][k];
		bool finish = false;
		cout << "Case #"<<i+1<<": ";
		//row
		int countdot = 0;
		for(int j = 0; j < 4; j++){
			int countX=0,countO=0;
			for(int k = 0; k < 4; k++){
				if(tic[j][k] == 'T'){countX++;countO++;}
				else if(tic[j][k] == 'X')countX++;
				else if(tic[j][k] == 'O')countO++;
				else if(tic[j][k] == '.')countdot++;
			}
			if(countX == 4){cout << "X won"<<endl;finish = true;break;}
			else if(countO == 4){cout << "O won"<<endl;finish = true;break;}
		}
		if(finish)continue;
		//column
		
		for(int k = 0; k < 4; k++){
			int countX=0,countO=0;
			for(int j = 0; j < 4; j++){
				if(tic[j][k] == 'T'){countX++;countO++;}
				else if(tic[j][k] == 'X')countX++;
				else if(tic[j][k] == 'O')countO++;
				else if(tic[j][k] == '.')countdot++;
			}
			
			if(countX == 4){cout << "X won"<<endl;finish = true;break;}
			else if(countO == 4){cout << "O won"<<endl;finish = true;break;}
		}
		if(finish)continue;
		//diagonal
		int countX=0,countO=0;
		for(int j = 0; j < 4; j++){
			if(tic[j][j] == 'T'){countX++;countO++;}
			else if(tic[j][j] == 'X')countX++;
			else if(tic[j][j] == 'O')countO++;
			else if(tic[j][j] == '.')countdot++;
		}
		if(countX == 4){cout << "X won"<<endl;continue;}
		else if(countO == 4){cout << "O won"<<endl;continue;}

		countX=0;countO=0;
		for(int j = 3; j >= 0; j--){
			if(tic[3-j][j] == 'T'){countX++;countO++;}
			else if(tic[3-j][j] == 'X')countX++;
			else if(tic[3-j][j] == 'O')countO++;
			else if(tic[3-j][j] == '.')countdot++;
		}
		if(countX == 4){cout << "X won"<<endl;continue;}
		else if(countO == 4){cout << "O won"<<endl;continue;}
		//draw
		if(countdot == 0)cout << "Draw" << endl;
		else cout << "Game has not completed"<<endl;
	}
	system("pause");
}