#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define RREPEAT(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) RREPEAT(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll long long int
#define uli unsigned long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("A-large.in");
//A-small-attempt0
#define cin fin
ofstream fout ("A-large.out");
#define cout fout

set<pair<string,string> > st;
int ans=0LL;
void parse(string s) {
	REP(i,s.size()) if(s[i]=='/') s[i]=' ';
	vs v;
	string k;
	istringstream iss(s);
	while(iss>>k) v.pb(k);
	k="/";
	REP(i,v.size()) {
		if(!st.count(mkp(k,v[i]))) st.insert(mkp(k,v[i]));
		k+=v[i]+"/";
	}
	return;
}
void cnt(string s) {
	REP(i,s.size()) if(s[i]=='/') s[i]=' ';
	vs v;
	string k;
	istringstream iss(s);
	while(iss>>k) v.pb(k);
	k="/";
	REP(i,v.size()) {
		if(!st.count(mkp(k,v[i]))) st.insert(mkp(k,v[i])),ans++;
		k+=v[i]+"/";
	}
	return;
}
int main() {
    int t=0;
    cin>>t;
    REP(T,t) { 
		st.clear();
		ans=0;
		int n,m;
		cin>>n>>m;
		string s;
		REP(i,n) cin>>s,parse(s);
		REP(i,m) {
			cin>>s,cnt(s);
		//	cout<<s<<endl;
		//	cout<<ans<<endl;
		//	system("pause");
		}
		cout<<"Case #"<<T+1<<": "<<ans<<endl;
    }
    system("pause");
    return 0;
}
