/*
 * B.cpp
 *
 *  Created on: May 6, 2011
 *      Author: elvitucho
 */

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
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;

map<string,char> comb, del;

char getcomb(char c1, char c2){
	string key = "";
	key+=c1;
	key+=c2;
	sort(all(key));
	if(comb.find(key)!=comb.end()) return comb[key];
	return ' ';
}
bool puededel(char c, string sol){
	REPSZ(i,sol){
		string key = "";
		key+=c;
		key+=sol[i];
		sort(all(key));
		if(del.find(key)!=del.end()) return true;
	}
	return false;
}
string format(string s){
	string sol="[";
	REPSZ(i,s){
		if(i>0) sol+=", ";
		sol+= s[i];
	}
	sol+="]";
	return sol;
}
void run1(int caso){
	int C;
	cin >>C;
	comb.clear();
	del.clear();
	REP(i,C){
		string s;
		cin >> s;
		string key = s.substr(0,2);
		sort(all(key));
		//cout << key << endl;
		comb[key]=s[2];
	}
	//cout << "********" << endl;
	int D;
	cin >> D;
	REP(i,D){
		string s;
		cin >> s;
		string key = s;
		sort(all(key));
		//cout << key << endl;
		del[key]=' ';
	}

	int N;
	cin >> N;
	string cad;
	cin >> cad;

	string sol="";
	REP(i,N){
		char c = ' ';
		if(sol.size()>0) c = getcomb(sol[sol.size()-1],cad[i]);
		if(c!=' '){
			sol = sol.substr(0,sol.size()-1)+c;
		} else{
			if(puededel(cad[i],sol)) sol="";
			else sol+=cad[i];
		}
	}
	sol = format(sol);
	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}
