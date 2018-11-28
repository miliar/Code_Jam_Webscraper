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
    int dd, cas=0;
    scanf("%d",&dd);    
    while(dd--)
    {
        char s[65];
        scanf("%s",s);
        set<char> x;
        for(int i=0;s[i];i++) x.insert(s[i]);
        ll b = max(2, (int)x.size()), w = 0, k = 0;
        map<char,int> ma;
        for(int i=0;s[i];i++) 
        {
            if(!ma.count(s[i])) 
            {
                if(i==0) ma[s[i]] = 1;
                else if(k == 0)
                {
                    k = 2;
                    ma[s[i]] = 0;
                }
                else ma[s[i]] = k++;
            }
            w = w * b + ma[s[i]];
        }
        printf("Case #%d: %lld\n",++cas,w);
    }
    return 0;
}
