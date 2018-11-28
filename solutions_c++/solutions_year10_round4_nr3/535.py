#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <sstream>
#include <bitset>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned long long UL;
typedef long double LD;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000+1;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b); x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for (VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

void scase() {
	int r;
	int N = 102;
	VVI b(N,VI(N));
	scanf("%d",&r);
	REP(i,r) {
		int x1, y1, x2, y2;
		scanf("%d%d%d%d",&x1, &y1, &x2, &y2);
		FOR(ii, y1, y2+1) FOR( jj, x1, x2+1) 
			b[ii][jj]=1;
	}
	queue<int > q, qb;
	FOR (i,1, N) FOR (j,1,N) if (b[i][j] && !b[i-1][j] && !b[i][j-1]) q.push(i*N+j);
	FOR (i,1, N) FOR (j,1,N) if (!b[i][j] && b[i-1][j] && b[i][j-1]) qb.push(i*N+j);

	int cnt=0;
	queue<int> nq, nqb;
	while (!q.empty() || !qb.empty()) {
		cnt++;
		while (!q.empty()) {
			int x=q.front()/N, y=q.front()%N;
//			printf("(%d, %d) ",x,y);
			q.pop();
			b[x][y]=0;
			if (b[x+1][y] && !b[x+1][y-1]) nq.push((x+1)*N+y);
			if (b[x][y+1] && !b[x-1][y+1]) nq.push((x*N+y+1));
		}
		while (!qb.empty()) {
			int x=qb.front()/N, y=qb.front()%N;
//			printf("(%d, %d) ",x,y);
			qb.pop();
			b[x][y]=1;
			if (!b[x+1][y] && b[x+1][y-1]) nqb.push((x+1)*N+y);
			if (!b[x][y+1] && b[x-1][y+1]) nqb.push((x*N+y+1));
		}
//		printf("\n");
		swap(nq,q);
		swap(nqb,qb);
	}
	printf("%d\n",cnt);

}

int main() {
	int z;
	scanf("%d",&z);
	REP(i,z) {
		printf("Case #%d: ",i+1);
		scase();
	}

	return 0;
}
