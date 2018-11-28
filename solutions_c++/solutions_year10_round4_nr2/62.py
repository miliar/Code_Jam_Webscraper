#include <vector>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define F(i,n) for (int i=0;i<n;i++)
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int T;

const int MAXN = 1<<11;

int P;
int dp[MAXN][MAXN];
int M[MAXN];
int t[20][MAXN];

vector<int> go[MAXN][14];

const bool dbg = 0;

int solve(int pos, int mask)
{
    int &ret = dp[pos][mask];
    if (ret > -1)
        return ret;
    if (pos == (1<<P))
        {
            return ret = 0;
        }
    ret = 1000000000;

    int add = M[pos] - __builtin_popcount(mask);
    if (add < 0) add = 0;

   if (dbg) cout<<" at "<<pos<<" "<<mask<<" :add "<<add<<"\n";

    for (int i = 0; i < go[mask][add].size(); i++)
    {
        int temp = 0;
        int to = go[mask][add][i];
      if (dbg)  cout<<"  from "<<pos<<" "<<mask<<" to "<<to<<" : ";
        
        for (int i = P - 1, j = 1; i >= 0; i--, j++)
        {
            int match = pos / (1<<j);
            if ( ((1<<i)&mask) != ((1<<i)&to) )
            {
                temp += t[i][match];
               if (dbg) cout<<"("<<i<<","<<match<<") "<<t[i][match]<<" + ";
            }
        }
       if (dbg) cout<<"\n";
        
       if (dbg) cout<<"      ruin : ";
        for (int i = P - 1, j = 1; i >= 0; i--, j++)
        {
            int match = pos / (1<<j);
            int nmatch = (pos + 1) / (1<<j);
            if (match != nmatch)
            {
                to &= ~(1<<i);
             if (dbg)   cout<<i<<" ";
            }
        }
    if (dbg)    cout<<"\n";
        
        ret = min(ret, temp + solve(pos + 1, to));
    }
    
 if (dbg)   cout<<"    "<<pos<<" "<<mask<<" = "<<ret<<"\n";
    return ret;
}

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
            scanf("%d", &P);

    for (int i = 0; i < (1<<P); i++)
    {
        for (int k = 0; k <= P+1; k++)
            go[i][k].clear();
     for (int j = 0; j < (1<<P); j++)
      if ( (j & i) == i )
       {
            int add = __builtin_popcount(j ^ i);
           if (dbg) cout<<i<<" "<<add<<" -> "<<j<<"\n";
            go[i][add].push_back(j);
       }
    }


            for (int i = 0; i < (1<<P); i++)
            {
                scanf("%d", M+i);
                M[i] = P - M[i];
            }
            for (int i = P - 1; i >= 0; i--)
            {
                for (int j = 0; j < (1<<i); j++)
                {
                    scanf("%d", &t[i][j]);
            if (dbg)        cout<<t[i][j]<<" ";
                }
          if (dbg)     cout<<"\n";
            }
            
            memset(dp, -1, sizeof(dp));
            printf("Case #%d: %d\n", xx+1, solve(0, 0));
            cerr<<xx<<"\n";
     }
    return 0;
}
