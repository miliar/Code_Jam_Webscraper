#include <iostream>
#include <fstream>
using namespace std;

char Grid[4][4];


int main()
{
	ifstream cin("A-large.in");
	ofstream cout("sevag_tic_tac_large.out");

	int T;
	cin>>T;

	for (int t=1; t<=T; t++){
		bool complete=true;
		bool won=false;

		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				cin>>Grid[i][j];
				if (Grid[i][j]=='.')
					complete=false;
			}
		}

		//for X
		for (int i=0; i<4 && !won; i++){
			bool same=true;
			for (int j=0; j<4; j++){
				if (Grid[i][j]!='X' && Grid[i][j]!='T'){
					same=false;
					break;
				}
			}
			if (same){
				cout<<"Case #"<<t<<": X won"<<endl;
				won=true;
				break;
			}
		}

		for (int j=0; j<4 && !won; j++){
			bool same=true;
			for (int i=0; i<4; i++){
				if (Grid[i][j]!='X' && Grid[i][j]!='T'){
					same=false;
					break;
				}
			}
			if (same){
				cout<<"Case #"<<t<<": X won"<<endl;
				won=true;
				break;
			}
		}

		if (!won){
			bool same=true;
			for (int i=0; i<4; i++){
				if (Grid[i][i]!='X' && Grid[i][i]!='T'){
					same=false;
					break;
				}
			}
			if (same){
					cout<<"Case #"<<t<<": X won"<<endl;
					won=true;
			}
		}

		if (!won){
			bool same=true;
			for (int i=0; i<4; i++){
				if (Grid[i][3-i]!='X' && Grid[i][3-i]!='T'){
					same=false;
					break;
				}
			}
			if (same){
					cout<<"Case #"<<t<<": X won"<<endl;
					won=true;
			}
		}

		//for O
		for (int i=0; i<4 && !won; i++){
			bool same=true;
			for (int j=0; j<4; j++){
				if (Grid[i][j]!='O' && Grid[i][j]!='T'){
					same=false;
					break;
				}
			}
			if (same){
				cout<<"Case #"<<t<<": O won"<<endl;
				won=true;
				break;
			}
		}

		for (int j=0; j<4 && !won; j++){
			bool same=true;
			for (int i=0; i<4; i++){
				if (Grid[i][j]!='O' && Grid[i][j]!='T'){
					same=false;
					break;
				}
			}
			if (same){
				cout<<"Case #"<<t<<": O won"<<endl;
				won=true;
				break;
			}
		}

		if (!won){
			bool same=true;
			for (int i=0; i<4 && !won; i++){
				if (Grid[i][i]!='O' && Grid[i][i]!='T'){
					same=false;
					break;
				}
			}
			if (same){
					cout<<"Case #"<<t<<": O won"<<endl;
					won=true;
			}
		}

		if (!won){
			bool same=true;
			for (int i=0; i<4 && !won; i++){
				if (Grid[i][3-i]!='O' && Grid[i][3-i]!='T'){
					same=false;
					break;
				}
			}
			if (same){
					cout<<"Case #"<<t<<": O won"<<endl;
					won=true;
			}
		}

		if (!won){
		if (complete)
			cout<<"Case #"<<t<<": Draw"<<endl;
		else
			cout<<"Case #"<<t<<": Game has not completed"<<endl;
		}

	}

	return 0;
}