/*
Try Try & Try until you solve the problem...
Nothing is impossible for the problem solvers... :)
*/
/*

*/
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <numeric>

#include <cmath>
#include <cstdio>

#define IP(n) for(i=0;i<n;i++)
#define JP(n) for(j=0;j<n;j++)
#define KP(n) for(k=0;k<n;k++)

#define vi vector<int>
#define vi2 vector<vector<int>>
#define vs vector<string>

#define pb push_back
#define TC int t,check=1;cin>>t;while(check<=t)
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)


using namespace std;

vector<vector<pair<int,int> > > v(2000005);

void gen()
{
    int n,m;
    for(int i=10;i<100;i++)
    {
        n=i;
        m=(i%10)*10+i/10;

        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }
    }

    for(int i=100;i<1000;i++)
    {
        n=i;
        m=(i%100)*10+i/100;

        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%10)*100+i/10;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }
    }

    for(int i=1000;i<10000;i++)
    {
        n=i;
        m=(i%1000)*10+i/1000;

        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%100)*100+i/100;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%10)*1000+i/10;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }
    }

    for(int i=10000;i<100000;i++)
    {
        n=i;
        m=(i%10000)*10+i/10000;

        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%1000)*100+i/1000;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%100)*1000+i/100;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%10)*10000+i/10;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }
    }

    for(int i=100000;i<1000000;i++)
    {
        n=i;
        m=(i%100000)*10+i/100000;

        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%10000)*100+i/10000;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%1000)*1000+i/1000;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%100)*10000+i/100;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%10)*100000+i/10;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }
    }

    for(int i=1000000;i<2000001;i++)
    {
        n=i;
        m=(i%1000000)*10+i/1000000;

        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%100000)*100+i/100000;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%10000)*1000+i/10000;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%1000)*10000+i/1000;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%100)*100000+i/100;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }

        m=(i%10)*1000000+i/10;
        if(n<m)
        {
            v[i].pb(make_pair(n,m));
        }
    }

}

set<pair<int,int> > s;

int calc(int a,int b)
{
    s.clear();

    for(int i=a;i<=b;i++)
    {
        for(int j=0;j<v[i].size();j++)
        {
            if(v[i][j].second<=b)
            s.insert(v[i][j]);
        }

    }

    return s.size();
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C_hard.txt","w",stdout);
    gen();
    int t,check=1;
    cin>>t;
    while(t--)
    {
        int a,b;
        cin>>a>>b;

        printf("Case #%d: %d\n",check++,calc(a,b));
    }
    return 0;
}
