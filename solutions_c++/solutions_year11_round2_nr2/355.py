#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
using namespace std;
struct bb{double a;int b;};
bool cmp(bb x, bb y)
{
    return x.a<y.a;
}
bb v[210];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("2.out","w",stdout);
    int c,T,i,j,cs;
    double pos,d;
    double beg,end,mid;
    cin>>T;
    for (cs=1;cs<=T;cs++)
    {
        cin>>c>>d;
        for (i=0;i<c;i++)
        {
            cin>>v[i].a>>v[i].b;
        }
        sort(v,v+c,cmp);
        beg=0;end=100000000000000;
        v[0].b--;
        while (fabs(beg-end)>(1e-4))
        {
            //cout<<beg<<" "<<end<<endl;
            mid=(beg+end)/2.0;

            pos=v[0].a-mid;
            //if (fabs(mid-1)<1e-6)
                //cout<<pos<<endl;
            //if (fabs(beg-0.5)<1e-6 && fabs(end-0.5)<1e-6)
                //cout<<v[0].b<<endl;
            bool flag=true;
            //cout<<v[0].b<<" "<<v[1].b<<" "<<v[2].b<<" "<<c<<endl;
            for (i=0;i<c;i++)
                for (j=0;j<v[i].b;j++)
                {
                    //if (fabs(mid-1)<1e-6)
                        //cout<<i<<" "<<j<<endl;
                    if (fabs(v[i].a-(pos+d))<=mid)
                    {
                        pos+=d;
                    }
                    else if (v[i].a>pos+d)
                    {
                        pos=v[i].a-mid;
                    }
                    else flag=false;
                }
            if (flag)
                end=mid;
            else
                beg=mid;
        }
        printf("Case #%d: %lf\n", cs,beg);
    }
    return 0;
}
