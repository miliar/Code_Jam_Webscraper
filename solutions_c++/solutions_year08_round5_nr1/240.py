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

char A[1008][1008];
char B[1008][1008];
char V[1008][1008];

#define X 3003

int dx[4] = { 0, +1, 0, -1 };
int dy[4] = { -1, 0, +1, 0 };
int px1[1008][1008];
int px2[1008][1008];
int py1[1008][1008];
int py2[1008][1008];

int main() {
	int C;
	scanf("%d", &C);
	FORTO(c,1,C) {
		int L;
		memset(A,0,sizeof(A));
		memset(B,0,sizeof(B));
		memset(V,0,sizeof(V));
		memset(px1,0,sizeof(px1));
		memset(px2,0,sizeof(px2));
		memset(py1,0,sizeof(py1));
		memset(py2,0,sizeof(py2));
		
		
		scanf("%d", &L);
		int x = 503, y = 503, d = 0;
		FOR(i,L) {
			char S[256];
			int T;
			scanf("%s %d", S, &T);
			int Len = strlen(S);
			FOR(j,T) FOR(k,Len)
					switch (S[k]) {
						case 'F': {
							switch (d) {
								case 0: y--; A[y][x] = 1; break;
								case 1: B[y][x] = 1; x++; break;
								case 2: A[y][x] = 1; y++; break;
								case 3: x--; B[y][x] = 1; break;
							}
							break;
						}
						case 'L': d = (d+3) & 3; break;
						case 'R': d = (d+1) & 3; break;
					}
		}
			
			queue<int> Q;
			Q.push(1);
			Q.push(1);
			while (!Q.empty()) {
				
				int x = Q.front(); Q.pop();
				int y = Q.front(); Q.pop();
				
				if (x < 1 || x > 1006 || y < 1 || y > 1006) continue;
				if (!V[y][x]) {
					V[y][x] = 1;
					// 0
					if (!B[y][x]) {
						Q.push(x);
						Q.push(y-1);
					}
					// 1
					if (!A[y][x+1]) {
						Q.push(x+1);
						Q.push(y);
					}
					// 2
					if (!B[y+1][x]) {
						Q.push(x);
						Q.push(y+1);
					}
					// 3
					if (!A[y][x]) {
						Q.push(x-1);
						Q.push(y);
					}
				}
			}
		FOR(y,1006) {
			FOR(x,1005) {
				if (A[y][x]) px1[y][x] = 1;
				if (px1[y][x]) px1[y][x+1] = 1;
			}
			FORD(x,1005) {
				if (A[y][x+1]) px2[y][x] = 1;;
				if (px2[y][x+1]) px2[y][x] = 1;
			}
		}
		FOR(x,1006) {
			bool ok1 = false;
			FOR(y,1005) {
				if (B[y][x]) ok1 = true;
				if (ok1) py1[y][x] = 1;
			}
			FORD(y,1005) {
				if (B[y+1][x]) py2[y][x] = 1;
				if (py2[y+1][x]) py2[y][x] = 1;
			}
		}
		
		int area = 0;
		int cx = 0;
		FOR(y,1005) FOR(x,1005) {
			if (V[y][x]) {
				if (px1[y][x] && px2[y][x]) {
					area++;
				} else if (py1[y][x] && py2[y][x]) {
					area++;
				}
			}
		}
		
		printf("Case #%d: %d\n", c, area);
	}
	return 0;
}
