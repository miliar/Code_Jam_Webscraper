// Headers {{{
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
template<typename Q> inline int size(Q a) { return a.size(); }
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

int k;
string s;
VI v;

int calc() {
	string s2=s;
	for(int i=0; i<size(s2); i+=k) {
		string s3=s2.substr(i,k);
		for(int j=0; j<k; ++j) s2[i+j]=s3[v[j]];
	}
	int res=1;
	FOR(i,1,size(s2)-1) if(s2[i]!=s2[i-1]) ++res;
	return res;
}

int main() {
	int ntc;
	scanf("%d",&ntc);
	FOR(tc,1,ntc) {
		scanf("%d",&k);
		char buf[1001];
		scanf("%s",buf);
		s=buf;
		v.clear();
		REP(i,k) v.push_back(i);
		int res=INF;
		do {
			int cur=calc();
			res=min(res,cur);
		} while(next_permutation(ALL(v)));
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}
