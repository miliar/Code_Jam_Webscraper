#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iterator> 
#include <algorithm> 
#include <utility> 

// container 
#include <vector> 
#include <string> 
#include <set> 
#include <map> 
#include <stack>
#include <queue>

// C-style 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <climits>
#include <cfloat>
#include <cassert>

using namespace std;

#define FOR(_I,_A,_B) for(int _I=(_A);(_I)<(_B);_I++)
#define FORE(_I,_A,_B) for(int _I=(ll)(_A);(_I)<=(_B);_I++) 
#define REP(_I,_B) for(int _I=(0);(_I)<(_B);_I++) 

typedef long long ll;
typedef long double ld;

struct point{
	int x, y;
	point() {}
	point(ll a, ll b) {
		x=a;
		y=b;
	}
	point(int a, int b) {
		x=a;
		y=b;
	}
};

ll area(point a, point b, point c) {
	return (a.x*b.y + b.x*c.y + c.x*a.y)-(a.y*b.x + b.y*c.x+c.y*a.x);
}
ll N, M, C, A;
point p[1000];
int main(void) {
	freopen("bs.in", "r", stdin);
	freopen("bs.out", "w", stdout);

	cin >> C;

	FORE(tc, 1, C) {
		cin >> N >> M >> A;

		//if(A*A > M) {
		//	printf("Case #%d: IMPOSSIBLE\n", tc); 
		//	continue;
		//}

		bool found=false;
		int x1=0, y1=0;
			FORE(x2, 0, N) FORE(y2, 0, M) {
				FORE(x3, 0, N) FORE(y3, 0, M) {
					ll AA = area(point(x1, y1), point(x2, y2), point(x3, y3));
					if(AA == A || AA==-A) {
						printf("Case #%d: %d %d %d %d %d %d\n", tc, x1, y1, x2, y2, x3, y3);
						found=true;
					}
					if(found) break;
				}
				if(found) break;
			}
			
		if(!found) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
	}
	return 0;
}
