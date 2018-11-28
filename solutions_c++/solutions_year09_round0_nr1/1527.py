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

map<string,int> dic;
int sol;
vector<string> v;

bool valido(string s){
	if(s=="") return true;
	map <string, int> :: iterator it;	
	for(it=dic.begin(); it!=dic.end(); it++){
		string sdic = it->first;
	    if(s==sdic) return true;
		if(sdic.substr(0,SZ(s)) == s) return true;
		if(s<sdic) return false;		
	}
	return false;

}
void go(int ind, string s){
	if(ind>=SZ(v)){
		if(dic.find(s)!=dic.end()) sol++;
		return;
	}
	if(!valido(s)) return;
	
	REP(i,SZ(v[ind])) {
		string wi = s + v[ind][i];
		go(ind+1,wi);
	}

}
vector<string> getTokens(string s){
	vector<string> sol;
	string tok = "";
	bool btok = false;
	REP(i,SZ(s)){
		if(s[i]==')'){
			sol.push_back(tok);	
			tok = "";
			btok = false;
		}else if(s[i]!='(') {			
			if(btok)tok+=s[i];
			else{
				tok="";		
				string wi = "";
				wi+=s[i];
				sol.push_back(wi);
			}
		} else if(s[i]=='(') btok = true;
	}
	
	return sol;
}
void run1(int caso){
	string pattern;
	cin >>pattern;

	v = getTokens(pattern);
	sol = 0;
	go(0,"");	
	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int L,D;
	cin >>L>>D;
	int T; cin >>T;
	string s;
	REP(i,D) {
		cin >> s;
		dic[s]=1;
	}
	
	FORE(i,1,T) run1(i);
	return 0;
}