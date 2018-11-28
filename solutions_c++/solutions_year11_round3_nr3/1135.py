#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#define MAXN 10005
#include <cstdlib>
using namespace std;
int num[MAXN];
int tt, n, l, h, flag, mm;


int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &tt);
    for(int t=1; t<=tt; t++)
    {
        printf("Case #%d: ", t);
        scanf("%d", &n);
        scanf("%d%d", &l, &h);
        for(int i=0; i<n; i++)
        {
            scanf("%d", &num[i]);
        }
        for(int i=l; i<=h; i++)
        {
            flag=1;
            for(int j=0; j<n; j++)
            {
                if(num[j]<i)
                {
                    if(i%num[j]!=0) flag=0;
                }
                else
                {
                    if(num[j]%i!=0) flag=0;
                }
            }
            if(flag) {mm=i;break;}
        }
        if(flag==0) printf("NO\n");
        else printf("%d\n", mm);
    }
    return 0;
}
