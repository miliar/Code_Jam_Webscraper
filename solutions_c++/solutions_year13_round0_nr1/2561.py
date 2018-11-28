#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
#include <queue>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

typedef long long ll;
#define REP(i,k) for(int (i)=0;(i)<(k);(i)++)
#define INF ~(1<<31)
#define CLR(a) memset((a),0,sizeof((a)))
#define EPS 1e-9
#define DBG 1
#define D(s,v) if(DBG) cout<<(s)<<": "<<(v)<<endl;
#define DVEC(s,v) if(DBG) {cout<<(s)<<": "; for(int i=0;i<(v).size();i++) cout<<(v)[i]<<" "; cout<<endl;}
#define DARR(s,v,n) if(DBG) {cout<<(s)<<": "; for(int i=0;i<n;i++) cout<<(v)[i]<<" "; cout<<endl;}

int main(){
ios_base::sync_with_stdio(0);
int T;
cin>>T;
string board[4];

for(int cs=0;cs<T;cs++){
	for(int i=0;i<4;i++){
		string s;
		cin>>s;
		board[i]=s;
	}
	
	char winner='!';
	
	for(int i=0;i<4;i++){		
		bool same=1;
		char c = board[i][0];
		if(c=='T') c=board[i][1];
		
		for(int j=1;j<4;j++)
		if(board[i][j]!=c && board[i][j]!='T') same=0;		
		if(same && c!='.') winner=c;
				
		same=1;
		c = board[0][i];
		if(c=='T') c=board[1][i];
		
		for(int j=1;j<4;j++)
		if(board[j][i]!=c && board[j][i]!='T') same=0;		
		if(same && c!='.') winner=c;
	}
		
	bool same=1;
	char c = board[0][0];
	if(c=='T') c=board[1][1];
	
	for(int i=1;i<4;i++){
		if(board[i][i]!=c && board[i][i]!='T') same=0;
	}
	if(same && board[0][0]!='.') winner=c;
	
	for(int i=0;i<4;i++){
		reverse(board[i].begin(),board[i].end());
	}
	
	same=1;
	c = board[0][0];
	if(c=='T') c=board[1][1];
	
	for(int i=1;i<4;i++){
		if(board[i][i]!=c && board[i][i]!='T') same=0;
	}	
	if(same && board[0][0]!='.') winner=c;
	
	cout<<"Case #"<<cs+1<<": ";
	
	if(winner=='!'){
		bool rem=0;
		
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		if(board[i][j]=='.') rem=1;
		
		if(rem) cout<<"Game has not completed"<<endl;
		else cout<<"Draw"<<endl;
	}
	else{
		cout<<winner<<" won"<<endl;
	}
	
}

}