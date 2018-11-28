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
bool solve(long long n, long long pd, long long pg){
	long long h = 100;
	long long g = __gcd(pd, 1LL * h);
	
	pd /= g, h /= g;
	//cout<<pd<<" "<<h<<endl;
	if(n < h) return false;
	long long k = n / h;
	
	long long D = k * h;
	long long win = D * pd / h;
	//cout<<win<<" "<<D<<endl;
	h = 100;
	g = __gcd(pg, 1LL * h);
	pg /= g, h /= g;
	while(h != 0 && h <= D){
		h *= 2, pg *= 2;
	}
	while(pg != 0 && pg <= win){
		pg *= 2, h *= 2;
	}
	while(h != 0 && h <= D){
		h *= 2, pg *= 2;
	}
	while(pg != 0 && pg <= win){
		pg *= 2, h *= 2;
	}
	int cnt = 0;
	while(cnt < 20 && (h - pg) < (D - win)){
		if(h < 0 || pg < 0) return false;
		if(pg >= win && (h - pg) >= (D - win)) return true;
		h *= 2, pg *=2;
		cnt ++;
	}
	if(h < 0 || pg < 0) return false;
	if(pg >= win && (h - pg) >= (D - win)) return true;
	//cout<<D<<" "<<win<<" "<<h<<" "<<pg<<endl;
	
	//cout<<pg<<" "<<h<<endl;
	return false;
}
int main() {
	//freopen("A-small-attempt0.in", "r", stdin); 
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt22.out", "w", stdout);
	//freopen("A-small-attempt3.in", "r", stdin); freopen("A-small-attempt3.out", "w", stdout);
	
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	
	int nT;
	cin>>nT;
	for (int t=1; t<=nT; t++) {
		printf("Case #%d: ", t);
		long long N, PD, PG;
		cin>>N>>PD>>PG;
		if(solve(N, PD, PG)){
			cout<<"Possible"<<endl;
		}
		else{
			cout<<"Broken"<<endl;
		}
		//cout<<)<<endl;
	}
	return 0;
}
