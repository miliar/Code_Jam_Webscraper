#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
using namespace std;

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a-1); i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
typedef long long LG;

LG n, A, B, C, D, _x0, _y0, M;
LG tx[105], ty[105];

int main() {
	int T;
	scanf("%d", &T);
	for(int z=1; z<=T; ++z) {
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &_x0, &_y0, &M);
		tx[0] = _x0; ty[0] = _y0;
		FOR(i,1,n) {
			tx[i] = (A*tx[i-1] + B) % M;
			ty[i] = (C*ty[i-1] + D) % M;
		}
		int counter = 0;
		FOR(i,0,n)
			FOR(j,i+1,n)
				FOR(k,j+1,n) {
					if((tx[i] + tx[j] + tx[k])%3 == 0 &&
					   (ty[i] + ty[j] + ty[k])%3 == 0)
						++counter;
				}
		printf("Case #%d: %d\n", z, counter);
	}
	return 0;
}
