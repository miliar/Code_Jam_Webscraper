#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <cassert>
#include <cstring>
using namespace std; 

using namespace std;

void solver(int T, string board[]){
	bool dot=false;
	int xmax=0;
	int omax=0;
	int xcount=0;
	int ocount=0;
	for(int r=0;r<4;r++){
		for(int c=0;c<4;c++){
			if(board[r][c]=='.'){
				dot=true;
				break;
			}
		}
	}
	
	for(int r=0;r<4;r++){
		xcount=0;
		ocount=0;
		for(int c=0;c<4;c++){
			if(board[r][c]=='X'||board[r][c]=='T')
				xcount++;
			if(board[r][c]=='O'||board[r][c]=='T')
				ocount++;
		}
		xmax=max(xmax,xcount);
		omax=max(omax,ocount);
	}


	for(int c=0;c<4;c++){
		xcount=0;
		ocount=0;
		for(int r=0;r<4;r++){
			if(board[r][c]=='X'||board[r][c]=='T')
				xcount++;
			if(board[r][c]=='O'||board[r][c]=='T')
				ocount++;
		}
		xmax=max(xmax,xcount);
		omax=max(omax,ocount);
	}

	xcount=0;
	ocount=0;
	for(int r=0,c=0;r<4,c<4;r++,c++){
		if(board[r][c]=='X'||board[r][c]=='T')
			xcount++;
		if(board[r][c]=='O'||board[r][c]=='T')
			ocount++;
	}
	xmax=max(xmax,xcount);
	omax=max(omax,ocount);

	xcount=0;
	ocount=0;
	for(int r=3,c=0;r>=0,c<4;r--,c++){
		if(board[r][c]=='X'||board[r][c]=='T')
			xcount++;
		if(board[r][c]=='O'||board[r][c]=='T')
			ocount++;
	}
	xmax=max(xmax,xcount);
	omax=max(omax,ocount);

	if(xmax==4){
		cout<<"Case #"<<T<<": X won"<<endl;
		return;
	}
	if(omax==4){
		cout<<"Case #"<<T<<": O won"<<endl;
		return;
	}
	if(xmax<4&&omax<4){
		if(dot)
			cout<<"Case #"<<T<<": Game has not completed"<<endl;
		else
			cout<<"Case #"<<T<<": Draw"<<endl;
	}
}

int main()
{
	int T=0;
	cin>>T;
	string board[4];

	for(int i=1;i<=T;i++){
		for(int j=0;j<4;j++){
			cin>>board[j];
		}
		solver(i, board);
	}
}