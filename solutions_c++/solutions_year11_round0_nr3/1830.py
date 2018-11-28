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
    int cases;
    int count;
    cin >> cases;
    count=1;
    while(cases > 0)
    {
        int num[1000],n,ip,xx,yy;
        cin >> n;
        REP(i,n)
        {
            cin >> ip;
            num[i]=ip;
            if(i==0)
                xx=ip;
            else
                xx=xx^ip;
        }
        if(xx==0)
        {
           int handle=0;
           sort(&num[0],&num[n]);
           xx=num[0];
           for(int i=1;i<n;i++)
           {
               yy=num[i];
               for(int j=i+1;j<n;j++)
               {
                    yy=yy^num[j];
               }
               if(yy==xx)
               {
                   handle=i;
                   break;
               }
               else
                   xx=xx^num[i];
           }
           int sum=0;
           for(;handle<n;handle++)
           {
                sum+=num[handle];
           }
            printf("Case #%d: %d\n",count,sum);

        }
        else
            printf("Case #%d: NO\n",count);
        count++;
        cases--;
    }
    return 0;
}
