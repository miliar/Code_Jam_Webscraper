// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long int ll;
typedef long double ld;
typedef pair<ld,ld> PDD;
typedef pair<ll,ll> PLL;

#define FOR(i,n)      for(int i=0;i<n;i++)
#define FORTO(i,a,b)  for(int i=a;i<=b;i++)
#define FORD(i,n)     for(int i=n-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=b;i>=a;i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define $ size()
#define ALL(x) (x).begin(),(x).end()
#define PB push_back

//template<class T> T min(T a, T b) { return a < b ? a : b; }
//template<class T> T max(T a, T b) { return a > b ? a : b; }

int FindPairing(vector<PII> V) {
	sort(V.begin(), V.end());
	int Arrivals = 0, Pairing = 0;
	FOR(i,int(V.$))
		if (V[i].second < 0)
			Arrivals++;
		else if (Arrivals > 0)
			Pairing++, Arrivals--;
	return Pairing;
}

int LoadTime() {
	int H, M;
	scanf("%d:%d", &H, &M);
	return H*60+M;
}

int main() {
	int N;
	scanf("%d", &N);
	FORTO(c,1,N) {
		int Delay, NA, NB;
		vector<PII> A, B;
		scanf("%d %d %d", &Delay, &NA, &NB);
		FOR(i,NA) {
			A.PB(PII(LoadTime(),+1));
			B.PB(PII(LoadTime()+Delay,-1));
		}
		FOR(i,NB) {
			B.PB(PII(LoadTime(),+1));
			A.PB(PII(LoadTime()+Delay,-1));
		}
		printf("Case #%d: %d %d\n", c, NA - FindPairing(A), NB - FindPairing(B));
	}
	return 0;
}
