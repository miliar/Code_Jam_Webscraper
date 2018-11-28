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

#define MAXN 55
char S[MAXN][MAXN];

const int dx[4] = {
	+1, +1, 0, -1
};
const int dy[4] = {
	0, +1, +1, +1
};

int main() {
	int T;
	scanf("%d", &T);
	FORTO(t,1,T) {
		int N, K;
		scanf("%d %d", &N, &K);
		FOR(y,N) {
			scanf("%s", S[y]);
			int j = N;
			FORD(x,N) {
				if (S[y][x] != '.')
					swap(S[y][x],S[y][--j]);
			}
		}
		
		int LR = 0, LB = 0;
		
		FOR(y,N) FOR(x,N) if (S[y][x] != '.') FOR(i,4) {
			int l = 0, px = x, py = y;
			while (px >= 0 && px < N && py < N && S[py][px] == S[y][x])
				px += dx[i], py += dy[i], l++;
			if (S[y][x] == 'R') LR = max(LR,l);
			if (S[y][x] == 'B') LB = max(LB,l);
		}
		
		printf("Case #%d: ", t);
		if (LR >= K && LB >= K)
			printf("Both\n");
		else if (LR >= K)
			printf("Red\n");
		else if (LB >= K)
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}
