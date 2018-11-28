#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

/*problems
*/

/*plans
*/

//classes
typedef pair<int,int> P;

//constants
int INF=INT_MAX/2;

//variables
ifstream fin;
ofstream foot,fout;
int T;
string board[10];

//data structures

//functions
void solve()
{
	bool ny=0;

	//‰¡
	bool xw,ow;
	for(int i=0; i<4; i++){
		xw=0,ow=0;
		if(board[i][0]=='T'){
			xw=1;
			ow=1;
		}
		else if(board[i][0]=='X')xw=1;
		else if(board[i][0]=='O')ow=1;
		else ny=1;

		for(int j=1; j<4; j++){
			if(board[i][j]=='X')ow=0;
			if(board[i][j]=='O')xw=0;
			if(board[i][j]=='.'){
				ow=0;
				xw=0;
				ny=1;
			}
		}

		if(xw){
			fout<<"X won"<<endl;
			return;
		}
		if(ow){
			fout<<"O won"<<endl;
			return;
		}
	}

	//c
	for(int i=0; i<4; i++){
		xw=0,ow=0;
		if(board[0][i]=='T'){
			xw=1;
			ow=1;
		}
		else if(board[0][i]=='X')xw=1;
		else if(board[0][i]=='O')ow=1;
		else ny=1;

		for(int j=1; j<4; j++){
			if(board[j][i]=='X')ow=0;
			if(board[j][i]=='O')xw=0;
			if(board[j][i]=='.'){
				ow=0;
				xw=0;
				ny=1;
			}
		}

		if(xw){
			fout<<"X won"<<endl;
			return;
		}
		if(ow){
			fout<<"O won"<<endl;
			return;
		}
	}

	//ŽÎ‚ß1
	xw=0,ow=0;
	if(board[0][0]=='T'){
			xw=1;
			ow=1;
	}
	else if(board[0][0]=='X')xw=1;
	else if(board[0][0]=='O')ow=1;
	else ny=1;

	for(int i=1; i<4; i++){
		if(board[i][i]=='X')ow=0;
		if(board[i][i]=='O')xw=0;
		if(board[i][i]=='.'){
			ow=0;
			xw=0;
			ny=1;
		}
	}
	if(xw==1){
		fout<<"X won"<<endl;
		return;
	}
	if(ow==1){
		fout<<"O won"<<endl;
		return;
	}

	//ŽÎ‚ß2
	xw=0,ow=0;
	if(board[0][3]=='T'){
			xw=1;
			ow=1;
	}
	else if(board[0][3]=='X')xw=1;
	else if(board[0][3]=='O')ow=1;
	else ny=1;

	for(int i=1; i<4; i++){
		if(board[i][3-i]=='X')ow=0;
		if(board[i][3-i]=='O')xw=0;
		if(board[i][3-i]=='.'){
			ow=0;
			xw=0;
			ny=1;
		}
	}
	if(xw==1){
		fout<<"X won"<<endl;
		return;
	}
	if(ow==1){
		fout<<"O won"<<endl;
		return;
	}

	//Œˆ’…‚Â‚©‚¸
	if(ny==1)fout<<"Game has not completed"<<endl;
	else fout<<"Draw"<<endl;
}

int main()
{
	fin.open("C:\\Users\\fumi\\Downloads\\A-large.in");
	fout.open("C:\\Users\\fumi\\Downloads\\A-large-answer.txt");
	foot.open("C:\\Users\\fumi\\Downloads\\A-large-sample.txt");

	fin>>T;

	for(int i=0; i<T; i++){

	    memset(board,0,sizeof(board));
		for(int j=0; j<4; j++)fin>>board[j];

		fout<<"Case #"<<i+1<<":"<<" ";
		solve();
	}

	fin.close();
	fout.close();
	foot.close();

	system("pause");
	return 0;
}