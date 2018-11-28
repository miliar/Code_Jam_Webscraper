#include <algorithm> 
#include <vector> 
#include <string> 
#include <cstdio> 
#include <cstring> 
#include <iostream> 
#include <sstream> 
#include <iterator> 
#include <cmath> 
#include <list> 
#include <queue> 
#include <map> 
#include <cctype> 
#include <set>

#define INF 10000000 
#define DINF 1e99 
#define all(x) (x).begin(),(x).end() 

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define ALL(x) (x).begin(),(x).end()  
#define FOREACH(i,a) for(typeof((a).begin()) i=(a).begin();i!=(a).end();i++)
#define CLR(v,a) memset(v,a,sizeof(v))
#define SIZE(a) ((int)(a).size())

typedef vector<string> VS;
typedef vector<int>    VI;
typedef long long      LL;

int P,K,L;
int main()
{
    int T;
    scanf("%d",&T);
    REP(cse,T)
    {
        cin>>P>>K>>L;
        vector<long long> f(L);
        REP(i,L)
            cin>>f[i];
        sort(f.rbegin(),f.rend());
        LL ans=0;
        LL presses=1;
        LL u=0;
        REP(i,L)
        {
            ans+=1LL*f[i]*presses;
            u++;
            if(u==K)
            {
                u=0;
                presses++;
            }
        }
        printf("Case #%d: %lld \n",cse+1,ans);
    }
    return 0;
}
