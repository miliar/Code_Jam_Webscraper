#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

struct ww
{
  double b,e,s;
  bool operator>(ww w)const{return s>w.s;}
  bool operator<(ww w)const{return s<w.s;}
};


int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    int t;
    cin>>t;
    for(int test_case=0;test_case<t;test_case++)
    {
        double x,s,r,t;
        cin>>x>>s>>r>>t;
        int n;
        ww w[1000];
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>w[i].b>>w[i].e>>w[i].s;
        double l=0;
        double res=0;
        int j=0;
        double p=0;
        for(int i=0;i<n;i++)
        {
            l+=w[i].b-p;
            p=w[i].e;
        }
        l+=x-p;
        double t1=l/r;
        if(t1>t)
        {
            double l1=t*(r);
            res+=t;
            l-=l1;
            res+=l/s;
            t=0;
        }
        else
        {

            res+=t1;
            t-=t1;
        }
        sort(w,w+n);
        while(j<n)
        {
            double t1=(w[j].e-w[j].b)/(r+w[j].s);
            if(t1>t)
            {
                double l=t*(r+w[j].s);
                res+=t;
                t=0;
                l=w[j].e-w[j].b-l;
                res+=l/(w[j].s+s);
            }
            else
            {
                res+=t1;
                t-=t1;
            }
            j++;
        }
        /*
        for(int i=0;i<=j;i++)
        {
            res+=(w[i].e-w[i].b)/(w[i].s+s);
        }
        */
        printf("Case #%d: %.10f\n",test_case+1,res);
    }


    return 0;
}
