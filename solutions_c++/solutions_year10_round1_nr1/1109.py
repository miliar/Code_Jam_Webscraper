//============================================================================
// Name        : Rotate.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
using namespace std;

string board[50];
int main() {
	int ntc;
	cin >> ntc;
	for(int ci=0;ci<ntc;ci++){
		int N,K;
		cin >> N >> K;
		for(int i=0;i<N;i++){
			cin >> board[i];
//			cout << board[i] << endl;
		}
		bool is_shift=false;
		for(int i=0;i<N;i++){
			for(int j=N-1;j>=0;j--){
				if(board[i][j]=='.'){
					for(int k=j;k>0;k--){
						board[i][k]=board[i][k-1];
						if(board[i][k-1]!='.'){
							is_shift=true;
						}
					}
					board[i][0]='.';
					if(is_shift){
						is_shift=false;
						j++;
					}
//					cout << i<<" "<< board[i] << endl;
				}
			}
//			cout << board[i] << endl;
		}
		string keyB=string(K,'B');
		string keyR=string(K,'R');
		bool is_B_win=false;
		bool is_R_win=false;
		for(int i=0;i<N;i++){
			if(!is_B_win)
				if(board[i].find(keyB)!=string::npos)
					is_B_win=true;
			if(!is_R_win)
				if(board[i].find(keyR)!=string::npos)
					is_R_win=true;
		}
		for(int i=0;i<N;i++){
			string tmp;
			for(int j=0;j<N;j++){
				tmp+=board[j][i];
			}
			if(!is_B_win)
				if(tmp.find(keyB)!=string::npos)
					is_B_win=true;
			if(!is_R_win)
				if(tmp.find(keyR)!=string::npos)
					is_R_win=true;
		}
		for(int i=0;i<N;i++){
			string tmp1,tmp2,tmp3,tmp4;
			for(int j=0;j<=i;j++){
				tmp1+=board[j][i-j];
				tmp2+=board[N-1-j][N-1-i+j];
				tmp3+=board[j][N-1-i+j];
				tmp4+=board[N-1-j][i-j];
			}
			if(!is_B_win)
				if(tmp1.find(keyB)!=string::npos)
					is_B_win=true;
			if(!is_R_win)
				if(tmp1.find(keyR)!=string::npos)
					is_R_win=true;
			if(!is_B_win)
				if(tmp2.find(keyB)!=string::npos)
					is_B_win=true;
			if(!is_R_win)
				if(tmp2.find(keyR)!=string::npos)
					is_R_win=true;
			if(!is_B_win)
				if(tmp3.find(keyB)!=string::npos)
					is_B_win=true;
			if(!is_R_win)
				if(tmp3.find(keyR)!=string::npos)
					is_R_win=true;
			if(!is_B_win)
				if(tmp4.find(keyB)!=string::npos)
					is_B_win=true;
			if(!is_R_win)
				if(tmp4.find(keyR)!=string::npos)
					is_R_win=true;
		}
//		cout << is_B_win << is_R_win << endl;
		cout << "Case #" << ci+1 << ": ";
		if(is_R_win && is_B_win)
			cout << "Both";
		else if(is_R_win)
			cout << "Red";
		else if(is_B_win)
			cout << "Blue";
		else
			cout << "Neither";
		cout << endl;
	}
	return 0;
}
