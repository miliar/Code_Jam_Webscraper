#include <cstdio>

using namespace std;
#define MAXN 1024
int arr[MAXN];
int main()
{
    int T,N,round=1;
    long long sum;
    int tsum=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&arr[i]);
        }
        tsum=arr[0];
        for(int i=1;i<N;i++) tsum^=arr[i];
        if(tsum!=0)
        {
            printf("Case #%d: NO\n",round++);
            continue;
        }
        sum=0;
        int minVal=1000000;
        for(int i=0;i<N;i++)
        {
            if(arr[i]<minVal) minVal=arr[i];
            sum+=(long long)arr[i];
        }
        printf("Case #%d: %I64d\n",round++,sum-minVal);
    }
    return 0;
}
