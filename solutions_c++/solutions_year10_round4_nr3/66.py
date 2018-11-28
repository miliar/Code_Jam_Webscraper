
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

#define M 113

bool t[M][M];

void test()
{
    int n;
    scanf("%d",&n);
    REP(i,M) REP(j,M) t[i][j] = 0;
    REP(i,n)
    {
        int x,y, a,b;
        scanf("%d %d %d %d",&x,&y,&a,&b);
        FOR(i,x,a) FOR(j,y,b) t[i][j] = 1;
    }
    int ret = 0, ok = 1;
    while(ok)
    {
        ok = 0;
        ret++;
        FORD(i,M-1,1) FORD(j,M-1,1) 
        {
            if(t[i][j] && !t[i-1][j] && !t[i][j-1]) 
                t[i][j] = 0;
            if(!t[i][j] && t[i-1][j] && t[i][j-1]) 
                t[i][j] = 1;
            if(t[i][j])
                ok = 1;
        }
    }
    printf("%d\n",ret);
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
