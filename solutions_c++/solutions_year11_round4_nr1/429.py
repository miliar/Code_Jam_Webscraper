#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string>
#include <stdio.h>
using namespace std;

int N,X,S,R,t;

int B[1111];
int E[1111];
int W[1111];

vector< pair<double, double> > V;
void test()
{
    cin>>X>>S>>R>>t>>N;
    int i;
    for(i=0;i<N;i++)
    cin>>B[i]>>E[i]>>W[i];
    R-=S;

    int p=0;
    double ans=0,d,v,dt;

    vector< pair<double, double> > V;
    for(i=0;i<N;i++)
    {
        d=B[i]-p;
        v=S;
        V.push_back(make_pair(v,d));
        p=B[i];
        d=E[i]-p;
        v=S+W[i];
        V.push_back(make_pair(v,d));
        p=E[i];
    }
    d=X-p;
    v=S;
    p=0;

    V.push_back(make_pair(v,d));

    sort(V.begin(),V.end());

    N=V.size();

    for(i=0;i<N;i++)
    {
        d=V[i].second;
        v=V[i].first;
        if(ans<t) v+=R;
        dt=d/v;
        if(ans<t&&ans+dt>t)
        {
            d-=v*double(t-ans);
            ans=t;
            v=V[i].first;
            dt=d/v;
        }
        ans+=dt;
        //p=B[i];
    }



    /*for(i=0;i<N;i++)
    {
        d=B[i]-p;
        v=S;
        if(ans<t) v+=R;
        dt=d/v;
        if(ans<t&&ans+dt>t)
        {
            d-=v*double(t-ans);
            ans=t;
            v=S;
            dt=d/v;
        }
        ans+=dt;
        p=B[i];

        //cout<<ans<<" "<<p<<" "<<v<<" "<<endl;
        //--------------------

        d=E[i]-p;
        v=S+W[i];
        if(ans<t) v+=R;
        dt=d/v;
        if(ans<t&&ans+dt>t)
        {
            d-=v*double(t-ans);
            ans=t;
            v=S+W[i];
            dt=d/v;
        }
        ans+=dt;
        p=E[i];
       // cout<<ans<<" "<<p<<endl;

    }
        d=X-p;
        v=S;
        if(ans<t) v+=R;
        dt=d/v;
        if(ans<t&&ans+dt>t)
        {
            d-=v*double(t-ans);
            ans=t;
            v=S;
            dt=d/v;
        }
        ans+=dt;
        p=X;*/
       // cout<<ans<<" "<<p<<endl;
    printf("%.10lf",ans);
    return;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<": ";
      test();
      cout<<endl;
    }
    return 0;
}
