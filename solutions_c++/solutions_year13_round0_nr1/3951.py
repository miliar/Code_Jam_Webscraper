#include<iostream>

using namespace std;

string whoWon(char board[4][4]){
	int i,j;
	int ocnt,xcnt;
	bool t,e = false;
	for(i = 0;i < 4;i++){
		t = false;
		ocnt = xcnt = 0;
		for(j = 0;j < 4;j++){
			if(board[i][j] == 'O')
				ocnt++;
			else if(board[i][j] == 'X')
				xcnt++;
			else if(board[i][j] == 'T')
				t = true;
			else{ 
				e = true;
				//cout<<board[i][j]<<"--"<<i<<"--"<<j;
			}
		}
		if(xcnt==4 || (xcnt==3 && t))
			return "X won";
		else if(ocnt==4 || (ocnt==3 && t))
			return "O won";
	}
	for(j = 0;j < 4;j++){
		t = false;
		ocnt = xcnt = 0;
		for(i = 0;i < 4;i++){
			if(board[i][j] == 'O')
				ocnt++;
			else if(board[i][j] == 'X')
				xcnt++;
			else if(board[i][j] == 'T')
				t = true;
		}
		if(xcnt==4 || (xcnt==3 && t))
			return "X won";
		else if(ocnt==4 || (ocnt==3 && t))
			return "O won";
	}
	t = false;
	ocnt = xcnt = 0;
	for(i=0;i<4;i++){
		if(board[i][i]=='O')
			ocnt++;
		else if(board[i][i]=='X')
			xcnt++;
		else if(board[i][i]=='T')
			t = true;
	}
	if(xcnt==4 || (xcnt==3 && t))
		return "X won";
	else if(ocnt==4 || (ocnt==3 && t))
		return "O won";
		
	t = false;
	ocnt = xcnt = 0;
	for(i=0;i<4;i++){
		if(board[i][3-i]=='O')
			ocnt++;
		else if(board[i][3-i]=='X')
			xcnt++;
		else if(board[i][3-i]=='T')
			t = true;
	}
	if(xcnt==4 || (xcnt==3 && t))
		return "X won";
	else if(ocnt==4 || (ocnt==3 && t))
		return "O won";
	
	if(e)
		return "Game has not completed" ;
	else
		return "Draw";
}

int main(){
	int n,i,j,k;
	char b[4][4];
	string l;
	cin>>n;
	for(i=0;i<n;i++){
		for(j=0;j<4;j++){
			cin>>l;
			for(k=0;k<4;k++){
				b[j][k] = l[k];
			}
		}
		cout<<"Case #"<<i+1<<": "+whoWon(b)<<endl;
	}
	return 0;
}