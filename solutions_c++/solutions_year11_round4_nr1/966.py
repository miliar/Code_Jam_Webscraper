#include<cstdio>
#include<cmath>
#include<algorithm>
#include<functional>
using namespace std;

struct st{
    int b,e,w;
    bool operator < (const st o) const
    {
        if(b<o.b)
            return true;
        return false;
    }
};

struct st2{
    int b,e,w;
    bool operator < (const st2 o) const
    {
        if(w<o.w)
            return true;
        return false;
    }
};

int main(){

    int t;
    st ww[1005];
    st2 ar[2005];
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int x,s,r,t,n;
        scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
        for(int j=0;j<n;j++)
        {
            scanf("%d %d %d",&ww[j].b,&ww[j].e,&ww[j].w);
            ww[j].w+=s;
            ar[j].b=ww[j].b;
            ar[j].e=ww[j].e;
            ar[j].w=ww[j].w;
        }
        sort(ww,ww+n,less<st>());
        /*
        for(int j=0;j<n;j++)
        {
            printf(".%d %d %d\n",ww[j].b,ww[j].e,ww[j].w);
        }
        */
        int last=0;
        int p=n;
        for(int j=0;j<n;j++)
        {
            if(last<ww[j].b)
            {
                ar[p].b=last;
                ar[p].e=ww[j].b;
                ar[p].w=s;
                last=ww[j].e;
                p++;
            }else
            {
                last=ww[j].e;
            }
        }
        if(last<x)
        {
            ar[p].b=last;
            ar[p].e=x;
            ar[p].w=s;
            p++;
        }
        sort(ar,ar+p,less<st2>());
/*
        for(int j=0;j<p;j++)
        {
            printf(".%d %d %d\n",ar[j].b,ar[j].e,ar[j].w);
        }
*/
        double tt=t;
        int pp=0;
        double sol=0;
        while(tt>1E-7&&pp<p)
        {
            if(tt>(1.0*(ar[pp].e-ar[pp].b)/(ar[pp].w+r-s)))
            {
                ar[pp].w+=r-s;
                tt-=(1.0*(ar[pp].e-ar[pp].b)/(ar[pp].w));
                sol+=(1.0*(ar[pp].e-ar[pp].b)/(ar[pp].w));
                //printf("1 %lf\n",tt);
            }else
            {
                sol+=tt;
                double temp=1.0*ar[pp].e-ar[pp].b-(tt*(ar[pp].w+r-s));
                tt=0;
                sol+=(1.0*temp/ar[pp].w);
                //printf("2 %lf\n",tt);
            }
            //printf("pp=%d sol=%lf tt=%lf\n",pp,sol,tt);
            pp++;
            //int swa;
            //scanf("%d",&swa);
        }
        while(pp<p)
        {
            sol+=(1.0*(ar[pp].e-ar[pp].b)/(ar[pp].w));
            //printf("pp=%d sol=%lf\n",pp,sol);
            pp++;
        }
        printf("Case #%d: %.9lf\n",i+1,sol);
    }

    return 0;
}
