#include <cstdio>

using namespace std;

long long T,N,L,H;
long long fArr[10000];
long long gcd(long long a,long long b);
long long gcd(long long a,long long b)
{
    if(a<b) return gcd(b,a);
    while(b!=0)
    {
        long long tmp=a%b;
        a=b;
        b=tmp;
    }
    return a;
}
bool checkGCD(long long &gcdV)
{
    if(gcdV<L) return false;
     if((gcdV%2)==0)
    {
            if(L<=2&&2<=H)
            {
                gcdV=2;
                return true;
            }
            while((gcdV&1)==0) gcdV>>=1;
    }
    long long t=3;
    while(gcdV>1)
    {
        if((gcdV%t)==0)
        {
            if(L<=t&&t<=H)
            {
                gcdV=t;
                return true;
            }
            while((gcdV%t)==0) gcdV/=t;
        }
        t+=2;
    }
    return false;
}
bool checkLCM(long long &lcmV)
{
    if(lcmV>H)
    {
        //
        return false;
    }
    else
    {
        long long dur=lcmV;
        while(lcmV<L)
        {
            lcmV+=dur;
        }
        if(lcmV>=L&&lcmV<=H)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

int main()
{
    int round=1;
    scanf("%I64d",&T);
    while(T--)
    {
        scanf("%I64d%I64d%I64d",&N,&L,&H);
        for(long long i=0; i<N; i++)
        {
            scanf("%I64d",&fArr[i]);
        }
        bool found=false;
        for(long long i=L;i<=H;i++)
        {
            int cnt=0;
            for(int j=0;j<N;j++)
            {
                if((fArr[j]%i)==0||(i%fArr[j])==0)
                {
                    cnt++;
                }else
                {
                    break;
                }
            }
            if(cnt==N)
            {
                printf("Case #%d: %I64d\n",round++,i);
                found=true;
                break;
            }
        }
        if(!found)
        {
            printf("Case #%d: NO\n",round++);
        }

    }
    return 0;
}
