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

#define LOG 20
#define MAX (1<<LOG)

int S[2*MAX];

int get(int Sum) {
	int v = 1;
	FOR(i,LOG)
		if (S[2*v+0] >= Sum) {
			v = 2*v+0;
		} else {
			Sum -= S[2*v+0];
			v = 2*v+1;
		}
	return v - MAX;
}

void Set(int Pos) {
	S[Pos+=MAX]--;
	FOR(i,LOG)
		S[Pos/=2]--;
}

int getSum(int Pos) {
	int Sum = S[Pos += MAX];
	FOR(i,LOG) {
		if (Pos&1) Sum += S[Pos-1];
		Pos /= 2;
	}
	return Sum;
}

int X[MAX];

int main() {
	int C, K, N, P;
	scanf("%d", &C);
	FORTO(c,1,C) {
		FORD(i,MAX) S[MAX+i] = 1;
		FORD(i,MAX) S[i] = S[2*i+0] + S[2*i+1];
		scanf("%d %d", &K, &N);
		int last = 0;
		FOR(i,K) {
			P = get((i+last)%(K-i)+1);
			X[P] = i+1;
			Set(P);
			last = getSum(P);
		}
		printf("Case #%d:", c);
		FOR(i,N) {
			scanf("%d", &P);
			printf(" %d", X[P-1]);
		}
		printf("\n");
	}
	return 0;
}
