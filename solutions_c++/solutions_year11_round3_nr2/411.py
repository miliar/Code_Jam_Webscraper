#include<iostream>
using namespace std;
int len[1011010];
int tt[1010101];
int c[1010];
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
        long long l,t,n,C;
        scanf("%I64d%I64d%I64d%I64d",&l,&t,&n,&C);
        for(int i=0;i<C;i++)
        scanf("%d",&c[i]);
        int p=0;
        long long all=0;
        for(int i=0;i<n;i++)
        {
            len[i]=c[p];
            p++;
            p%=C;
            all+=len[i];
        }
        long long need=t/2;
        p=0;
        long long sum=0;
        long long res=0;
        bool judge=false;
        for(int i=0;i<n;i++)
        {
            sum+=len[i];
            if(sum>=need)
            {
                tt[i]=sum-need;
                for(int j=i+1;j<n;j++)
                {
                    tt[j]=len[j];
                }
                sort(tt+i,tt+n,greater<int>());
                if(n-i<=l)
                {
                    long long temp=0;
                    for(int j=i;j<n;j++)
                    temp+=tt[j];
                    res=(all-temp)*2+temp;
                }
                else
                {
                    long long temp=0;
                    for(int j=0;j<l;j++)
                    temp+=tt[i+j];
                    res=(all-temp)*2+temp;
                }
                judge =true;
                break;
            }
        }
        if(!judge)
        res=all*2;
        printf("Case #%d: %I64d\n",ca,res);
    }
}
