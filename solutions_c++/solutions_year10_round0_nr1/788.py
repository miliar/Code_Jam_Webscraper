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
int N,K,t;
bool isOn(int n, int k){
	int mod = 1;
	REP(i,n-1){
		mod *= 2;
	}
	if((k / mod) % 2 == 0 ) return false;
	return true;
}
bool isPow(int n, int k){
	if(n == 1) return true;
	int mod = 1;
	REP(i,n-1){
		mod *= 2;
	}
	if(k % mod == mod - 1) return true;
	return false;
}
int main() {
	ifstream fin("A-large.in");
	ofstream fout("a-large.out");
	fin>>t;
	REP(test, t){
		fin>>N>>K;
		fout<<"Case #"<<(test+1)<<": "<<((isOn(N, K) && isPow(N, K))? "ON" : "OFF" )<<endl;
	}
    return 0;
}
