#include <iostream>
#include <fstream>

using namespace std;

enum Status {UNDEFINED, X_WON, O_WON, DRAW, NOT_COMPLETED};

int main() {
	int nTestCases;
	ifstream in("A-large.in");
	ofstream out("out");
	in>>nTestCases;
	for(int t=0; t<nTestCases; t++) {
		string board[4];
		Status status=UNDEFINED;
		for(int r=0; r<4; r++)
			in>>board[r];
		//Row
		for(int r=0; r<4 && status==UNDEFINED; r++) {
			int n=0;
			for(int c=0; c<4; c++)
				if(board[r][c]=='T' || board[r][c]=='X')
					n++;
			if(n==4) {
				status=X_WON;
				break;
			}
			n=0;
			for(int c=0; c<4; c++)
				if(board[r][c]=='T' || board[r][c]=='O')
					n++;
			if(n==4) {
				status=O_WON;
				break;
			}
		}
		//Column
		for(int c=0; c<4 && status==UNDEFINED; c++) {
			int n=0;
			for(int r=0; r<4; r++)
				if(board[r][c]=='T' || board[r][c]=='X')
					n++;
			if(n==4) {
				status=X_WON;
				break;
			}
			n=0;
			for(int r=0; r<4; r++)
				if(board[r][c]=='T' || board[r][c]=='O')
					n++;
			if(n==4) {
				status=O_WON;
				break;
			}
		}
		if(status==UNDEFINED) {
			int n=0;
			for(int c=0, r=0; c<4; c++, r++)
				if(board[r][c]=='T' || board[r][c]=='X')
					n++;
			if(n==4)
				status=X_WON;
			n=0;
		}
		if(status==UNDEFINED) {
			int n=0;
			for(int c=0, r=0; c<4; c++, r++)
				if(board[r][c]=='T' || board[r][c]=='O')
					n++;
			if(n==4)
				status=O_WON;
		}
		if(status==UNDEFINED) {
			int n=0;
			for(int c=0, r=3; c<4; c++, r--)
				if(board[r][c]=='T' || board[r][c]=='X')
					n++;
			if(n==4)
				status=X_WON;
		}
		if(status==UNDEFINED) {
			int n=0;
			for(int c=0, r=3; c<4; c++, r--)
				if(board[r][c]=='T' || board[r][c]=='O')
					n++;
			if(n==4)
				status=O_WON;
		}
		//Incomplete
		if(status==UNDEFINED) {
			for(int r=0; r<4; r++)
				for(int c=0; c<4; c++)
					if(board[r][c]=='.')
						status=NOT_COMPLETED;
			if(status!=NOT_COMPLETED)
				status=DRAW;
		}
		out<<"Case #"<<(t+1)<<": ";
		switch(status) {
		case X_WON:			out<<"X won"<<endl; break;
		case O_WON:			out<<"O won"<<endl; break;
		case DRAW:			out<<"Draw"<<endl; break;
		case NOT_COMPLETED:	out<<"Game has not completed"<<endl; break;
		}
	}
}