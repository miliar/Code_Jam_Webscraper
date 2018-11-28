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
	int n; cin>>n;
	string play[n];
	float wp[n],owp[n],oowp[n];
	int win[n],lose[n];
	REP(i,n)
	{
		cin>>play[i];
		win[i]=0;lose[i]=0;
		REP(j,n)
		{
			if(play[i][j] == '.') continue;
			else if(play[i][j] == '1') win[i]++;
			else if(play[i][j] == '0') lose[i]++;
		}
		wp[i] = float(win[i])/(win[i] + lose[i]);
	}
	REP(i,n)
	{
		owp[i]=0;
		REP(j,n)
		{
			if(play[i][j] == '.') continue;
			else if(play[i][j] == '1') owp[i] += float(win[j])/(win[j]+lose[j]-1);
			else if(play[i][j] == '0') owp[i] += float(win[j]-1)/(win[j]+lose[j]-1);
		}
		owp[i] /= win[i] + lose[i];
	}
	REP(i,n)
	{
		oowp[i]=0;
		REP(j,n)
		{
			if(play[i][j] == '.') continue;
			else if(play[i][j] == '1') oowp[i] += owp[j];
			else if(play[i][j] == '0') oowp[i] += owp[j];
		}
		oowp[i] /= win[i] + lose[i];
	}
	cout<<"Case #"<<casenr<<":"<<endl;
	REP(i,n) cout<<(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i])<<endl;
}

int main() {
	int n; cin>>n; FORE(i,1,n) run(i);
	return 0;
}

 
