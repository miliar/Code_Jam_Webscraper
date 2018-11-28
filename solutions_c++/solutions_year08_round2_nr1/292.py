#include <vector>
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
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

LL X,Y,t;
LL p[3][3];


int main()
{
    scanf("%d",&t);

int n,A,B,C,D,x0,y0,M;
Repk(t)
{
    memset(p,0,sizeof(p));
    scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&x0,&y0,&M);
    X=x0,Y=y0; p[X%3][Y%3]++;
    for (int i=1;i<n;i++)
     {
            X=((LL)A*(LL)X+(LL)B)%(LL)M; Y=((LL)C*(LL)Y+(LL)D)%(LL)M;
            p[X%3LL][Y%3LL]++;
     }
    
    LL ans=0;
    int x3,y3;
    LL p1,p2,p3;
    for (int x1=0;x1<3;x1++)
    for (int y1=0;y1<3;y1++)
    if (p[x1][y1])
    {
      for (int x2=0;x2<3;x2++)
      for (int y2=0;y2<3;y2++)
      if (p[x2][y2])
       {
         x3=(12-x1-x2)%3; y3=(12-y1-y2)%3;
         p1=p[x1][y1],p2=p[x2][y2],p3=p[x3][y3];
         if (!p3) continue;
         if (x1==x2 && y1==y2) p2--;
         if (x1==x3 && y1==y3) p3--;
         if (x2==x3 && y2==y3) p3--;
         ans+=p1*p2*p3;
       //  if (p1*p2*p3)   printf("   %d%d %d%d %d%d = %d*%d*%d = %d\n",x1,y1,x2,y2,x3,y3,(int)p1,(int)p2,(int)p3,ans);
       }
    }
    
    cout<<"Case #"<<k+1<<": "<<ans/6LL<<"\n";
}   
    return 0;
}
