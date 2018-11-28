#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cassert>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define sz size()
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
#define INF int(1e9)

typedef long long LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

int g(int a,int b)
{
    if(b==0)
    return a;
    else return g(b,a%b);
}

int main()
{
    LL n,pd,pg;
    int t,kase=0;
    cin >> t;
    while(t--)
    {
              kase++;
              cin >> n >> pd >> pg;
              if(pd == 0 && pg == 0) {cout << "Case #" << kase << ": Possible\n" ;continue;}
              if(pd != 0 && pg == 0) {cout << "Case #" << kase << ": Broken\n" ;continue;}
              if(100/g(pd,100) <= n )
              {
                           if(pd == 100)
                           {
                                 cout << "Case #" << kase << ": Possible\n" ;
                           }
                           else if( pd >0 && pg < 100)
                           {
                                cout << "Case #" << kase << ": Possible\n" ;
                           }
                           else
                           {
                               cout << "Case #" << kase << ": Broken\n" ;
                           }
              }
              else cout << "Case #" << kase << ": Broken\n" ;
    }
    return 0;
}
