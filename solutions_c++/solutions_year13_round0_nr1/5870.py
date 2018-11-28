// A.cpp : Defines the entry point for the console application.
//

#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>


using namespace std;
#define ll long long
vector <string> in;
bool check(char ch){
	for(int r=0;r<4;++r){
		bool ok=true;
		for(int c=0;c<4;++c){
			if(in[r][c]!=ch&&in[r][c]!='T')ok=false;
		}
		if(ok){
			return true;
		}
	}

	for(int c=0;c<4;++c){
		bool ok=true;
		for(int r=0;r<4;++r){
			if(in[r][c]!=ch&&in[r][c]!='T')ok=false;
		}
		if(ok){
			return true;
		}
	}
	
	bool ok=true;
	for(int d=0;d<4;++d){
		if(in[d][d]!=ch&&in[d][d]!='T')ok=false;	
	}
	if(ok)return true;

	ok=true;
	for(int d=0;d<4;++d){
		if(in[3-d][d]!=ch&&in[3-d][d]!='T')ok=false;
	}
	if(ok)return true;

	return false;
}

int main(void)
{

	int N;
	cin>>N;
	for(int i=0;i<N;++i){
		in.clear();
		in.resize(4);
		for(int j=0;j<4;++j){
			cin>>in[j];
		}
		
		bool xWin=check('X');
		bool oWin=check('O');
		if(xWin&&oWin)cout<<"ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"<<endl;
		
		if(xWin){
			cout<<"Case #"<<i+1<<": X won"<<endl;
		}else if(oWin){
			cout<<"Case #"<<i+1<<": O won"<<endl;
		}else{
			bool gameEnd=true;
			for(int r=0;r<4;++r){
				for(int c=0;c<4;++c){
					if(in[r][c]=='.')gameEnd=false;
				}
			}
			if(gameEnd){
				cout<<"Case #"<<i+1<<": Draw"<<endl;
			}else{
				cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
			}
		}
	}
}




