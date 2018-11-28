#include<iostream>
#include<string>
#include<stdio.h>
#include<cstdio>
#include<fstream>
#define FOR(i,b) for(int i=0;i<b;++i)
using namespace std;
char a[4][4];
string check(){
	int xc=0,oc=0,tc=0;
	FOR(i,4){
		 xc=0,oc=0,tc=0;
		FOR(j,4){
			if(a[i][j]=='X') xc++;
			if(a[i][j]=='O') oc++;
			if(a[i][j]=='T') tc++;

		}
		if(oc+tc==4) return "O won";
		if(xc+tc==4) return "X won";
		xc=oc=tc=0;
		FOR(j,4){
			if(a[j][i]=='X') xc++;
			if(a[j][i]=='O') oc++;
			if(a[j][i]=='T') tc++;
		}
		if(oc+tc==4) return "O won";
		if(xc+tc==4) return "X won";
	}
	xc=oc=tc=0;
	FOR(i,4) {
		if(a[i][i]=='X') xc++;
		if(a[i][i]=='O') oc++;
		if(a[i][i]=='T') tc++;
		
	}
	if(oc+tc==4) return "O won";
		if(xc+tc==4) return "X won";
	xc=oc=tc=0;
	FOR(i,4) {
		if(a[i][3-i]=='X') xc++;
		if(a[i][3-i]=='O') oc++;
		if(a[i][3-i]=='T') tc++;
	}
	if(oc+tc==4) return "O won";
	if(xc+tc==4) return "X won";
	FOR(i,4) FOR(j,4) if(a[i][j]=='.') return "Game has not completed";
	return "Draw";
}

int main(int argc, char* argv[]){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	
	FOR(n,t){
		FOR(i,16){
			cin>>a[i/4][i%4];
		}
		cout<<"Case #"<<n+1<<": "<<check()<<"\n";
	}
}