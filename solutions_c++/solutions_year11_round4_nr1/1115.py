#include<stdio.h>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
vector<pair<int,int> >v;
int main()
{
    int t,s,x,r,n,ti,i,j;
    freopen("GAL.in","r",stdin);
    freopen("GAL.out","w",stdout);
    scanf("%d",&t);
    for(int cn=1;cn<=t;cn++)
    {
        scanf("%d%d%d%d%d",&x,&s,&r,&ti,&n);
        v.clear();
        int sum=0;
        for(i=0;i<n;i++)
        {
            int b,e,w;
            scanf("%d%d%d",&b,&e,&w);
            sum+=e-b;
            v.push_back(make_pair(w,e-b));
        }
        v.push_back(make_pair(0,x-sum));
        sort(v.begin(),v.end());
        double tu=ti,ts=0;
        for(i=0;i<n+1;i++)
        {
            if(tu>(double)v[i].second/(v[i].first+r))
            {
                ts+=(double)v[i].second/(v[i].first+r);
                tu-=(double)v[i].second/(v[i].first+r);
            }
            else
            {
                ts+=tu;
                double sr=tu*(v[i].first+r);
                double sw=v[i].second-sr;
                ts+=sw/(v[i].first+s);
                tu=0;
            }
        }
        printf("Case #%d: %f\n",cn,ts);
    }
    return 0;
}
