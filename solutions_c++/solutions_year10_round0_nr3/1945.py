#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std ;

long long arr[1005];
long long flag[1005];
long long sums[1005];
long long R,n;
long long k;

int main()
{
//    FILE *in=fopen("park.in","r");
    freopen("park.in","r",stdin);
    freopen("park.out","w",stdout);
    int c,c2;
    int tests;
    cin>>tests;
    int testn=1;
    while (tests)
    {
        memset(flag,-1,sizeof(flag));
        printf("Case #%d: ",testn);
        testn++;
        tests--;
//        fscanf(in,"%d%lld%d",&R,&k,&n);
        cin>>R>>k>>n;
        for (c=0;c<n;c++)cin>>arr[c];
        long long cnt=0;
        long long ret=0;
        long long cnt2=0;
        while (flag[cnt]==-1&&cnt2<R)
        {
            flag[cnt]=cnt2;
            long long sum=arr[cnt];
            if (sum>k)
            {
                sums[cnt2]=0;
                cnt2++;
                continue;
            }
            for (c=(cnt+1)%n;c!=cnt&&sum+(long long)arr[c]<=k;sum+=(long long)arr[c],c++,c%=n);
            cnt=c;
            sums[cnt2]=sum;
            ret+=sum;
            cnt2++;
        }
        long long i=flag[cnt];
        long long sum=0;
        for (c=i;c<cnt2;c++)sum+=sums[c];
        ret+=sum*((long long)(R-cnt2)/(long long)(cnt2-i));
        long long howmany=(R-cnt2)%(cnt2-i);
        for (c=i;c<cnt2&&howmany;c++,howmany--)ret+=sums[c];
        cout<<ret<<endl;
    }
//    system("pause");
    return 0;
}
























