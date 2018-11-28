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


int main()
{
    //freopen("inp.txt","r",stdin);
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt1.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long cases,i,a,b,c,x,s,r,n,cs;
    cin>>cases;
    vector < pair < pair < int, int> , int > > arr;
    vector < pair < int, int > > arr1;
    double ans, sum, speed, dist, tmptime,t,dr;
    for(cs=1;cs<=cases;cs++)
    {
        cin>>x>>s>>r>>t>>n;
        sum=0; ans=0;
        arr.clear(), arr1.clear();
        for(i=0;i<n;i++)
        {
            cin>>a>>b>>c;
            sum+=(b-a);
            //arr.push_back(make_pair(make_pair(a,b),c));
            arr1.push_back(make_pair(c, b-a));

        }
        //cout<<sum<<endl;
        arr1.push_back(make_pair(0,x-sum));
        //sort(arr.begin(),arr.end());
        sort(arr1.begin(),arr1.end());
        for(i=0;i<=n;i++)
        {
            //cout<<arr1[i].first<<endl;
            //cout<<arr1[i].second<<endl;
            //cout<<i<<" "<<arr1[i].first<<" "<<arr1[i].second<<endl;
            //cout<<t<<endl;
            if(t>0)
            {

                speed = r+arr1[i].first;
                dist = arr1[i].second;
                //cout<<speed<<" "<<dist<<endl;
                tmptime = (double)dist/speed;
                //cout<<tmptime<<endl;
                if(tmptime<=t)
                    ans+=tmptime , t-=tmptime;
                else
                {
                    dr = speed*t;
                    ans+=t;
                    ans+=(double)(dist-dr)/(s+arr1[i].first);
                    //cout<<ans<<endl;
                    t=-1;
                }
            }
            else
            {
                speed = s+arr1[i].first;
                dist = arr1[i].second;
                //cout<<dist<<" "<<speed<<endl;
                ans+=(dist)/(speed);
            }
        }
        cout<<"Case #"<<cs<<": ";
        printf("%.8lf\n",ans);
    }
    return 0;
}
