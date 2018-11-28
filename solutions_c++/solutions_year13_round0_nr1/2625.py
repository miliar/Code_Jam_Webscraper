
//Problem A. 

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <cmath>

using namespace std;

int n;
char board[4][4];
char instr[10];

int checkrow(char v, int index){
	int i;
	for (i=0;i<4;i++)
		if (board[index][i]!='T' && board[index][i]!=v) return 0;
	return 1;
}

int checkcol(char v, int index){
	int i;
	for (i=0;i<4;i++)
		if (board[i][index]!='T' && board[i][index]!=v) return 0;
	return 1;
}

int checkdiaga(char v){
	int i;
	for (i=0;i<4;i++)
		if (board[i][i]!='T' && board[i][i]!=v) return 0;
	return 1;
}

int checkdiagb(char v){
	int i;
	for (i=0;i<4;i++)
		if (board[i][3-i]!='T' && board[i][3-i]!=v) return 0;
	return 1;
}

int compute(){
	int i,j,k;
	int res=1;
	
	for (i=0;i<4;i++)
		for (j=0;j<4;j++)
			if (board[i][j]=='.') res=0;

	//check X
	for (i=0;i<4;i++){
		if (checkrow('X',i)) return 2;
		if (checkcol('X',i)) return 2;
		if (checkdiaga('X')) return 2;
		if (checkdiagb('X')) return 2;
	}
	for (i=0;i<4;i++){
		if (checkrow('O',i)) return 3;
		if (checkcol('O',i)) return 3;
		if (checkdiaga('O')) return 3;
		if (checkdiagb('O')) return 3;
	}
	return res;
}

int main(){
	int t;
	int i,j,k;
	
	cin>>t;
	for (i=0;i<t;i++){
		gets(instr);
		for (k=0;k<4;k++) {
			gets(instr);
			for (j=0;j<4;j++) board[k][j]=instr[j];
		}
			
		k=compute();
		cout<<"Case #"<<(i+1)<<": ";
		if (k==0) cout<<"Game has not completed";
		else if (k==1) cout<<"Draw";
		else if (k==2) cout<<"X won";
		else if (k==3) cout<<"O won";
		cout<<endl;
	}
}
