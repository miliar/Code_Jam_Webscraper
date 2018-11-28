#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair((a),(b))
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define debug if(1)printf

#define MOD(x,m) ((x)%(m))
#define MAXT 1000000007

int n, m;
LL X, Y, Z;
LL t[500*1001];
LL v[500*1001];
LL A[500*1001];

int main() {
	int ncaso;
	scanf(" %d", &ncaso);
	FOR(icaso, 1, ncaso) {
		printf("Case #%d: ", icaso);
		cin >> n >> m >> X >> Y >> Z;
		
		REP (i, m) cin >> A[i];
		REP (i, n) {
			//cout << "X*A=" << X*A[i%m] << " Y*(i+1)=" <<Y * (i+1)<<" A="<<(X * A[i%m] + Y * (i+1))<<endl;
			v[i]=A[i%m];
			//A[i%m]=(X * A[i%m] + Y * (i+1))%Z;
			A[i%m]=(MOD(MOD(X,Z) * MOD(A[i%m],Z),Z) + MOD(MOD(Y,Z) * MOD((i+1),Z),Z))%Z;
		}
		//REP(i, n) printf("v[%d]=%d\n", i, v[i]);
		LL tot=1;
		t[n-1]=1;
		for (int i=n-2; i>=0; i--) {
			t[i]=1;
			for (int j=i+1; j<n; j++) {
				if (v[j]>v[i]) {t[i]+=t[j]; t[i]=t[i]%MAXT;}
			}
			//printf("t[%d]=%d\n", i, t[i]);
			tot=MOD(tot+t[i],MAXT);
		}
		cout << tot << endl;
	}

	return 0;
}
