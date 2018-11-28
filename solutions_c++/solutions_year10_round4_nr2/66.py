
//Tomasz Kulczyński
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }

int t[4213][13];
int c[4213];

void test()
{
    int p;
    scanf("%d",&p);
    int n = 1;
    REP(i,p) n*=2;
    REP(i,n+n) REP(j,p+1) t[i][j] = 1<<29;
    REP(i,n) 
    {
        int x;
        scanf("%d",&x);
        REP(j,x+1) t[n+i][j] = 0;
    }
    int pocz = n;
    REP(o,p)
    {
        pocz /= 2;
        REP(i, pocz)
            scanf("%d",&c[pocz+i]);
    }
    FORD(i,n-1,1) REP(j,p)
    {
        t[i][j] = min(t[i+i][j] + t[i+i+1][j] + c[i], min(1<<29, t[i+i][j+1] + t[i+i+1][j+1]));
//        printf("%d %d :: %d\n",i,j,t[i][j]);
    }
    printf("%d\n",t[1][0]);
}

int main()
{
    int dd,cas;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        printf("Case #%d: ",cas);
        test();
    }
    return 0;
}
