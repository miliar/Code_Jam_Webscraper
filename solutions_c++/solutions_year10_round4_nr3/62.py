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
int R;

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
        scanf("%d", &R);
        set<PI> p;
        Repi(R)
        {
            int x,y;
            int x1,  y1,  x2,  y2;
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for (int x = x1; x <= x2; x++)
                for (int y = y1; y <= y2; y++)
                 {
                    p.insert(MP(x, y));
              //      cout<<x<<" "<<y<<"\n";
                 }
        }
        
        int cnt = 0;
        while (p.size())
        {
            set<PI> np = p;
            for (set<PI>::iterator it = p.begin(); it != p.end(); it++)
            {
                if (p.find(MP(it->x + 1, it->y - 1)) != p.end())
                {
                    np.insert(MP(it->x + 1, it->y));
                //    cout<<"   add "<<it->x + 1<<" "<<it->y<<"\n";
                }
            }
            for (set<PI>::iterator it = p.begin(); it != p.end(); it++)
            {
                if (p.find(MP(it->x - 1, it->y)) == p.end() && p.find(MP(it->x, it->y - 1)) == p.end())
                {
                    np.erase(*it);
               //     cout<<"   erase "<<it->x<<" "<<it->y<<"\n";
                }
            }
            cnt++;
            p = np;
        }
        
        printf("Case #%d: %d\n", xx+1, cnt);
        cerr<<xx<<" "<<cnt<<"\n";
     }
    return 0;
}
