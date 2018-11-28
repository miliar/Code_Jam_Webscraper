// 2013QR_A_TTTT.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <string>
using namespace std;

bool checkLine(char *p,int sv,int sh,char *winner )
{
	char *plast = p+sv*3+sh*3;
	*winner = *p;
	p=p+sv+sh;
	if(*winner == '.') return false;
	while(p<=plast){
		if(*p=='.') return false;
		if(*p!=*winner){
			if(*winner=='T'){
				*winner=*p;
				p=p+sv+sh;
				continue;
			}
			else if(*p=='T'){
				p=p+sv+sh;
				continue;
			}
			else return false;
		}
		p=p+sv+sh;
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char board[4][4];
	ifstream infile("A-large.in");
	int T;
	infile>>T;
	ofstream outfile("out.txt");
	for(int i = 1;i<=T;i++){
		for(char *p = &board[0][0];p<=&board[3][3];)
			infile>>*p++;//会有问题
		infile.get();
		char firstChar;
		//line scan
		int j=0;
		for(;j<4;j++){
			if(checkLine(&board[j][0],0,1,&firstChar))
				break;
		}
		if(j!=4){
			outfile<<"Case #"+to_string(long long(i))+": "+firstChar+" won"<<endl;
			continue;
		}
		//col scan
		j = 0;
		for(;j<4;j++){
			if(checkLine(&board[0][j],4,0,&firstChar))
				break;
		}
		if(j!=4){
			outfile<<"Case #"+to_string(long long(i))+": "+firstChar+" won"<<endl;
			continue;
		}
		//cross
		if(checkLine(&board[0][0],4,1,&firstChar)){
			outfile<<"Case #"+to_string(long long(i))+": "+firstChar+" won"<<endl;
			continue;
		}
		if(checkLine(&board[0][3],4,-1,&firstChar))
		{
			outfile<<"Case #"+to_string(long long(i))+": "+firstChar+" won"<<endl;
			continue;
		}
		char *p = board[0],*q=&board[3][3];
		for(;p<=q;p++)
			if(*p=='.'){
				outfile<<"Case #"+to_string(long long(i))+": Game has not completed"<<endl;
				break;
			}
		if(p>q)
			outfile<<"Case #"+to_string(long long(i))+": Draw"<<endl;
	}
	return 0;
}

