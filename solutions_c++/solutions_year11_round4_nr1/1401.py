#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
using namespace std;

pair<int,int> ma[1001];
int w[1001];

#define tres pair<double,pair<int,int> > 
#define dist first
#define ini second.first
#define fin second.second

int main()
{
    int T;
    scanf("%d",&T);
    for(int I=0;I<T;I++)
    {
        double s,r,x,t;
        int n;
        scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d%d",&ma[i].first,&ma[i].second,&w[i]);
        }
        
        sort(ma,ma+n);
        
        int pos=0;
        int p=0;
        vector<tres> z;
        
        while(p<n && pos<x)
        {
            if(pos!=ma[p].first)
            {
                z.push_back(make_pair(0.0,make_pair(pos,ma[p].first)));
                pos=ma[p].first;
            }else
            {
                pos=ma[p].second;
                z.push_back(make_pair((double)(w[p]),make_pair(ma[p].first,ma[p].second)));
                p++;
            }
        }
        
        if(p==n && pos<x)
        {
            z.push_back(make_pair(0.0,make_pair(pos,(int)(x))));
        }
        
        sort(z.begin(),z.end());
        
        double res=0;
        double temp;
        p=0;
        
        //printf("%d\n",z.size());
        
        while(p<z.size() && t>0)
        {
       //     printf("run %d %d %lf\n",z[p].ini,z[p].fin,(r+z[p].dist));
            temp=z[p].fin-z[p].ini;
            if(temp/(r+z[p].dist)<=t)
            {
                res+=temp/(r+z[p].dist);
                t-=temp/(r+z[p].dist);
            }else
            {
                res+=t-(t*(r+z[p].dist)-temp)/(s+z[p].dist);
                t=0;
            }
        //    printf("%lf\n",res);
            p++;
        }
        
        
        while(p<z.size())
        {
            temp=z[p].fin-z[p].ini;
            res+=temp/(s+z[p].dist);
            p++;
        }
        
        printf("Case #%d: %lf\n",I+1,res);
        
    }
    return 0;
}
