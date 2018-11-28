#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int T, N;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        scanf("%d", &N);
        int cnt = 0, m;
        for(int i = 0; i < N; i++){
            scanf("%d", &m);
            if(m!=i+1)cnt++;
        }
        printf("Case #%d: %d\n", cas, cnt);
    }
    
    return 0;
}
