#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
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
ifstream fin("B-large.in");
ofstream fout("B-large.out");
int no;
int tot[10];
int num[21];
string solve(string n){
	
	
	string s = n;
	string tmp = s;
	next_permutation(ALL(s));
	if(s<=tmp){
		int cnt = 1;
		while(s[0]=='0'){
			s.erase(s.begin());
			cnt++;
		}
		REP(i,cnt)
			s.insert(s.begin()+1,'0');
	}
	
	return s;
}
int main() {
	fin>>no;
	string str;
	getline(fin,str);
	for(int k=1;k<=no;k++){
		getline(fin,str);
		fout<<"Case #"<<k<<": "<<solve(str)<<endl;
	}
    return 0;
}
