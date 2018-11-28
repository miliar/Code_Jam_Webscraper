#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <stdio.h>
#include <assert.h>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)
#define GN(a) scanf("%d",&a)

typedef long long int LL;
typedef vector<int> VI;

using namespace std;
int a[10002];
int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);

    int t;
    cin>>t;
    FOR(test,1,t+1)
    {
        vector<LL> dist,dist0;
        double t;
        int N,L,C;
        cin>>L>>t>>N>>C;
        FOR(i,0,C)cin>>a[i];
        FOR(i,0,N)dist.push_back(a[i%C]);
        LL sum = 0;
        FOR(i,0,N)
        {
            sum+=dist[i];
            dist0.push_back(sum);
        }
        LL lim = t / 2;
        int ind = (int)(upper_bound(dist0.begin(),dist0.end(),lim)-dist0.begin());
       // cout<<lim<<" "<<ind<<endl;
        vector<LL> D;
        FOR(i,ind+1,dist.size())D.push_back(dist[i]);
        if(ind<dist.size()){D.push_back(dist0[ind]-lim);}
        sort(D.begin(),D.end());
        reverse(D.begin(),D.end());
        sum = 0;
        FOR(i,0,min(L,(int)D.size()))sum+=D[i];
        LL ans = sum + (LL)(dist0[dist0.size()-1]-sum)*2;
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}

