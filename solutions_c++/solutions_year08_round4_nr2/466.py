#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int N, M, A;

int main()
{
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d %d %d", &N, &M, &A);
		bool found = false;
		for (int a = 0; a <= N && !found; ++a) {
			for (int b = 0; b <= M && !found; ++b) {
				if (a == 0 && b == 0)
					continue;
				for (int c = 0; c <= N && !found; ++c) {
					for (int d = 0; d <= M && !found; ++d) {
						if ((c==0&&d==0) || (c==a||d==b) || (a*d-b*c==0))
							continue;
						double aa = hypot(a,b);
						double bb = hypot(c,d);
						double cc = hypot(abs(a-c),abs(b-d));
						if (aa < bb) swap(aa,bb);
						if (aa < cc) swap(aa,cc);
						if (bb < cc) swap(bb,cc);
						double area;
						double S;
						S = (aa+bb+cc) / 2.0;
						area = sqrt(S*(S-aa)*(S-bb)*(S-cc));
						//area = 0.25 *
							//sqrt( (aa+(bb+cc))*
								//(cc-(aa-bb))*
								//(cc+(aa-bb))*
								//(aa+(bb-cc))
							//);
						if (abs(2*area-A) > 1.0e-8)
							continue;
						found = true;
						//printf("%lf %lf %lf %lf\n", S, aa, bb, cc);
						printf("Case #%d: 0 0 %d %d %d %d\n", tt, a, b, c, d);
					}
				}
			}
		}
		if (!found)
			printf("Case #%d: IMPOSSIBLE\n", tt);
	}

	return 0;
}
