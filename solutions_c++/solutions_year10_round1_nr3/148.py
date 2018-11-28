// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
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
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define SIZE(X) int(X.size())

bool get(int A, int B) {
	if (A > B) swap(A,B);
	if (!A) return true;
	bool res = get(B%A,A);
	if (res) {
		return (B/A) > 1;
	} else {
		return true;
	}
}

int main() {
	int C;
	scanf("%d", &C);
	FORTO(t,1,C) {
		int A1, A2, B1, B2, sum = 0;
		scanf("%d %d %d %d", &A1, &A2, &B1, &B2);
		FORTO(a,A1,A2) FORTO(b,B1,B2)
			if (get(a,b)) sum++;
		printf("Case #%d: %d\n", t, sum);
	}
	return 0;
}
