#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

string getRes(string board[4]){
    //check status
	//check diagals
    int xnum=0;
	int onum=0;
	int tnum=0;
	int dotnum=0;
	bool flag=false;

	for (int i=0;i<4;i++){
		if (board[i][i]=='X') {xnum++;}
			if (board[i][i]=='O') {onum++;}
			if (board[i][i]=='T') {tnum++;}
		}
		if (xnum==4) {return "X won";}
		if (xnum+tnum==4){return "X won";}
		if (onum==4) {return "O won";}
		if (onum+tnum==4) {return "O won";}

        xnum=0;
		onum=0;
		tnum=0;
		for (int i=0;i<4;i++){
			if (board[i][3-i]=='X') {xnum++;}
			if (board[i][3-i]=='O') {onum++;}
			if (board[i][3-i]=='T') {tnum++;}
		}
if (xnum==4) {return "X won";}
		if (xnum+tnum==4){return "X won";}
		if (onum==4) {return "O won";}
		if (onum+tnum==4) {return "O won";}


		//check rows.
		for (int i=0;i<4;i++){
        	xnum=0;
            onum=0;
            tnum=0;
			for (int j=0;j<4;j++){
				if (board[i][j]=='X') {xnum++;}
				if (board[i][j]=='O') {onum++;}
				if (board[i][j]=='T') {tnum++;}
				if (board[i][j]=='.') {dotnum++;}
			}
if (xnum==4) {return "X won";}
		if (xnum+tnum==4){return "X won";}
		if (onum==4) {return "O won";}
		if (onum+tnum==4) {return "O won";}
		}
		if (dotnum!=0) {flag = true;}
		//check columns
		for (int i=0;i<4;i++){
            xnum=0;
            onum=0;
            tnum=0;
			for (int j=0;j<4;j++){
				if (board[j][i]=='X') {xnum++;}
				if (board[j][i]=='O') {onum++;}
				if (board[j][i]=='T') {tnum++;}
			}
        if (xnum==4) {return "X won";}
		if (xnum+tnum==4){return "X won";}
		if (onum==4) {return "O won";}
		if (onum+tnum==4) {return "O won";}
		}
    if (flag) {return "Game has not completed";}
    else {return "Draw";}
}

int main(){
	ifstream input;
	input.open("A-large.in");
	ofstream output("outputl.txt");
	int casenum;
	string s;
	getline(input,s);
	casenum=atoi(s.c_str());
	//for each case
	for (int k=0;k<casenum;k++){
		string board[4];
		string res;
		bool flag = false;
		//input
		for (int j=0;j<4;j++){
			getline(input,s);
			board[j]=s;
		}
		getline(input,s);
        res = getRes(board);
        output << "Case #" << k+1 << ": " << res << endl;
	}
	input.close();
	output.close();

}
