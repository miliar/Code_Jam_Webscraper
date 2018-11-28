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

string ReadString() {
	char Buffer[256];
	gets(Buffer);
	return string(Buffer);
}

int T[1234][1234];

int ReadInt() {
	char Buffer[256];
	gets(Buffer);
	int Val;
	sscanf(Buffer, "%d", &Val);
	return Val;
}

int main() {
	int N = ReadInt();
	FORTO(c,1,N) {
		
		int S = ReadInt();
		vector<string> Names(S);
		FOR(i,S) Names[i] = ReadString();		
		int Q = ReadInt();
		vector<string> Query(Q);
		FOR(i,Q) Query[i] = ReadString();
		
		FORD(i,S) T[Q][i] = 0;
		
		FORD(i,Q) FOR(j,S) {
			if (Query[i] == Names[j]) {
				int Min = INT_MAX;
				FOR(k,S) if (k != j) Min = min(Min,T[i+1][k]);
				T[i][j] = Min+1;
			} else {
				T[i][j] = T[i+1][j];
			}
		}
		
		int Min = INT_MAX;
		FOR(i,S) Min = min(Min,T[0][i]);
		
		printf("Case #%d: %d\n", c, Min);
	}
	return 0;
}
