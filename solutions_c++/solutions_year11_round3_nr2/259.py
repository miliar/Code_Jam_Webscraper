#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define maxn 1000010
int T;
int cs;
long long int L,N,C;
long long int t;
long long int c[maxn];
long long int a[maxn];
long long int aa[maxn];
int main()
{
    long long int i;
    int cnt;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    while(scanf("%d",&T)!=EOF)
    {
        cs = 1;
        long long int ans;
        long long int tmp;
        long long int sum;
        int flag,p,tt;
        while(T--)
        {
            ans = 0;
            sum = 0;
            scanf("%lld%lld",&L,&t);
            scanf("%lld%lld",&N,&C);
            for(i = 0 ; i < C; i++)
            {
                scanf("%lld",&a[i]);
            }
            tmp = t/2;
            flag =0 ;
            tt = 0;

            for(i = 0; i < N ; i++)
            {
                c[i] = a[i%C];
                sum += c[i];
                if(tmp < sum && flag == 0)
                {
                    p = i;
                    c[i] = sum - tmp;
                    flag = 1;
                }
                if(flag)
                {
                    aa[tt++] = c[i];
                }
            }
           // for(i = 0; i < N ;i ++)
           //     printf("ddd %lld ",c[i]);
          //  printf("\n");
            sort(aa,aa+tt);
            ans = min(t,sum*2);
          //  printf("%lld\n",ans);
            cnt = 0;

            for(i = tt - 1 ; i >= 0 ; i--)
            {
           //     printf("%lld ",aa[i]);
                if(cnt < L)
                    ans += aa[i];
                else
                    ans += aa[i] * 2;
                cnt++;
            }
          //  printf("\n");
            printf("Case #%d: %lld\n",cs++,ans);
        }
    }
    return 0;
}
