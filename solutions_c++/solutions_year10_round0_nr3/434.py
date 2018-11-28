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
const int MAXN = 1024;
int g[MAXN];

int ride[MAXN];
long long prof[MAXN];

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
        int R, k, N;
        scanf("%d%d%d", &R, &k, &N);
        Repi(N)
        {
            scanf("%d", g + i);
        }
        memset(ride, -1, sizeof(ride));
        memset(prof, -1, sizeof(prof));
        int group = 0;
        long long profit = 0;
        for (int r = 0; r < R; r++)
        {
            //cerr<<" ride "<<r<<" from group "<<group<<":\n";
            int total = 0;
            if (ride[group] > -1)
            {
                //cerr<<"    cycle at ride "<<r<<": old ride "<<ride[group]<<" old profit "<<prof[group]<<"\n";
                profit += (profit - prof[group]) * (long long)((R - r) / (r - ride[group]));
                r = R - (R - r) % (r - ride[group]) - 1;
                memset(ride, -1, sizeof(ride));
                continue;
            }
            while (total + g[group] <= k && ride[group] != r)
            {
                if (total == 0)
                {
                    ride[group] = r;
                    prof[group] = profit;
                }
                total += g[group];
                group++;
                if (group == N) group = 0;
            }
            profit += total;
            //cerr<<"      to group "<<group<<": total "<<total<<" ppl; profit "<<profit<<"\n";
        }
        
        cout<<"Case #"<<xx + 1<<": "<<profit<<"\n";
     }
    return 0;
}
