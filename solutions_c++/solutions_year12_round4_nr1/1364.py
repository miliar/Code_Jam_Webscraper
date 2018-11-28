#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;
pair<lli,lli> d[10011]; lli D,N;
map<pair<lli,lli>,int> memo;

int possible(lli i,lli li)
{
    if(d[i].first+li>=D) return 1;
    pair<lli,lli> key=make_pair(i,li);
    if(memo.count(key)) return memo[key];
    int rv=0;
    for(int j=i+1;j<N && !rv;j++)
    {
        if(d[i].first+li<d[j].first) break;
        if(possible(j,min(d[j].second,d[j].first-d[i].first))) rv=1;
    }
    return memo[key]=rv;

}

int main()
{
    int t; cin>>t; int cn=0;
    while(t--)
    {
        cin>>N;
        for(int i=0;i<N;i++) cin>>d[i].first>>d[i].second;
        cin>>D;
        memo.clear();
        int rv=possible(0,d[0].first);
        printf("Case #%d: ",++cn); if(rv) printf("YES\n"); else printf("NO\n");
    }

}
