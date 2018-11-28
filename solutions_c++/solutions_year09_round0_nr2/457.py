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

const int dx[4] = { 0, -1, +1, 0 };
const int dy[4] = { -1, 0, 0, +1 };

#define MAX 123
#define INF 1000000

int T, X, Y, F;
int A[MAX][MAX];
int V[MAX][MAX];

int DFS(int x, int y) {
	if (V[y][x] != -1)
		return V[y][x];
	
	int j = -1, Min = A[y][x];
	FOR(i,4)
		if (Min > A[y+dy[i]][x+dx[i]])
			Min = A[y+dy[i]][x+dx[i]], j = i;
	
	if (j == -1)
		V[y][x] = F++;
	else
		V[y][x] = DFS(x+dx[j],y+dy[j]);
	
	return V[y][x];
}

int main() {
	scanf("%d", &T);
	FOR(k,T) {
		scanf("%d %d", &Y, &X);
		FOR(y,MAX) FOR(x,MAX) {
			A[y][x] = INF;
			V[y][x] = -1;
		}
		
		FORTO(y,1,Y) FORTO(x,1,X)
			scanf("%d", &A[y][x]);
		
		printf("Case #%d:\n", k+1);
		
		F = 0;
		FORTO(y,1,Y) {
			FORTO(x,1,X) {
				if (x > 1) putchar(' ');
				putchar(DFS(x,y) + 'a');
			}
			putchar('\n');
		}
	}
	return 0;
}
