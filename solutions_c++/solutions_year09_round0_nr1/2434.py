#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
ifstream fin("A-large.in");
ofstream fout("a.large.out");
int l,d,n,r;
vector<string> m;
string ret;
int solve(string s){
	r = 0;
	ret = "";
	int k=0;
	map<char,bool> v[15];
	REP(i,SIZE(s)){
		if(s[i]=='('){
			i++;
			while(s[i]!=')'){
				v[k][s[i]] = true;
				i++;
			}
		}
		else{
			v[k][s[i]] = true;
		}
		k++;
	}
	REP(i,d){
		bool found = true;
		REP(j, l){
			if(v[j].find(m[i][j]) == v[j].end()){
				 found = false;
				 break;
			}
		}
		if(found) r++;
	}
	return r;
}
int main() {
    fin>>l>>d>>n;
	string s;
	REP(i,d){
		fin>>s;
		m.push_back(s);
	}
	REP(i,n){
		fin>>s;
		fout<<"Case #"<<(i+1)<<": "<<solve(s)<<endl;
	}
    return 0;
}
