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
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int N,T;
double R[4],X[4],Y[4];

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
            scanf("%d",&N);
            Repi(N)
             {

                    scanf("%lf%lf%lf",X+i,Y+i,R+i);
             }
            double ans=R[0];
            if (N==2)
             {
                    ans=max(R[0],R[1]);
             }
            if (N==3)
             {
                    ans=1e100;
                    ans=min(ans , max( R[0] , (hypot(X[1]-X[2],Y[1]-Y[2]) + R[1]+R[2])/2.  ) );
                    ans=min(ans , max( R[1] , (hypot(X[0]-X[2],Y[0]-Y[2]) + R[0]+R[2])/2. ) );
                    ans=min(ans , max( R[2] , (hypot(X[1]-X[0],Y[1]-Y[0]) + R[1]+R[0])/2. ) );
             }
            printf("Case #%d: %.7lf\n",xx+1,ans);
        }
    return 0;
}
