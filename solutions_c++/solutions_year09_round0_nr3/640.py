//Tomasz Kulczyński
#include <cstdio>
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
#define COND 1
#define DB(x) { if(COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }

#define M 19
#define Q 10000

char s[513],w[]="welcome to code jam";
int t[M+1],e[M+1];


int main()
{
    int n;
    scanf("%d",&n);    
    gets(s);
    REP(cas,n)
    {
        int ret=0;
        gets(s);
        REP(j,M+1) t[j]=!j;
        for(int i=0;s[i];i++)    
        {
            e[0] = 1;
            REP(j,M) 
                e[j+1] = (t[j+1] + (s[i]==w[j] ? t[j] : 0)) % Q;
            ret += e[M];
            ret %= Q;
            REP(j,M) t[j] = e[j];
        }
        printf("Case #%d: %04d\n",cas+1,ret);
    }
    return 0;
}
