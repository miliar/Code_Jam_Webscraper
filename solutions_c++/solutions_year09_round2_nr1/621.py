#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <iomanip>
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
const int MAX = 10000000;
ifstream fin("A-small-attempt0.in");
ofstream fout("A-small.out");
int noCase;
map<string,bool> m;
struct item{
	double weight;
	string feature;
	item(double a=0,string b=""){
		weight = a;
		feature = b;
	}
	
};
item list[500];
int get(string s,int& start){
	while(s[start]!='(')start++;
	start++;
	while(s[start]==' ')start++;
	int end = start;
	int open = 1;
	while(open){
		if(s[end]=='(')open++;
		if(s[end]==')')open--;
		end++;
	}
	end--;
	while(s[end]==' ')end--;
	return end;
}
void construct(string s,int n){
	istringstream iss(s);
	double weight;
	string feature;
	iss>>weight;
	iss>>feature;
	list[n] = item(weight,feature);
	if(feature!=""){
		int start = 0 ;
		int end = get(s,start);
		construct(s.substr(start,end-start), 2*n);
		start = end;
		end = get(s,start);
		construct(s.substr(start,end-start), 2*n+1);
	}	
}
long double solve(){
	int idx = 1;
	long double p = 1;
	while(list[idx].feature != ""){
		p *= list[idx].weight;
		if(m[list[idx].feature]){
			idx = 2*idx;
		}
		else{
			idx = 2*idx+1;
		}
	}
	
	return p*list[idx].weight;
}
int main() {
	fin>>noCase;
	for(int k=1;k<=noCase;k++){
		int n;
		
		string s,tmp;
		fin>>n;getline(fin,tmp);
		REP(i,n){
			getline(fin,tmp);
			s+=tmp;
		}
		construct(s.substr(1,SIZE(s)-2),1);
		fin>>n;
		fout<<"Case #"<<k<<": "<<endl;
		REP(i,n){
			fin>>tmp;
			int noProp;
			fin>>noProp;
			m.clear();
			REP(j,noProp){
				fin>>tmp;
				m[tmp]=true;
			}
			fout<<fixed<<setprecision(8)<<solve()<<endl;
		}
		
	}
    return 0;
}
