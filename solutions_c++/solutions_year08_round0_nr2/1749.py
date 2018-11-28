
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

int n,dh,dm,ah,am,xA,xB,nA,nB,turnaround;
struct Route
{
    int d;
    int a;
    int from;
    Route(int dh,int dm,int ah,int am,int f):
        d(dh*60+dm),
        a(ah*60+am),
        from(f)
    {
    }
    bool operator<(const Route& r) const
    {
        return d>r.d;
    }
};
int main()
{
    scanf("%d",&n);
    REP(cse,n)
    {
        priority_queue<Route> r;
        scanf("%d",&turnaround);
        scanf("%d%d",&nA,&nB);
        REP(i,nA)
        {
            scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
            r.push(Route(dh,dm,ah,am,0));
        }
        REP(i,nB)
        {
            scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
            r.push(Route(dh,dm,ah,am,1));
        }

        xA=xB=0;
        priority_queue<int,vector<int>,greater<int> > readyA,readyB;
        while(!r.empty())
        {
            const Route& f=r.top();
            //printf("Processing [%d]: %d:%d->%d:%d xA=%d,xB=%d,readyA=%d,readyB=%d\n",f.from,f.d/60,f.d%60,f.a/60,f.a%60,xA,xB,SIZE(readyA),SIZE(readyB));
            if(f.from == 0)
            {
                if(SIZE(readyA)==0 || readyA.top()>f.d)
                {
                    xA++;
                }
                else
                    readyA.pop();
                readyB.push(f.a+turnaround);
            }
            else
            {
                if(SIZE(readyB)==0 || readyB.top()>f.d)
                    xB++;
                else
                    readyB.pop();
                readyA.push(f.a+turnaround);
            }
            r.pop();
        }
        printf("Case #%d: %d %d\n",cse+1,xA,xB);
    }
    return 0;
}
