#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>
#include <sstream>
using namespace std;
#define PB push_back
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for(__typeof((x).begin()) i=(x).begin();i != (x).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,w) memset((x),w,sizeof (x))
#define X first
#define Y second
typedef long long int lli;
typedef vector<int> VI;

int best[31][2],T,N,S,P,x;

int main(){ 
	//pre
	REP(i,11) REP(j,i+1) REP(k,j+1){
		int diff = i - k;
		if(diff > 2) continue;
		best[i+j+k][diff == 2] = max(best[i+j+k][diff == 2], i);
	}
	cin >> T;
	FOR(t,1,T){
		int res = 0;
		cin >> N >> S >> P;
		while(N--){
			cin >> x;
			int r1 = (best[x][1] >= P);
			int r0 = (best[x][0] >= P);
			if(S > 0 && r1 > r0){
				S--;
				res += r1;
			} else
				res += r0;
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	//in
	//sol
	//out
    return 0;
}
