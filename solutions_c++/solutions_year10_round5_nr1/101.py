#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>

#define INF 2000000000

using namespace std;

long long t,iii;
long long a,b,n,k,i,j,d,tmp1,tmp2;
long long lim;
long long v[100];
long long prime[500005],enp,p;
long long can[500005];
long long chk;
long long ans;

void precomp()
{
    enp=0;
    for(i=2;i<=1000000;i++)
    {
        for(j=0;j<enp&&prime[j]*prime[j]<=i;j++)
        {
            if(i%prime[j]==0)
            break;
        }
        if(j>=enp||prime[j]*prime[j]>i)
        {
            prime[enp]=i;
            enp++;
        }
    }
    return ;
}

void Euclid(long long a,long long b,long long &x,long long &y)
{
    if(a==0)
    {
        x=0;
        y=1;
        return ;
    }
    else
    {
        long long xx,yy,q;
        q=(b/a);
        Euclid(b%a,a,xx,yy);
        x=yy-q*xx;
        y=xx;
        return ;
    }
}

long long mod(long long tmpx,long long tmpy)
{
    return (tmpx%tmpy+tmpy)%tmpy;
}

int main()
{
    precomp();
    scanf("%I64d",&t);
    for(iii=1;iii<=t;iii++)
    {
        scanf("%I64d %I64d",&d,&k);
        lim=1;
        for(i=0;i<d;i++)
        {
            lim*=10;
        }
        for(i=0;i<k;i++)
        {
            scanf("%I64d",&v[i]);
        }
        printf("Case #%I64d: ",iii);
        if(k<=2)
        {
            if(k==1||v[0]!=v[1])
            printf("I don't know.\n");
            else
            printf("%I64d\n",v[0]);
        }
        else
        {
            chk=0;
            ans=-1;
            for(j=0;j<enp&&prime[j]<=lim;j++)
            {
                can[j]=0;
                p=prime[j];
                a=-1;
                for(i=0;i<k-2;i++)
                {
                    if(mod(v[i+2]-v[i+1],p)==0)
                    {
                        if(mod(v[i+1]-v[i],p)!=0)
                        {
                            a=0;
                            b=mod(v[i+1]-a*v[i],p);
                            break;
                        }
                        else
                        {
                            a=1;
                            b=0;
                            break;
                        }
                    }
                    else
                    {
                        Euclid(mod(v[i+1]-v[i],p),p,tmp1,tmp2);
                        tmp1=mod(tmp1,p);
                        tmp2=mod(tmp1*(v[i+2]-v[i+1]),p);
                        //printf("YYY %I64d %I64d %I64d %I64d %I64d\n",tmp1,tmp2,i,v[i+1]-v[i],v[i+1],v[i]);
                        if(a==-1)
                        {
                            a=tmp2;
                            b=mod(v[i+1]-v[i]*a,p);
                            break;
                        }
                    }
                }
                if(a!=-1)
                {
                    //if(a==2)
                    //printf("%I64d %I64d %I64d %I64d %I64d\n",j,p,a,b,ans);
                    can[j]=1;
                    for(i=0;i<k;i++)
                    {
                        if(v[i]>=p)
                        can[j]=0;
                    }
                    for(i=0;i<k-1;i++)
                    {
                        if(mod(v[i+1]-a*v[i]-b,p)!=0)
                        can[j]=0;
                    }
                }
                if(can[j]==1)
                {
                    //printf("%I64d %I64d %I64d %I64d %I64d\n",j,p,a,b,ans);
                    if(ans==-1||ans==mod(a*v[k-1]+b,p))
                    ans=mod(a*v[k-1]+b,p);
                    else
                    ans=-2;
                    //printf("XXX %I64d XXX\n",ans);
                }
            }
            if(ans<0)
            {
                printf("I don't know.\n");
            }
            else
            {
                printf("%I64d\n",ans);
            }
        }
    }
    return 0;
}
