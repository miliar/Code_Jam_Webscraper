#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<set>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<sstream>

using namespace std;

int n, test;
string board[4];

bool iswin(char symbol) {
	
	//Win row
	for(int i = 0 ; i < n ; i++) { 
		bool rwon = true;
		for(int j = 0; j < n ; j++) {
			if (board[i][j] != symbol && board[i][j] != 'T') {
				rwon = false;
				break;
			}
		}
		if (rwon) return true;
	}
	//Win column
	for(int j = 0 ; j < n ; j++) { 
		bool cwon = true;
		
		for(int i = 0; i < n ; i++) {
			//cout<<i<<" "<<j<<" "<<board[i][j]<<endl;;
			if (board[i][j] != symbol && board[i][j] != 'T') {
				cwon = false;
				break;
			}
		}
		if (cwon) return true;
	}
	
	//X won diagonal left to right
	int i = 0; int j = 0;
	bool dwin = true;
	for(int k = 0 ; k < n ;k++) {
		if (board[i][j] != symbol && board[i][j] != 'T') {
			dwin = false;
			break;
		}
		i++; j++;
	}
	if (dwin) return true;
	
	i = 3; j = 0;
	dwin = true;
	for(int k = 0 ; k < n ;k++) {
		if (board[i][j] != symbol && board[i][j] != 'T') {
			dwin = false;
			break;
		}
		i--; j++;
	}
	if (dwin) return true;
	
	return false;
}

string solve() {
	if (iswin('X')) return "X won";
	else if (iswin('O')) return "O won";
	
	
	for(int i = 0 ; i < n ; i++) { 
		for(int j = 0 ; j < n ; j++) {
			if (board[i][j] == '.') return "Game has not completed";
		}
	}
	
	return "Draw";
}

int main(){
    cin>>test;
    string a;
	n = 4;
    for(int t = 1;t<=test;t++){
        for(int i = 0 ; i < n ; i++) {
        	cin>>board[i];
        }
        cout<<"Case #"<<t<<": ";
        cout<<solve();
        if (t < test) {
        	cout<<endl;
        }
    }               
}
