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
	int N, i, j, wins, played, k;
	char plays[101][101];
	double wp[101], owp[101]={0}, oowp, rpi, exWp[101][101]={0};
	scanf("%d\n",&N);
	REP(i, N) {
	  scanf("%s", plays[i]);
	  wins = played = 0;
	  REP(j, N) {
		if (plays[i][j] == '.') continue;
		if (plays[i][j] == '1') wins++;
		played++;
	  }
	  wp[i] = ((float)wins)/played;
	  REP(j, N) {
	    if (i == j || plays[i][j] == '.') continue;
		if (plays[i][j] == '1')
	  	  exWp[i][j] = ((float)wins-1)/(played-1);
	  	else 
	  	  exWp[i][j] = ((float)wins)/(played-1);
	  }
	}
	REP(i, N) {
	   k = 0;
	   owp[i] = 0;
	   REP(j, N) {
	     if (i == j || plays[i][j] == '.') continue;
	     owp[i] += exWp[j][i];
	     k++;
	   }
	   owp[i] /= k;
	}
	printf("Case #%d:\n",casenr);
	REP(i, N) {
	   k=0;
	   oowp=0;
	   REP(j, N) {
	     if (i == j || plays[i][j] == '.') continue;
	     oowp += owp[j];
	     k++;
	   }
	   oowp /= k;
	   rpi = wp[i]*0.25 + owp[i]*0.5 + oowp*0.25;
	   printf("%0.12g\n", rpi); 
	}	
}

int main() {
	int n; 
	scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}

 
