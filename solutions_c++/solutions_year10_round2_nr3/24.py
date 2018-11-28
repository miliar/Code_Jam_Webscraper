
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

#define M 513

int newt[M][M], t[M][M];
int Q = 100003;

int test()
{
    int n;
    scanf("%d",&n);
    newt[0][0] = 1;
    FOR(i,1,n) 
    {
        FOR(j,1,i) newt[i][j] = (newt[i-1][j-1] + newt[i-1][j]) % Q;
        newt[i][0] = 1;
    }
    t[1][0] = 1;
    FOR(i,2,n) FOR(k,1,i-1) 
    {
        t[i][k] = 0;
        FOR(x,0,k-1) t[i][k] += ((ll)t[k][x] * newt[i-1-k][k-x-1]) % Q;
        t[i][k] %= Q;
    }
    int ret = 0;
    FOR(x,0,n-1) ret += t[n][x];
    return (ret%Q + Q ) % Q;
}

int main()
{
    int dd,cas;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        printf("Case #%d: %d\n",cas, test());
    }
    return 0;
}
