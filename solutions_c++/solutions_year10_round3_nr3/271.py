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

int M, N;
int B[33][33];
int C[33];

bool check(int a, int b, int s) {
	FOR(i,a,a+s) FOR(j,b,b+s) {
		if(B[i][j] == -1) return false;
		if(i != a) {
			if(B[i - 1][j] == B[i][j]) return false;
		}
		if(j != b) {
			if(B[i][j - 1] == B[i][j]) return false;
		}
	}
	FOR(i,a,a+s) FOR(j,b,b+s) B[i][j] = -1;
	return true;
}

int main() {
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) {
		scanf("%d%d", &M, &N);
		int N4 = N / 4;
		FOR(i,0,M) FOR(j,0,N) B[i][j] = 0;
		FOR(i,0,33) C[i] = 0;
		FOR(i,0,M) {
			char str[11];
			scanf("%s", str);
			FOR(j,0,N4) {
				int k = 0;
				if('A' <= str[j] && str[j] <= 'F') {
					k = 10 + int(str[j] - 'A');
				} else k = int(str[j] - '0');
				if(k & 1) B[i][4 * j + 3] = 1;
				if(k & 2) B[i][4 * j + 2] = 1;
				if(k & 4) B[i][4 * j + 1] = 1;
				if(k & 8) B[i][4 * j + 0] = 1;
			}
		}
		FORD(v,33,1) {
			FOR(i,0,M-v+1) FOR(j,0,N-v+1) {
				if(check(i, j, v)) {
					++C[v];
					FOR(x,0,v) FOR(y,0,v)
						B[i + x][j + y] = -1;
				}
			}
		}
		int res = 0;
		FOR(i,1,33) if(C[i]) ++res;
		printf("Case #%d: %d\n", zzz + 1, res);
		FORD(i,33,1) if(C[i]) printf("%d %d\n", i, C[i]);
	}
	return 0;
}
