#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
#define MAX(x, y) ((x)>(y)?(x):(y))

typedef long long LL;


int D, C, P[1000], V[1000];
LL len[1000];
LL sv;
bool ok(LL t)
{
    LL r = -(1LL << 50);
    
    int i;
    for(i = 0; i < C; ++i)
    {
        if(len[i] > t) 
        { return 0; }
        r = MAX(len[i] * 2 + r, len[i] * 2 + 2 * P[i] - t);
        if(r - P[i] * 2 > t) 
        {
            return 0;
        }
        r += D  * 2;
    }
    return 1;
}
LL exec()
{
    LL s = -1, e = 1000001;
    
    while(s + 1 < e)
    {
        LL m = (e + s) / 2;
		if(ok(m)) {
			e = m;
		} else {
			s = m;
		}
    }
    return e;
}
int main()
{
    freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int i, j, k;
    int T, c = 0;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d%d", &C, &D);
        for(i = 0; i < C; ++i) {
            scanf("%d%d", &P[i], &V[i]);
            len[i] = ((LL)(V[i] - 1) ) * D;
        }
        
        LL res = exec();
        printf("Case #%d: ", ++c);
		if(res % 2 == 1) {
			printf("%lld.5\n", res / 2);
		} else {
			printf("%lld.0\n", res / 2);
		}
    }
	return 0;
}
