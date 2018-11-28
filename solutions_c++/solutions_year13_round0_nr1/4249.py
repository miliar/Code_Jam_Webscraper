using namespace std;
#include <iostream>
#include <string>
#include <vector>
int status(string S) {
	int x, len=4, lenX=0, lenO=0;
	for(x=0;x<4;x++) {
		if(S[x]=='.')
			return 0;
		if(S[x]=='X')
			lenX++;
		if(S[x]=='O')
			lenO++;
		if(S[x]=='T')
			len--;
	}
	if(len==lenX)
		return 1;
	if(len==lenO)
		return 2;
	return 0;
}
bool filled(vector<string> Board) {
	int x,y;
	for(x=0;x<4;x++) {
		for(y=0;y<4;y++) {
			if(Board[x][y]=='.') {
				return false;
			}
		}
	}
	return true;
}
int main() {
	int T,x,y;
	string S;
	cin>>T;
	for (x=0;x<T;x++) {
		getline(cin,S);
		vector <string> Board;
		for (y=0;y<4;y++) {
			getline(cin,S);
			Board.push_back(S);
		}
		bool decision = false;
		int winner = 0;
		if(filled(Board)) {
			winner = 3;
		}
		S="...."; S[0]=Board[0][0]; S[1]=Board[1][1]; S[2]=Board[2][2]; S[3]=Board[3][3];
		if(status(S) && !decision) {
			winner = status(S);
			decision = true;
		}
		S="...."; S[0]=Board[0][3]; S[1]=Board[1][2]; S[2]=Board[2][1]; S[3]=Board[3][0];
		if(status(S) && !decision) {
			winner = status(S);
			decision = true;
		}
		for(y=0;y<4 && !decision;y++) {
			if(status(Board[y]) && !decision) {
				winner = status(Board[y]);
				decision = true;
			}
		}
		for(y=0;y<4 && !decision;y++) {
			S="...."; S[0]=Board[0][y]; S[1]=Board[1][y]; S[2]=Board[2][y]; S[3]=Board[3][y];
			if(status(S) && !decision) {
				winner = status(S);
				decision = true;
			}
		}
		cout<<"Case #"<<x+1<<": ";
		switch(winner) {
			case 0: cout<<"Game has not completed\n"; break;
			case 1: cout<<"X won\n"; break;
			case 2: cout<<"O won\n"; break;
			case 3: cout<<"Draw\n"; break;
		}
	}
	return 0;
}
