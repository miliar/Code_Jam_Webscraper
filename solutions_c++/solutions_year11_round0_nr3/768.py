#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int T, C, N;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        int mi = 1<<30, xo = 0, sum = 0;
        scanf("%d", &N);
        while(N--){
            scanf("%d", &C);
            xo ^= C;
            sum += C;
            if(C < mi) mi = C;
        }
        printf("Case #%d: ", cas);
        if(xo) printf("NO\n");
        else printf("%d\n", sum - mi);
    }
    return 0;
}
