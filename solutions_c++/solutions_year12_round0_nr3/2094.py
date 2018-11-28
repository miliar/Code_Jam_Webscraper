#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
#include <sstream>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define REPR(i,n) for(int i=(n-1);i>=0;--i)
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define FORR(i,z,n) for (int (i)=(n-1);(i)>=(z);--(i))
#define FOREACH(it,c) \
  for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define UNIQUE(x) remove(unique((x).begin(),(x).end()),(x).end())
#define CLEAR(x,v) memset((x),(v),sizeof((x)))
#define FORS(i,x) for(int i=0;i<(int)(x).size();i++)

typedef pair<int,int> PII;
typedef set<PII> SP;

int main() {
	SP allpairs;
	FORE(i,1,2000000) {
		stringstream ss; ss<<i;
		string s(ss.str());
		int n=s.size();
		FOR(j,1,n) {
			s=s.substr(1)+s[0];
			stringstream sss(s);
			int k;sss>>k;
			if (k<=i) continue;
			allpairs.insert(PII(i,k));
		}
	}
	int T;
	cin >> T;
	FORE(t,1,T) {
		int a,b;
		cin >> a >> b;
		int ret=0;
		FOREACH(it,allpairs) {
			if (it->first>=a && it->second<=b) ret++;
		}
		printf("Case #%d: %d\n",t,ret);
	}
}

