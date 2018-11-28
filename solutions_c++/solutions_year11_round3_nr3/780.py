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

int find(int num,int ar[],int m)
{
	int res = -1;
	REP(i,m)
	{
		if(ar[i] == num)
		{
			res = i;
			break;
		}
	}
	return res;
}
	

void run(int casenr) {
	int n,l,h;
	cin>>n>>l>>h;
	int f[n];
	REP(i,n) cin>>f[i];
	bool p[h+1];
	bool poss = true;
	int res;
	REPE(i,h) p[i] = true;
	FORE(i,l,h)
	{
		if(!p[i]) continue;
		poss = true;
		REP(j,n)
		{
			if(f[j]%i == 0 || i%f[j] == 0) continue;
			else {poss = false; break;}
		}
		// if(!poss)
		// {
			// int j = i;
			// while(j<=h)
			// {
				// p[j] = false;
				// j+= i;
			// }
		// }
		res = i;
		if(poss) break;
	}
	
	
	cout<<"Case #"<<casenr<<": ";
	if(poss) cout<<res<<endl;
	else cout<<"NO\n";
}

int main() {
	int n; cin>>n; FORE(i,1,n) run(i);
	return 0;
}

 
