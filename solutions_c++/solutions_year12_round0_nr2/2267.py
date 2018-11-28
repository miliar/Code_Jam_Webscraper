#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <bitset>
#include <assert.h>

using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))

#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second

typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;
int surprize(int a)
{
    if(!a)
        return a;
    if(a%3==0)
    {
        return a/3+1;
    }
    else if(a%3==1)
    {
        return (a/3+1);
    }
    
    else return a/3+2;
}
int noSurprize(int a)
{
    if(a%3==0)
    {
        return a/3;
    }
    else if(a%3==1)
    {
        return (a/3+1);
    }
    
    else return a/3+1;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("o.o","w",stdout);
    
        //int t=SS;
        int t,a;
        cin>>t;
        //cin.ignore();
        REP(cases,t)
        {
            int n,s,p,ans=0;
            cin>>n>>s>>p;
            REP(i,n)
            {
                cin>>a;
                if(s)
                {
                    if(noSurprize(a)>=p)
                        ans++;
                    else if(surprize(a)>=p)
                    {
                        ans++;s--;
                    }
                }
                else
                {
                    if(noSurprize(a)>=p)
                        ans++;
                }
            }
            
            printf("Case #%d: %d\n",cases+1,ans);
        }
    return 0;
}
