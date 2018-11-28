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
#define EPS 1e-8

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int T;
int N, M;

const int MAXN = 6000;
const int MAXM = 6000;

PD p[MAXN], q[MAXN];
const PD shit = MP(1e100, 1e100);

double dist(const PD &A, const PD &B)
{
    return sqrt(sqr(A.x-B.x) + sqr(A.y-B.y));
}

double len[MAXN];

double area(double R, double a)
{
    double c = sqrt(R * R * 2 - R * R * 2 * cos(a));
    double p = R + R + c;
    p /= 2;
    double tri = sqrt( p * (p - R) * (p - R) * (p - c) );
    double areaa = R * R * a;
    return areaa - tri;
}

double intersect(const PD &C1, double R1, const PD &C2, double R2)
{
    double d = dist(C1, C2);
    if ( R1 + R2 < d + EPS )
    {
        return 0;
    }
    double a1, a2;
    
    double cosA1 = sqr(R2) - (sqr(d) + sqr(R1));
    cosA1 /= - 2 * d * R1;
    a1 = acos(cosA1);

    double cosA2 = sqr(R1) - (sqr(d) + sqr(R2));
    cosA2 /= - 2 * d * R2;
    a2 = acos(cosA2);
    
    a1 += a1;
    a2 += a2;
    
    
    double area = 0.5 * a1 * R1 * R1 - 0.5 * R1 * R1 * sin(a1);
    area += 0.5 * a2 * R2 * R2 - 0.5 * R2 * R2 * sin(a2);
    
    return area;
}

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
        scanf("%d%d", &N, &M);
        for (int i = 0; i < N; i++)
        {
            scanf("%lf %lf", &p[i].x, &p[i].y);
        }
        for (int i = 0; i < M; i++)
        {
            scanf("%lf %lf", &q[i].x, &q[i].y);
        }
        
        cout<<"Case #"<<xx+1<<": ";
        for (int bucket = 0; bucket < M; bucket++)
        {
            PD b = q[bucket];
            for (int i = 0; i < N; i++)
            {
                len[i] = dist(p[i], b);
            }
            
            double area = intersect(p[0], len[0], p[1], len[1]);
            cout<<setprecision(8)<<fixed<<area;
            if (bucket < M - 1)
                cout<<" ";
            else
                cout<<"\n";
        }
     }
    return 0;
}
