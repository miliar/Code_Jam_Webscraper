#include <iostream>
#include <fstream>
#include <string>

using namespace std;
bool check_dot( char A , char B , char C , char D) {
	bool result = 0;
	if( A == '.' || B == '.' || C == '.' || D == '.' )
		result = 1;
	return result;
	}


bool check( char A , char B , char C , char D) {
	bool result = 0;
if ( (A != '.') && (B != '.') && (C != '.') && (D != '.') ){
	if( A == B && B == C && C == D )
		result = 1;
	else if( A == 'T' ) {
		if( B == C && C == D )
			result = 1;
		}
	else if( B == 'T' ) {
		if( A == C && C == D )
			result = 1;
		}
	else if( C == 'T' ) {
		if( A == B && B == D )
			result = 1;
		}
	else if( D == 'T' ) {
		if( A == B && B == C )
			result = 1;
		}
}
else
	result = 0;

return result;
}

int main(){
	
	ifstream input("A-large.in");
	ofstream output("output");
	//input.open("input");
	string s,out;
	//getline(input,s);
	//cout<<s<<endl;
	//output<<s<<endl;
	int tours;
	input>>tours;
	char board[4][4];
	for(int i=1;i<=tours;i++) {
		input>>board[0][0]>>board[0][1]>>board[0][2]>>board[0][3];
		input>>board[1][0]>>board[1][1]>>board[1][2]>>board[1][3];
		input>>board[2][0]>>board[2][1]>>board[2][2]>>board[2][3];
		input>>board[3][0]>>board[3][1]>>board[3][2]>>board[3][3];
		getline(input,s);
		
		//check rows
		if(check(board[0][0],board[0][1],board[0][2],board[0][3]))
		{ if(board[0][0]=='T') out = board[0][1]; else out = board[0][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(check(board[1][0],board[1][1],board[1][2],board[1][3]))
		{ if(board[1][0]=='T') out = board[1][1]; else out = board[1][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(check(board[2][0],board[2][1],board[2][2],board[2][3]))
		{ if(board[2][0]=='T') out = board[2][1]; else out = board[2][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(check(board[3][0],board[3][1],board[3][2],board[3][3]))
		{ if(board[3][0]=='T') out = board[3][1]; else out = board[3][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		// check columns
		else if(check(board[0][0],board[1][0],board[2][0],board[3][0]))
		{ if(board[0][0]=='T') out = board[1][0]; else out = board[0][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(check(board[0][1],board[1][1],board[2][1],board[3][1]))
		{ if(board[0][1]=='T') out = board[1][1]; else out = board[0][1]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(check(board[0][2],board[1][2],board[2][2],board[3][2]))
		{ if(board[0][2]=='T') out = board[1][2]; else out = board[0][2]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(check(board[0][3],board[1][3],board[2][3],board[3][3]))
		{ if(board[0][3]=='T') out = board[1][3]; else out = board[0][3]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		// check diameters
		else if(check(board[0][0],board[1][1],board[2][2],board[3][3]))
		{ if(board[0][0]=='T') out = board[1][1]; else out = board[0][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(check(board[3][0],board[2][1],board[1][2],board[0][3]))
		{ if(board[3][0]=='T') out = board[2][1]; else out = board[3][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		// not completed
		else if(check_dot(board[0][0],board[0][1],board[0][2],board[0][3]) || check_dot(board[1][0],board[1][1],board[1][2],board[1][3]) || check_dot(board[2][0],board[2][1],board[2][2],board[2][3]) || check_dot(board[3][0],board[3][1],board[3][2],board[3][3]))
		{ output<<"Case #"<<i<<": "<<"Game has not completed"<<endl; }
		// draw
		else
		{ output<<"Case #"<<i<<": "<<"Draw"<<endl; }
	}
	return 0;
	
}
