#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <utility>
#include <iterator>
#include <functional>
#include <numeric>
#include <string>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <climits>
#include <cassert>
#include <algorithm>
#define debug(x) cerr<<#x<<"="<<(x)<<endl
#define ISS istringstream
#define _USE_MATH_DEFINES
#define SS stringstream

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){

		char a[4][4];
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>a[j][k];

		int rowx;
		int colx;
		int colo;
		int rowo;
		bool trowfound = false;
		bool tcolfound = false;
			
		char winner;
		bool complete = true;
		bool winnerFound = false;
		for(int j=0;j<4;j++){
			rowx = 0;
			colx = 0;
			colo = 0;
			rowo = 0;
			trowfound = false;
			tcolfound = false;
			for(int k=0;k<4;k++){
				if(a[j][k]=='X')
					rowx++;
				if(a[j][k]=='O')
					rowo++;
				if(a[k][j]=='X')
					colx++;
				if(a[k][j]=='O')
					colo++;
				if(a[j][k]=='.')
					complete = false;
				if(a[j][k]=='T')
					trowfound = true;
				if(a[k][j]=='T')
					tcolfound = true;
			}
			if(rowx==4 || (rowx==3 && trowfound)){
				winner = 'X';
				winnerFound = true;
				break;
			}
			if(colx==4 || (colx==3 && tcolfound)){
				winner = 'X';
				winnerFound = true;
				break;
			}
			if(rowo==4 || (rowo==3 && trowfound)){
				winner = 'O';
				winnerFound = true;
				break;
			}
			if(colo==4 || (colo==3 && tcolfound)){
				winner = 'O';
				winnerFound = true;
				break;
			}
		}


		// Check diagonals
		if(!winnerFound){
			rowx = 0;
			colx = 0;
			colo = 0;
			rowo = 0;
			trowfound = false;
			tcolfound = false;
			for(int j=0;j<4;j++){
				if(a[j][j]=='X')
					rowx++;
				if(a[j][j]=='O')
					rowo++;
				if(a[3-j][j]=='X')
					colx++;
				if(a[3-j][j]=='O')
					colo++;
				if(a[j][j]=='T')
					trowfound = true;
				if(a[3-j][j]=='T')
					tcolfound = true;
		
			}
			if(rowx==4 || (rowx==3 && trowfound)){
				winner = 'X';
				winnerFound = true;
			}
			if(colx==4 || (colx==3 && tcolfound)){
				winner = 'X';
				winnerFound = true;
			}
			if(rowo==4 || (rowo==3 && trowfound)){
				winner = 'O';
				winnerFound = true;
			}
			if(colo==4 || (colo==3 && tcolfound)){
				winner = 'O';
				winnerFound = true;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(!winnerFound){
			cout<< (complete ? "Draw" : "Game has not completed")<<endl;
		}
		else{
			cout<<winner<<" won"<<endl;
		}
		cin.ignore(80,'\n');
	}
	return 0;
}