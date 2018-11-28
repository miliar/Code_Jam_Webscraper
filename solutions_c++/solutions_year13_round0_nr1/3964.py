#include<iostream>
#include<strings.h>
#include<fstream>
using namespace std;
class player{
	public:
	int d1,d2,h,v;
	player(){
		d1=0; d2=0; h=0; v=0;
	}
};

main(){
	int T;
	scanf("%d",&T);
	fstream mf;
	mf.open("D:/seijee.txt");
	for (int c=1; c<=T; c++){
		string board[4];
		player X;
		player Y;
		char winner='T';
		for (int i=0; i<4;i++){
			cin>>board[i];
			
			X.h=0; Y.h=0;
			for (int j=0; j<4; j++){
				X.h++;
				Y.h++;
				if (board[i][j]=='X'){
					Y.h=0;
				}else if (board[i][j]=='O'){
					X.h=0;
				}else if (board[i][j]=='.'){
					X.h=0;
					Y.h=0;
					if (winner=='T'){
						winner='.';
					}
				}
			}
			if (X.h==4){
				winner = 'X';
				//cout<<winner<<endl;
			}else if(Y.h==4){
				winner = 'O';
				//cout<<winner<<endl;
			}
		}
		
		//vertical
		for (int i=0; i<4; i++){
			X.v=0; Y.v=0;
			for (int j=0; j<4; j++){
				X.v++;
				Y.v++;
				if (board[j][i]=='X'){
					Y.v=0;
				}else if (board[j][i]=='O'){
					X.v=0;
				}else if (board[j][i]=='.'){
					X.v=0;
					Y.v=0;
					if (winner=='T'){
						winner='.';
					}
				}
			}
			if (X.v==4){
				winner = 'X';
				//cout<<winner<<endl;
			}else if(Y.v==4){
				winner = 'O';
				//cout<<winner<<endl;
			}
		}
		//diag
		for (int j=0; j<4; j++){
			X.d1++;X.d2++;
			Y.d1++;Y.d2++;
			
			//d1
			if (board[j][j]=='X'){
				Y.d1=0;
			}else if (board[j][j]=='O'){
				X.d1=0;
			}else if (board[j][j]=='.'){
				X.d1=0;
				Y.d1=0;
				if (winner=='T'){
					winner='.';
				}
			}
			//d2
			if (board[j][3-j]=='X'){
				Y.d2=0;
			}else if (board[j][3-j]=='O'){
				X.d2=0;
			}else if (board[j][3-j]=='.'){
				X.d2=0;
				Y.d2=0;
				if (winner=='T'){
					winner='.';
				}
			}
		}
		if (X.d1==4 || X.d2==4){
			winner = 'X';
			//cout<<winner<<endl;
		}else if(Y.d1==4 || Y.d2==4){
			winner = 'O';
			//cout<<winner<<endl;
		}
		
		if (winner=='T'){
			mf<<"Case #"<<c<<": Draw\n";
		}else if (winner=='.'){
			mf<<"Case #"<<c<<": Game has not completed\n";
		}else{
			mf<<"Case #"<<c<<": "<<winner<<" won\n";
		}
	}
	mf.close();
}
