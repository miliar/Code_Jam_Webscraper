#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

struct s{
    int b,e,s;
}w[1005];

bool mycomp(s x,s y)
{
    return (x.s<y.s);
}

int main()
{
    int i,j,k,l,s,r,T,cas,n;
    double t,ans,len,rtm,ntm;

    freopen("a.txt","r",stdin);
    freopen("aout.txt","w",stdout);

    //printf("what");

    scanf("%d", &T);
    //cout<<"QHAAAAAAAAAAAAAT"<<endl;


    for(cas=1;cas<=T;cas++)
    {
        cin>>l>>s>>r>>t>>n;
        ans=0.0;
        k=0;

        for(i=0;i<n;i++)
        {
            cin>>w[i].b>>w[i].e>>w[i].s;
            k+=w[i].e-w[i].b;
            //cout<<"QHAAAAAAAAAAAAAT"<<endl;
        }

        //cout<<"QHAAAAAAAAAAAAAT"<<endl;

        k=l-k;

        sort(w,w+n,mycomp);

        len=k;
        rtm=r;

        if(len/rtm<=t)
        {
            ans+=(len/rtm);
            t-=(len/rtm);
        }

        else if(t==0.0)
        {
            ans+=(len/(double)s);
        }

        else
        {
            ntm=t;
            ans+=t;
            t=0.0;

            ans+=(len-ntm*r)/(double)s;
        }

        //cout<<"QHAAAAAAAAAAAAAT"<<endl;

        for(i=0;i<n;i++)
        {
            len=w[i].e-w[i].b;
            rtm=w[i].s+r;

            if(len/rtm<=t)
            {
                t-=(len/rtm);
                ans+=len/rtm;
            }

            else if(t==0.0)
            {
                ans+=len/(double)(w[i].s+s);
            }

            else
            {
                ntm=t;
                ans+=t;
                t=0.0;

                ans+=(len-((ntm)*rtm))/(double)(w[i].s+s);
            }
        }
        printf("Case #%d: %.8lf\n",cas,ans);
    }

    return 0;
}







