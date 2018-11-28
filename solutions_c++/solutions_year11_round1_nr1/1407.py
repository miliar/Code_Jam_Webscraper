#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<=(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;	

int main()
{
    int cases,count;
    cin >> cases;
    count=1;
    while(cases>0)
    {
        int n,pd,pg,ok,i;
        float j;
        ok=0;
        cin >> n >> pd >> pg;
            for(i=1;i<=n;i++)
            {
                j=((float)pd/100)*(float)i;
                if((j-(int)j) == 0.0)
                {
                    ok=1;
                    break;
                }
            }
        if(pg==0 && pd>0)
            ok=0;
        if(pg==100 && pd<100)
            ok=0;
        /*if(ok)
        {
            for(;i<1000;i++)
            {
                j=((float)pg/100)*(float)i;
                if((j-(int)j) == 0.0)
                {
                    cout << "--"<<i<<"--";
                    break;
                }
            }
        }*/
        if(ok)
        {

            printf("Case #%d: Possible\n",count);

        }
        else
        {
            printf("Case #%d: Broken\n",count);
        }
        cases--;
        count++;
    }
    return 0;
}
