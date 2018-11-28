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
const int MAX = 100000;
ifstream fin("A-small-attempt0.in");
ofstream fout("A-small.out");
int noCase;
bool ok[11][MAX+1];
int pw(int a,int b){
	return b==0?1:a*pw(a,b-1);
}
string convert(int x, int base){
	string ret = "";
	while(x/base != 0){
		char c = (x%base) + '0';
		ret = c+ret;
		x/=base;
	}
	char c = (x%base) + '0';
	ret = c + ret ; 
	return ret;
}
int btoi(string x, int base){
	int ret = 0 ;
	for(int i=x.size()-1; i>=0;i--){
		ret += pw(base,x.size()-1-i)*(x[i]-'0');
	}
	return ret;
}
string square(string s,int base){
	int n = 0 ;
	REP(i, SIZE(s)){
		n += (s[i]-'0')*(s[i]-'0');
	}
	return convert(n,base);
}
bool isHappy(int x,int base){
	map<int,bool> m;
	string r = "";
	int k = 0;
	m[x] = true;
	while(x!=1 && k<=1000){
		r = convert(x,base);
		string sq = square(r,base);
		x = btoi(sq,base);
		if(x==1) return true;
		if(m.find(x) != m.end()) return false;
		m[x] = true;
		k++;
	}
	return false;
}
int main() {
	vector<int> bases;
	fin>> noCase;
	memset(ok, false, sizeof(ok));
	memset(ok[2],true,sizeof(ok[2]));
	for(int i=2;i<=MAX;i++){
		for(int j = 3; j<=10;j++){
			if(j==4){
				ok[j][i] =true;
				continue;
			}
			if(isHappy(i,j)){
				ok[j][i] = true;
			}
		}
	}
	string s;
	getline(fin,s);
	for(int k = 1 ; k <= noCase; k++){
		getline(fin,s);
		istringstream iss(s);
		int n ;
		bases.clear();
		while(iss>>n){
			bases.push_back(n);
		}
		for(int i=2;i<=MAX;i++){
			bool finished = true;
			for(int j=0;j<SIZE(bases);j++){
				if(!ok[bases[j]][i]){
					finished = false;
					break;
				}
			}
			if(finished){
				fout<<"Case #"<<k<<": "<<i<<endl;
				break;
			}
		}
	}
    return 0;
}
