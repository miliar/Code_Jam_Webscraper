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


int GCD(int a, int b) {
	return b ? GCD(b,a%b) : a;
}

int P[1024];

int Parent(int a) {
	return P[a] = (P[a]==a ? a : Parent(P[a]));
}

void Union(int a, int b) {
	if (Parent(a) != Parent(b))
		P[Parent(a)] = Parent(b);
}

// Erstratovo sito na vypocet prvocisel O(N log N)
vector<bool> Sieve(int N) {
	vector<bool> S(N, true);
	S[0] = S[1] = false;
	for (int i = 2; i * i < N; i++)
		if (S[i])
			for (int j = i * i; j < N; j += i)
				S[j] = false;
	return S;
}


int main() {
	int C;
	scanf("%d", &C);
	FORTO(c,1,C) {
		int A, B, R, X = 0;
		scanf("%d %d %d", &A, &B, &R);
		vector<bool> S = Sieve(B+1);
		FORTO(i,A,B) P[i] = i;
		FORTO(i,R,B)
			if (S[i])
				for (int j = i; j <= B; j += i)
					if (A <= j && j + i <= B)
						Union(j,j+i);
		FORTO(i,A,B) if (P[i] == i) X++;
		printf("Case #%d: %d\n", c, X);
	}
	return 0;
}
