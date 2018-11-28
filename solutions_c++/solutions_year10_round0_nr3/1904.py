#include <stdio.h>
#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

long long found(deque<long long> s,deque< deque<long long> > data)
{
    long long i,j;
    bool fl;
    for (i=0; i<data.size(); i++)
    {
        fl=1;
        for (j=0; j<data[i].size(); j++) if (data[i][j]!=s[j]) fl=0;
        if (fl) return i;
    }
    return -1;
}

int main()
{
    long long r,k,n,i,a,sum,rest,fnd,j,t,cas,c,ans;
    freopen("inc","r",stdin);
    freopen("outc","w",stdout);
    cin>>t;
    for (cas=1; cas<=t; cas++)
    {
        deque<long long> s;
        deque< deque<long long> > data;
        deque<long long> sums;
        cin>>r>>k>>n;
        for (i=0; i<n; i++)
        {
            cin>>a;
            s.push_back(a);
        }
        ans=0;
        data.push_back(s);
        sum=0;
        for (i=0; sum+s[i]<=k && i<s.size(); i++) sum+=s[i];
        sums.push_back(sum);
        ans=sums[0];
        for (i=1; i<r; i++)
        {
            sum=0;
            int cnt=0;
            for (cnt=0; sum+s[0]<=k && cnt<s.size(); cnt++)
            {
                sum+=s[0];
                c=s.front();
                s.pop_front();
                s.push_back(c);
            }
            //printf("%d\n",sum);

            if (found(s,data)!=-1) break;
            else
            {
                data.push_back(s);
                sum=0;
                for (j=0; sum+s[j]<=k && j<s.size(); j++) sum+=s[j];
                sums.push_back(sum);
                ans+=sum;
            }
        }
        if (i<r)
        {
            rest=r-data.size();
            fnd=found(s,data);
            int m=rest/(data.size()-fnd),l=data.size()-fnd;
            for (i=fnd; i<sums.size(); i++) ans+=sums[i]*m;
            for (i=fnd,j=0; j<rest%l; j++,i++) ans+=sums[i];
        }
        cout<<"Case #"<<cas<<": "<<ans<<"\n";
    }

	return 0;
}
