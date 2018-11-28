#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int N, op = 1, ot = 0, bp = 1, bt = 0, t = 0;
		scanf("%d",&N);
		for(int i=0;i<N;++i) {
			char r;
			int p;
			scanf(" %c%d",&r,&p);
			if(r == 'O') {
				int dp = abs(p - op);
				if(dp <= t - ot) dp = 0;
				else dp -= (t - ot);
				ot = t = t + dp + 1;
				op = p;
			}
			else {
				int dp = abs(p - bp);
				if(dp <= t - bt) dp = 0;
				else dp -= (t - bt);
				bt = t = t + dp + 1;
				bp = p;
			}
		}
		printf("Case #%d: %d\n",cn,t);
	}
}
