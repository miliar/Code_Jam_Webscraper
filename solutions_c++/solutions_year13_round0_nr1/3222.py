#include<iostream>
#include<sstream>
#include<cstring>
#include<fstream>
using namespace std;
int i,j,n;
char board[4][4];
char cur,ret,fret=' ';
char check_h(),check_v(),check_d1(),check_d2(),check_ret(char);
string space;
ifstream File("A-large.in");
ofstream oFile("output.io");
int main(){
	int k;
	File>>n;
	for(k=0;k<n;k++){
		fret=' ';
		for(i=0;i<4;i++){
			File>>board[i];
		}
		//getline(cin,space);
		check_ret(check_h());
		check_ret(check_v());
		check_ret(check_d1());
		check_ret(check_d2());
		oFile<<"Case #"<<k+1<<": ";
		switch(fret){
			case 'X':
				oFile<<"X won"<<endl;
				break;
			case 'O':
				oFile<<"O won"<<endl;
				break;
			case '.':
				oFile<<"Game has not completed"<<endl;
				break;
			case ' ':
				oFile<<"Draw"<<endl;
				break;
		}
	}
    return 0;
}

char check_h1(){
	cur=' ';
	for(i=0;i<4;i++){
		if(board[0][i]=='T')continue;
		if(board[0][i]=='.')return '.';
		if(cur==' '){
			cur=board[0][i];
		}
		if(cur!=' '){
			if(board[0][i]!=cur)return ' ';
			else continue;
		}
	}
	return cur;
}
char check_h(){
	char hret;
	for(j=0;j<4;j++){
		cur=' ';ret='\0';
		for(i=0;i<4;i++){
			if(board[j][i]=='T')continue;
			if(board[j][i]=='.'){
				ret='.';
				break;
			}
			if(cur==' '){
				cur=board[j][i];
			}
			if(cur!=' '){
				if(board[j][i]!=cur){
					ret=' ';
					break;
				}
				else continue;
			}
		}
		if(ret=='\0')ret=cur;
		if(ret=='X' || ret=='O')return ret;
		if(ret=='.')hret='.';
	}
	return hret;
}
char check_v(){
	char vret;
	for(j=0;j<4;j++){
		cur=' ';ret='\0';
		for(i=0;i<4;i++){
			if(board[i][j]=='T')continue;
			if(board[i][j]=='.'){
				ret='.';
				break;
			}
			if(cur==' '){
				cur=board[i][j];
			}
			if(cur!=' '){
				if(board[i][j]!=cur){
					ret=' ';
					break;
				}
				else continue;
			}
		}
		if(ret=='\0')ret=cur;
		if(ret=='X' || ret=='O')return ret;
		if(ret=='.')vret='.';
	}
	return vret;
}
char check_d1(){
	cur=' ';
	for(i=0;i<4;i++){
		if(board[i][i]=='T')continue;
		if(board[i][i]=='.')return '.';
		if(cur==' '){
			cur=board[i][i];
		}
		if(cur!=' '){
			if(board[i][i]!=cur)return ' ';
			else continue;
		}
	}
	return cur;
}
char check_d2(){
	cur=' ';
	for(i=0;i<4;i++){
		if(board[i][3-i]=='T')continue;
		if(board[i][3-i]=='.')return '.';
		if(cur==' '){
			cur=board[i][3-i];
		}
		if(cur!=' '){
			if(board[i][3-i]!=cur)return ' ';
			else continue;
		}
	}
	return cur;
}
char check_ret(char ret){
	if(ret=='X' || ret=='O')fret=ret;
	else if(ret=='.' && (fret!='X' && fret!='O'))fret='.';
	return fret;
}
