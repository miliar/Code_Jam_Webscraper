
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

VS engines(1100),queries(1100);
int n,nEng,nQuery;
int dp[1100];
string s;
int doit(int v)
{
    int &ret=dp[v];
    if(ret!=-1)
        return ret;
    ret=1000000000;
    REP(i,nEng)
    {
        vector<string>::iterator it=find(queries.begin()+v,queries.end(),engines[i]);
        if(it!=queries.end())
        {
            int p=it-queries.begin();
            if(p==v)
                ret<?=1+doit(p+1);
            else
                ret<?=1+doit(p);
        }
        else
            return ret=0;
    }
    return ret;
}
int main()
{
    scanf("%d",&n);
    REP(cse,n)
    {
        scanf("%d\n",&nEng);
        REP(i,nEng)
        {
            getline(cin,s);
            engines[i]=s;
        }
        scanf("%d\n",&nQuery);
        REP(i,nQuery)
        {
            getline(cin,s);
            queries[i]=s;
        }
        CLR(dp,255);
        printf("Case #%d: %d\n",cse+1,doit(0));
    }
    return 0;
}
