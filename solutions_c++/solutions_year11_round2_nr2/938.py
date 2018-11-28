#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int c,d;
int tp,tv;
struct point
{
    int pos;
    int cnt;
};
point tmp;
vector<point> seg;
int main()
{
    freopen("bs.in","r",stdin);
    freopen("bs.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        seg.clear();
        cin>>c>>d;
        for(int i=1;i<=c;i++)
        {
            cin>>tmp.pos>>tmp.cnt;
            seg.push_back(tmp);
        }
        double l=0,r=1e10;
        double res=0.0;
        while(fabs(l-r)>1e-6)
        {
            double ans=(l+r)/2;
            //cout<<l<<r<<ans<<endl;
            double tl=-10000000000.0;
            bool flag=true;
            for(int i=0;i<c;i++)
            {
                double ttl=seg[i].pos-ans;
                double tr=seg[i].pos+ans;
                int tcnt=seg[i].cnt;
                tl=max(tl,ttl);
                if(tr<tl || tr-tl<d*(tcnt-1))
                {
                    flag=false;break;
                }
                tl=tl+d*(tcnt);
            }
            if(flag) r=ans,res=(double)ans;
            else l=ans;
        }
        cout<<"Case #"<<t<<": ";
        cout<<res<<endl;
    }
    return 0;
}
