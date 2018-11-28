#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 110
int n,m;
int dt;

struct Time
{
    int hh,mm;
    bool operator <(Time b) const
    {
        if (hh!=b.hh) return hh<b.hh;
        else return mm<b.mm;
    }
    bool operator <=(Time b) const
    {
        if (hh!=b.hh) return hh<=b.hh;
        else return mm<=b.mm;
    }
    Time operator +(int t) const
    {
        Time ans=*this;
        ans.mm+=t;
        ans.hh+=ans.mm/60;
        ans.mm%=60;
        return ans;
    }
    void Load()
    {
        scanf("%d:%d",&hh,&mm);
    }
};

struct Schedule
{
    Time start;
    Time end;
};

bool comp_start(Schedule a,Schedule b)
{
    return a.start<b.start;
}

bool comp_end(Schedule a,Schedule b)
{
    return a.end<b.end;
}

Schedule L[MAXN],R[MAXN];
int cnt;
int ansL,ansR;

int t;
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>t;
    for (int i=1;i<=t && cout<<"Case #"<<i<<": ";i++)
    {
        int i,j,k;
        cin>>dt;
        cin>>n>>m;
        for (i=0;i<n;i++)
        {
            L[i].start.Load();
            L[i].end.Load();
        }
        for (i=0;i<m;i++)
        {
            R[i].start.Load();
            R[i].end.Load();
        }

        sort(L,L+n,comp_start);
        sort(R,R+m,comp_end);
        cnt=0;
        ansL=0;
        for (i=0,j=0;i<n;i++)
        {
            for (;j<m && R[j].end+dt<=L[i].start;j++) cnt++;
            if (!cnt) ansL++;
            else cnt--;
        }
        
        sort(L,L+n,comp_end);
        sort(R,R+m,comp_start);
        cnt=0;
        ansR=0;
        for (i=0,j=0;j<m;j++)
        {
            for (;i<n && L[i].end+dt<=R[j].start;i++) cnt++;
            if (!cnt) ansR++;
            else cnt--;
        }
        
        cout<<ansL<<' '<<ansR<<endl;
    }
    return 0;
}
