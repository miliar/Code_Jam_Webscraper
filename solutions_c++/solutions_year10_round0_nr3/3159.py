/* 
 * File:   main.cpp
 * Author: ubuntu
 *
 * Created on 2010年5月9日, 上午12:55
 */

#include <stdio.h>
#include <string.h>

typedef long long ll;
const int MAXN = 1001;

ll g[MAXN];

ll R, K, N;


int find(int &ptr)
{
    int i;
    int ret = 0;
    for(i = 0; i < N; i++)
    {
        if(ret+g[(ptr+i)%N] > R) break;
        ret += g[(ptr+i)%N];
    }
    ptr = (i+ptr)%N;
    return ret;
}

int main()
{
freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
    int T, CAS = 1;
    int  i, j;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%lld %lld %lld", &K, &R, &N);
        //printf("K = %lld\n", K);
        for(i = 0; i < N; i++)
        {
            scanf("%lld", &g[i]);
            //if(i) g[i] += g[i-1];
        }
        printf("Case #%d: ", CAS++);
        /*
        if(g[N-1] <= R)
        {
            printf("%lld\n", g[N]*K);
            continue;
        }
         * */
        int p = 0;
        int k = 0;
        ll cnt = 0;
        while(k < K)
        {
            k++;
            cnt += find(p);
            
            if(p == 0) break;
        }
        if(k < K)
        {
            cnt = cnt*(K/k);
            K %= k;
            while(K--)
            {
                cnt += find(p);
            }
        }
        printf("%lld\n", cnt);
    }
    return 0;
}

