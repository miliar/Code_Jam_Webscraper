#include <iostream>
#include <vector>
#include <cstdio>
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

typedef vector<int> VI;

int main() {
	int T;
	cin >> T;
	FORE(t,1,T) {
		int n,s,p;
		cin >> n >> s >> p;
		int ret=0;
		REP(i,n) {
			int x;
			cin >> x;
			int mn1=x/3;
			int mx1=mn1;
			if (x%3) mx1++;
			if (mx1>=p) ret++;
			else if (s && x>=2 && x<=28) {
				int mn2=(x-2)/3;
				int mx2=mn2+2;
				if (mx2>=p) {
					ret++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n",t,ret);
	}
}

