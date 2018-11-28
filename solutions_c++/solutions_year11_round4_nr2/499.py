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

int C;

struct {
	ll x, y;
} DP[505][505];

int X, Y, D;
ll W[505][505];
ll I[505][505];

char buffer[505];

int main() {
	scanf("%d", &C);
	FORTO(c,1,C) {
		scanf("%d %d %d", &Y, &X, &D);
		FOR(y,Y) {
			scanf("%s", buffer);
			FOR(x,X) I[y][x] = buffer[x]-'0'+0;
		}
		FORTO(y,1,Y) FORTO(x,1,X) {
			DP[y][x].x = (x-1) * I[y-1][x-1] + DP[y-1][x].x + DP[y][x-1].x - DP[y-1][x-1].x;
			DP[y][x].y = (y-1) * I[y-1][x-1] + DP[y-1][x].y + DP[y][x-1].y - DP[y-1][x-1].y;
			 W[y][x]   =         I[y-1][x-1] +  W[y-1][x]    + W[y][x-1]    - W[y-1][x-1];
		}
		
		printf("Case #%d: ", c);
		
	//	ll Size = 5, x = 6, y = 6;
		
		
		FORDTO(Size,min(X,Y),3) {
			FORTO(y,Size,Y) FORTO(x,Size,X) {
				
				ll SumX = DP[y][x].x - DP[y-Size][x].x - DP[y][x-Size].x + DP[y-Size][x-Size].x;
				ll SumY = DP[y][x].y - DP[y-Size][x].y - DP[y][x-Size].y + DP[y-Size][x-Size].y;
				ll SumW =  W[y][x]   -  W[y-Size][x]   -  W[y][x-Size]   +  W[y-Size][x-Size];
				SumX -= (x-1) * (I[y-1][x-1] + I[y-Size][x-1]) + (x-Size) * (I[y-1][x-Size] + I[y-Size][x-Size]);
				SumY -= (y-1) * (I[y-1][x-1] + I[y-1][x-Size]) + (y-Size) * (I[y-Size][x-1] + I[y-Size][x-Size]);
				SumW -= I[y-1][x-1] + I[y-1][x-Size] + I[y-Size][x-1] + I[y-Size][x-Size];

				if (SumX * 2 != SumW*(2ll*x-(Size+1))) continue;
				if (SumY * 2 != SumW*(2ll*y-(Size+1))) continue;
				
			//	DEBUG(x);
			//	DEBUG(y);
			//	DEBUG(SumX);
			//	DEBUG(SumY);
			//	DEBUG(SumW);
				
				printf("%d\n", Size);
				goto next;
			}
		}
		
		printf("IMPOSSIBLE\n");
		next:;
	}
	return 0;
}
