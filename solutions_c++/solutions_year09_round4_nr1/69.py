//Tomasz Kulczyński
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define COND 1
#define DB(x) { if(COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }

int main()
{
    int dd;
    scanf("%d",&dd);    
    FOR(cas,1,dd)
    {
        int ret = 0;
        int n;
        scanf("%d",&n);
        vector<int> t;
        REP(i,n) 
        {
            char s[101];
            scanf("%s",s);
            int k;
            for(k=n-1;k && s[k]=='0';k--);
            t.push_back(k);
        }
        REP(i,n)
        {
        //    FORE(j,t) printf("%d ",*j); printf("\n");
            int j = 0;
            while(t[j]>i) j++;
            ret += j;
            for(;j+1<(int)t.size();j++) t[j] = t[j+1];
            t.pop_back();
        }
        printf("Case #%d: %d\n",cas,ret);
    }
    return 0;
}
