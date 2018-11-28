#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#define maxn 103
using namespace std;


int main()
{
    freopen("C-small-attempt0 (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    int A,B,i,j,k,t,b;
    int cas = 1;
    int a[10];
    scanf("%d",&t);
    while (t--)
    {
        int ct = 0;
        scanf("%d%d",&A,&B);
        for (i = A; i <= B; ++i)
        {
            int tmp = i;
            int len = 0;
            while (tmp != 0)
            {
                a[len++] = tmp%10;
                tmp /= 10;
            }
            for (j = len - 2; j >= 0; --j)
            {
                int sum = 0;
                for (k = j,b = 0; b < len; ++b,--k)
                {
                    sum = sum*10 + a[(k + len)%len];
                }
                if (sum > i && sum <= B)
                ct++;
            }
        }
        printf("Case #%d: %d\n",cas++,ct);
    }
    return 0;
}
