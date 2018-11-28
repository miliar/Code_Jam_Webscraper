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
#include <map>
#include <stack>
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
ifstream fin("C-small-attempt0.in");
ofstream fout("C-small.out");
vector<string> v[150];
map<string, int> m;
string k = "welcome to code jam";
int n;
string solve(string s){
	m.clear();
	REP(i,SIZE(s)){
		if(s[i]=='w'){
			m["w"]++;
		}
		else{
			REP(j,SIZE(v[(int)s[i]])){
				m[v[(int)s[i]][j]+s[i]]+=m[v[(int)s[i]][j]];
				if(m[v[(int)s[i]][j]+s[i]]>1000){
					m[v[(int)s[i]][j]+s[i]]%=1000;
				}
			}
		}
	}
	ostringstream oss;
	oss<<m[k];
	string str = oss.str();
	while(SIZE(str)<4)str = "0"+str;
	return str;
}
int main() {
	for(int i=1;i<SIZE(k);i++){
		v[(int)k[i]].push_back(k.substr(0,i));
	}
	string s;
	fin>>n;
	getline(fin,s);
	REP(i,n){
		getline(fin,s);
		fout<<"Case #"<<(i+1)<<": "<<solve(s)<<endl;
	}
  
    
    return 0;
}
