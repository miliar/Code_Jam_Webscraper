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

#define MAXM 12345
#define INF 1000000

// 1 = AND

int T[MAXM][2];
int G[MAXM];
int C[MAXM];

void WithAND(int i, int Add) {
	int L = 2*i+0;
	int R = 2*i+1;
	T[i][1] = min(T[i][1], T[L][1] + T[R][1] + Add);
	T[i][0] = min(T[i][0], T[L][0] + T[R][0] + Add);
	T[i][0] = min(T[i][0], T[L][0] + T[R][1] + Add);
	T[i][0] = min(T[i][0], T[L][1] + T[R][0] + Add);
}

void WithOR(int i, int Add) {
	int L = 2*i+0;
	int R = 2*i+1;
	T[i][1] = min(T[i][1], T[L][1] + T[R][1] + Add);
	T[i][1] = min(T[i][1], T[L][0] + T[R][1] + Add);
	T[i][1] = min(T[i][1], T[L][1] + T[R][0] + Add);
	T[i][0] = min(T[i][0], T[L][0] + T[R][0] + Add);
}

int main() {
	int N;
	scanf("%d", &N);
	FORTO(c,1,N) {
		int M, V, A;
		scanf("%d %d", &M, &V);
		int IN = (M-1)/2;
		FORTO(i,1,IN)
			scanf("%d %d", &G[i], &C[i]);
		FORTO(i,IN+1,M) {
			scanf("%d", &A);
			T[i][A] = 0;
			T[i][A^1] = INF;
		}
		for (int i = IN; i > 0; i--) {
			T[i][0] = T[i][1] = INF;
			if (G[i]) { // and
				WithAND(i,0);
				if (C[i]) WithOR(i,1);
			} else {
				WithOR(i,0);
				if (C[i]) WithAND(i,1);
			}
		}
		printf("Case #%d: ", c);
		if (T[1][V] == INF)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", T[1][V]);
	}
	return 0;
}
