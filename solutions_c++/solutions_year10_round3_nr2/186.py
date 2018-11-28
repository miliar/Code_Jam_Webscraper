#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define FORE(i,a,b) for (int (i)=(a);(i)<=(b);++(i))
#define FOREACH(it,v) for (typeof((v).begin()) it=(v).begin();(it)!=(v).end();++(it))
#define ALL(v) v.begin(),v.end()
#define MSET(v,x) memset((v),(x),sizeof((v)))

typedef double D;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef set<int> SI;
typedef vector<int> VI;
typedef vector<double> VD;
typedef map<int,int> MII;
typedef long long ll;

int main () {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		ll L,P,C;
		cin >> L >> P >> C;
		ll ret=0;
		while(L*C<P) {
			C*=C;
			ret++;
		}
		cout << "Case #"<<t<<": "<< ret << endl;
	}
}
