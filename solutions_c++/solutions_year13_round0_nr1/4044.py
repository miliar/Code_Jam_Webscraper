#include<iostream>
using namespace std;
int T,x,o,t,dot,win; //win: 1 - X, 2 - O
char board[4][4];
int main(){
	cin>>T;
	for(int q=1;q<=T;q++){
		cin>>board[0]>>board[1]>>board[2]>>board[3];
		//check horizontal lines
		dot=0;
		win=0;
		for(int i=0;i<4;i++){ //four lines
			x=0;
			o=0;
			t=0;
			for(int j=0;j<4;j++){ //four symbols
				if(board[i][j]=='X')x++;
				else if(board[i][j]=='O')o++;
				else if(board[i][j]=='T')t++;
				else dot++;
			}
			if((x+t)==4){
				win=1;
				break;
			}
			else if((o+t)==4){
				win=2;
				break;
			}
		
		}
		//check vertical lines
		if(win==0){
			for(int i=0;i<4;i++){ //four lines
				x=0;
				o=0;
				t=0;
				for(int j=0;j<4;j++){ //four symbols
					if(board[j][i]=='X')x++;
					else if(board[j][i]=='O')o++;
					else if(board[j][i]=='T')t++;		
				}
				if((x+t)==4){
					win=1;
					break;
				}
				else if((o+t)==4){
					win=2;
					break;
				}
			}
		}
		//check diagonals
		if(win==0){
			//left upper corner - right lower corner
			x=0;
			o=0;
			t=0;
			for(int i=0;i<4;i++){
				if(board[i][i]=='X')x++;
				else if(board[i][i]=='O')o++;
				else if(board[i][i]=='T')t++;
			}
			if((x+t)==4){
				win=1;
				}
			else if((o+t)==4){
				win=2;
			}
			//left lower corner - right upper corner
			x=0;
			o=0;
			t=0;
			for(int i=0;i<4;i++){
				if(board[3-i][i]=='X')x++;
				else if(board[3-i][i]=='O')o++;
				else if(board[3-i][i]=='T')t++;
			}
			if((x+t)==4){
				win=1;
				}
			else if((o+t)==4){
				win=2;
			}
			
		}
		if(win==1)cout<<"Case #"<<q<<": X won\n";
		else if(win==2)cout<<"Case #"<<q<<": O won\n";
		else{
			if(dot==0)cout<<"Case #"<<q<<": Draw\n";
			else cout<<"Case #"<<q<<": Game has not completed\n";
		}
	}
cout<<endl;
return 0;
}
