#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
using namespace std;
double a[1000010];
map<int, int>mp;
int main()
{
    freopen("1.in","r",stdin);
    freopen("2.out","w",stdout);
    int c,cs,X,S,R,t,N,i,j;
    int b,w,e;
    cin>>cs;
    for (c=1;c<=cs;c++)
    {
        cin>>X>>S>>R>>t>>N;
        mp.clear();
        mp[0]=X;
        for (i=0;i<N;i++)
        {
            cin>>b>>e>>w;
            mp[w]+=e-b;
            mp[0]-=e-b;
        }
        double cnt=0;
        double time=0;
        for (i=0;i<=100;i++)
            if (mp.find(i)!=mp.end())
            {
                if (cnt+(double)mp[i]/(R+i) < t)
                {
                    cnt+=(double)mp[i]/(R+i);
                    time+=(double)mp[i]/(R+i);
                }
                else if (cnt<t)
                {
                    time+=t - cnt + ((double)mp[i] - (R + i) * (t - cnt)) / (S + i);
                    cnt=t+10;
                }
                else
                {
                    time+=(double)mp[i] / (S + i);
                }
            }
        printf("Case #%d: %.10lf\n",c,time);
    }
    return 0;
}
