//C: Candy splitting
#include<cstdio>
#include<memory.h>

using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    int a[1001];
    for (int num=1; num<=T; ++num)
    {
        int n;
        scanf("%d",&n);
        memset(a,0,sizeof(a));
        int i,flag=0,sum=0,min=1000001;
        for (i=0; i<n; ++i)
        {
            scanf("%d",a+i);
            flag ^= a[i];
            sum += a[i];
            if (a[i]<min)
                min = a[i];
        }
        if (flag)
            printf("Case #%d: NO\n",num);
        else
            printf("Case #%d: %d\n",num,sum-min);
    }
    return 0;
}

