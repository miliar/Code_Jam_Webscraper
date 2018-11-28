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

void resample(VI& v) {
	VI w=v;
	sort(ALL(w));
	MII m;
	FOR(i,0,w.size()) {
		m[w[i]]=i;
	}
	FOR(i,0,v.size()) v[i]=m[v[i]];
}

int main () {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		int N;
		cin >> N;
		VI A(N),B(N);
		FOR (i,0,N) {
			cin >> A[i] >> B[i];
		}
		resample(A);
		resample(B);
		int count=0;
		FOR (i,0,N) {
			int d=B[i]-A[i];
			if (d>0) count+=d;
		}
		cout << "Case #"<<t<<": "<< count << endl;
	}
}
