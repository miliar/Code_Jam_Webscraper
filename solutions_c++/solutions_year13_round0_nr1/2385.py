#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int T;

 bool find(vector<string> &M, string s){
 //horizontal
	 for(int i = 0; i<M.size(); i++)
		if(M[i] == s) return true;
//vertical
	 for(int i = 0; i<M.size(); i++){
		 string tmp;
		 for(int j = 0; j<M[i].size(); j++){
			 tmp += M[j][i];
		 }
		 if(s == tmp) return true;
	 }
//diagonal1
	string tmp="";
	 for(int i = 0; i<M.size(); i++){
		 tmp += M[i][i];
		 if(s == tmp) return true;
	 }
//diagonal2
	 tmp="";
	 for(int i = 0; i<M.size(); i++){
		 tmp += M[i][3-i];
		 if(s == tmp) return true;
	 }
	 return false;
 }

 int main(){
	ifstream in("A.txt");  
	ofstream out("resultado.txt");
	in >> T;
	cout << "T = " << T << endl;
	for(int test =1; test<=T; test++){
		vector<string> M;
		string tmp;
		for(int i =0; i<4; i++){
			in >> tmp;
			M.push_back(tmp);
		}

		string search[10] = {"XXXX","XXXT","XXTX","XTXX","TXXX", "OOOO", "OOOT", "OOTO", "OTOO", "TOOO"};

		bool Xwins=false,Owins=false;
		for(int i = 0; i<10; i++){
			if(find(M,search[i])){
				if(i<5) {Xwins = true; break;}
				else {Owins = true; break;}
			}
		}

		bool notcompleted = false;
		if(!Xwins && !Owins){
			for(int i = 0; i<4; i++)
				for(int j = 0; j<4; j++)
					if(M[i][j] == '.')
						notcompleted = true;
		}

		out << "Case #" << test << ": ";
		cout << "Case #" << test << ": ";
		
		if(Xwins){
			out << "X won" << endl;
			cout << "X won" << endl;
		}
		else if(Owins){
			out << "O won" << endl;
			cout << "O won" << endl;

		}
		else if(notcompleted){
			out << "Game has not completed" << endl;
			cout << "Game has not completed" << endl;
		}
		else{
			out << "Draw" << endl;
			cout << "Draw" << endl;
		}
	}
	return 0;
 } 
    