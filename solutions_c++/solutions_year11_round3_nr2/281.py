#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
long long cases,inp,cs,n,i,k,l,t,c,dist[10000000],temp;
vector < pair <double, long long> > a;
int main()
{
    //freopen("inp.txt","r",stdin);
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt1.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    cin>>cases;

    for(cs=1;cs<=cases;cs++)
    {
        cin>>l>>t>>n>>c;
        a.clear();
        for(i=0;i<c;i++)
        {
            cin>>temp;
            for(k=i;k<n;k+=c)
                dist[k]=temp;
        }
        long long hrs=0;
        for(i=0;i<n;i++)
        {
            hrs+=(dist[i]*2);
            if(hrs>t)
            break;
        }
        //cout<<t<<" "<<i<<endl;
        //cout<<hrs<<endl;
        hrs-=(dist[i]*2);
        temp=t-hrs;
        float td=((float)temp*0.5);
        float with=temp+(dist[i]-td);
        int wo=dist[i]*2;
        //cout<<hrs<<" "<<with<<" "<<wo<<" "<<i<<endl;
        a.push_back(make_pair(wo-with,i));
        int sp=i;
        i++;
        for(;i<n;i++)
        {
            a.push_back(make_pair(dist[i]*2-dist[i],i));
        }
        sort(a.begin(),a.end());
        reverse(a.begin(),a.end());
        for(i=0;i<l && i<a.size();i++)
        {
            if(a[i].second==sp)
                hrs+=with;
            else
            hrs+=dist[a[i].second];
        }
        for(;i<a.size();i++)
            hrs+=(dist[a[i].second]*2);
        long long hrs1=0;
        if(l==0)
            for(i=0;i<n;i++)
                hrs1+=(dist[i]*2);
        if(l==0 && hrs1!=hrs)
            cout<<"SHOUT\n";
        cout<<"Case #"<<cs<<": "<<hrs<<endl;

    }
    return 0;
}
