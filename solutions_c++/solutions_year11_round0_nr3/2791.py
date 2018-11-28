#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>
using namespace std;
int main()
{
    int n,t,minn;
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    int i,j,num;
    int sum,sum1;
    for (i = 1;i <= t;i++){
        scanf("%d",&n);
        minn = 10000000;
        sum = 0;sum1 = 0;
        for (j = 0;j < n;j++){
            scanf("%d",&num);
            if (minn > num)
                minn = num;
            sum += num;
            sum1 ^= num;
        }
        if (sum1 == 0){
            printf("Case #%d: %d\n",i,sum-minn);
        }
        else{
            printf("Case #%d: NO\n",i);
        }
    }
    return 0;
}
