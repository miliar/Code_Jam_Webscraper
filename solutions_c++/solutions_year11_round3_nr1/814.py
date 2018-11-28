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
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  

void run(int casenr) {
	int r,c; cin>>r>>c;
	string row[r];
	string nrow[r];
	bool poss = true;

	REP(i,r)
	{
		cin>>row[i];
		bool even = true;
		REP(j,c)
		{
			if(row[i][j] == '.' && even) continue;
			else if(row[i][j] == '.') {poss = false;break;}
			else if(row[i][j] == '#') even = !even;
		}
		if(!even) poss = false;
	}
	if(!poss) goto prints;
	REP(i,c)
	{
		bool even = true;
		REP(j,r)
		{
			if(row[j][i] == '.' && even) continue;
			else if(row[j][i] == '.') {poss = false;break;}
			else if(row[j][i] == '#') even = !even;
		}
		if(!even) poss = false;
	}
	if(!poss) goto prints;
	REP(i,r) nrow[i] = row[i];
	REP(i,r)
	{
		bool even = true;
		REP(j,c)
		{
			if(nrow[i][j] == '.') continue;
			else if(nrow[i][j] == '#') {nrow[i][j] = even?'/':'\\'; nrow[i+1][j] = even?'\\':'/'; even = !even;}
		}
	}
	prints: cout<<"Case #"<<casenr<<":"<<endl;
	if(poss) REP(i,r) cout<<nrow[i]<<endl;
	else cout<<"Impossible"<<endl;
}

int main() {
	int n; cin>>n; FORE(i,1,n) run(i);
	return 0;
}

 
