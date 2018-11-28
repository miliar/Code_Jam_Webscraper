#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int b,e;
int main()
{
    int t,T,n,i,j,l,s,r,ex;
    int ti;
    freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d%d%d%d",&l,&s,&r,&ti,&n);
        pair<int,int> w[1001];
        double ans=0.0;     
        ex=l;   
        for(i=0;i<n;i++)
        {
            scanf("%d%d%d",&b,&e,&w[i].first);
            w[i].second=e-b;
            ex-=e-b;
        }           
        w[n].first=0;
        w[n].second=ex; 
        sort(w,w+n+1);
        double time=1.0*ti;
        for(i=0;i<=n;i++)
        {
//            cout<<w[i].first<<" "<<w[i].second<<" "<<time<<"\n";
            double nt,nl=time*(r+w[i].first);
            if(nl<=w[i].second)
            {
                ans+=time+(double)(w[i].second-nl)/(w[i].first+s);
                time=0.0;
            }
            else 
            {
                 nt=(double)w[i].second/(w[i].first+r);
                 ans+=nt;
                 time-=nt;
            }
//            cout<<ans<<endl;
        }
        printf("Case #%d: %f\n",t,ans);
    }
//system("pause");
    return 0;
}
