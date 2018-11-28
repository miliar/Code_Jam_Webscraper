#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;

int n;
int A[12345], B[12345];

int main() {
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) {
		scanf("%d", &n);
		FOR(i,0,n) scanf("%d%d", A + i, B + i);
		int count = 0;
		FOR(i,0,n) FOR(j,i+1,n) {
			if(A[i] < A[j] && B[i] > B[j]) ++count;
			if(A[i] > A[j] && B[i] < B[j]) ++count;
		}
		printf("Case #%d: %d\n", zzz + 1, count);
	}
	return 0;
}
