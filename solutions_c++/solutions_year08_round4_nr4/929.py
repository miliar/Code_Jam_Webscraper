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

int main()
{
    int T;
    scanf("%d",&T);
    REP(cse,T)
    {
        int k;
        string s;
        cin>>k>>s;
        VI v(k);
        REP(i,k)
            v[i]=i;
        int sz=SIZE(s);
        int best=sz+1;
        do
        {
            string t;
            REP(i,sz/k)
                REP(j,k)
                {
                    t+=s[i*k+v[j]];
                }
            t.insert(0,"#");
            int b=0;
            REP(i,sz)
                if(t[i+1]!=t[i])
                    b++;
            best<?=b;
        }while(next_permutation(ALL(v)));
        printf("Case #%d: %d\n",cse+1,best);
    }
    return 0;
}
