#include<iostream>

using namespace std;

const int BS = 4;

char board[BS][BS];
int T;

int main() {
	cin>>T;
	for(int ti=0;ti<T;ti++) {
		bool xwon = 0, owon = 0, isfull = 1;
		for(int i=0;i<BS;i++)
			for(int j=0;j<BS;j++) {
				cin>>board[i][j];
				if(board[i][j]=='.')
					isfull = 0;
			}
		//row
		for(int i=0;i<BS;i++) {
			if( (board[i][0]=='X' || board[i][0]=='T') && (board[i][1]=='X' || board[i][1]=='T')
				&& (board[i][2]=='X' || board[i][2]=='T') && (board[i][3]=='X' || board[i][3]=='T') )
				xwon = 1;
			if( (board[i][0]=='O' || board[i][0]=='T') && (board[i][1]=='O' || board[i][1]=='T')
				&& (board[i][2]=='O' || board[i][2]=='T') && (board[i][3]=='O' || board[i][3]=='T') )
				owon = 1;
		}
		//col
		for(int j=0;j<BS;j++) {
			if( (board[0][j]=='X' || board[0][j]=='T') && (board[1][j]=='X' || board[1][j]=='T')
				&& (board[2][j]=='X' || board[2][j]=='T') && (board[3][j]=='X' || board[3][j]=='T') )
				xwon = 1;
			if( (board[0][j]=='O' || board[0][j]=='T') && (board[1][j]=='O' || board[1][j]=='T')
				&& (board[2][j]=='O' || board[2][j]=='T') && (board[3][j]=='O' || board[3][j]=='T') )
				owon = 1;
		}
		//diag
		if( (board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T')
			&& (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T') )
			xwon = 1;
		if( (board[0][0]=='O' || board[0][1]=='T') && (board[1][1]=='O' || board[1][1]=='T')
			&& (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T') )
			owon = 1;
		//alt diag
		if( (board[0][3]=='X' || board[0][3]=='T') && (board[1][2]=='X' || board[1][2]=='T')
			&& (board[2][1]=='X' || board[2][1]=='T') && (board[3][0]=='X' || board[3][0]=='T') )
			xwon = 1;
		if( (board[0][3]=='O' || board[0][3]=='T') && (board[1][2]=='O' || board[1][2]=='T')
			&& (board[2][1]=='O' || board[2][1]=='T') && (board[3][0]=='O' || board[3][0]=='T') )
			owon = 1;
		cout<<"Case #"<<ti+1<<": ";
		if(xwon)		cout<<"X won"<<endl;
		else if(owon)	cout<<"O won"<<endl;
		else if(isfull)	cout<<"Draw"<<endl;
		else 			cout<<"Game has not completed"<<endl;
	}
	return 0;
}