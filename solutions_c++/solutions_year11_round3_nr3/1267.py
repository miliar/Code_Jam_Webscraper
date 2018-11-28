#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

int case_num=0;
#define gout case_num++,cout<<"Case #"<<case_num<<": "

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;


void function();

int main() {
	int num_cases;
	cin>>num_cases;
	REP(i,num_cases)
		function();

	return 0;
}
void function(){
	int n,N,L,H;
	cin>>N; cin>>L; cin>>H;
	VI v;
	for(int i=0;i<N;i++) {
		cin>>n;
		v.push_back(n);
	}

	for(int i=L;i<=H;i++){
		bool res = true;
		for(int j=0;j<N;j++){
			if(v[j]%i != 0 && i%v[j] !=0) res = false;
		}
		if(res){
			gout<<i<<endl;
			return;
		}
	}
	gout<<"NO"<<endl;
}
