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
#include <numeric>

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

LL n,m,X,Y,Z;
vector<long long> mArr(500000),nArr(500000);
vector<long long> ans(500000);
int main()
{
    int T;
    scanf("%d",&T);
    REP(cse,T)
    {
        cin>>n>>m>>X>>Y>>Z;
        REP(i,m)
            cin>>mArr[i];
        REP(i,n)
        {
            nArr[i]=mArr[i%m];
            mArr[i%m]=(X*mArr[i%m]+Y*(i+1))%Z;;
        }
        REP(i,n)
        {
            ans[i]=1;
            REP(j,i)
                if(nArr[i]>nArr[j])
                    ans[i]=(ans[i]+ans[j])%1000000007LL;
        }
        LL a=0;
        REP(i,n)
            a=(a%1000000007LL+ans[i]%1000000007LL)%1000000007LL;
        printf("Case #%d: %lld\n",cse+1,a);
    }
    return 0;
}
