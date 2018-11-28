#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int T, N, K;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &T);
    for(int cas = 1; cas<=T; cas++){
        scanf("%d %d", &N, &K);
        int m = K % (1<<N);
        printf("Case #%d: ", cas);
        if(m == (1<<N)-1)puts("ON");
        else puts("OFF");
    }
    return 0;
}
