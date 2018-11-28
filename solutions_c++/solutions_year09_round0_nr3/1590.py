#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>
 
using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))
#define MOD 10000

string welcome = "welcome to code jam";
string s;
int memo[505][20];
int go( int ind, int indw){
	if(ind>=SZ(s)) return 0;
	if(memo[ind][indw]>-1) return memo[ind][indw];
	if(indw==SZ(welcome)-1 && s[ind]==welcome[indw]){
		memo[ind][indw]=(1+go(ind+1,indw))%MOD;
		return memo[ind][indw];
	}
	if(s[ind]!= welcome[indw]) return go(ind+1,indw)%MOD;
	memo[ind][indw]=(go(ind+1,indw+1)%MOD+go(ind+1,indw)%MOD)%MOD;
	return memo[ind][indw];
}
string format(int sol){
	string s="";
	char buff[5];
	if(sol>=1000){
		sprintf(buff,"%d",sol);	
		s=buff;
		return s;
	}
	if(sol>=100){
		sprintf(buff,"0%d",sol);	
		s=buff;
		return s;
	}
	if(sol>=10){
		sprintf(buff,"00%d",sol);	
		s=buff;
		return s;
	}
	
	sprintf(buff,"000%d",sol);	
	s=buff;
	return s;	
}
void run1(int caso){
	getline(cin,s);	
	memset(memo,-1,sizeof(memo));
//	cout <<SZ(s)<<endl;
	cout << "Case #"<<caso<<": "<< format(go(0,0))<<endl;
}
int main()
{
	int T; cin>>T;
	getline(cin,s);
	FORE(i,1,T) run1(i);
	return 0;
}