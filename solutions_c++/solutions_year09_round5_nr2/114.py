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

int licz(int m)
{
    if(!m) return 0;
    return m%2+licz(m/2);
}

#define M 113
#define MM 27

int ret[11],u[M];
int t[M][MM];
vector<string> q;
#define Q 10009

int k,n;

void go(int bi)
{
    if(bi < k)
    {
        REP(i,n)
        {
            REP(j,MM) u[j] += t[i][j];
            go(bi+1);
            REP(j,MM) u[j] -= t[i][j];
        }
    }
            FORE(i,q)
            {
                int w = 1;
                FORE(j,*i) w = w * u[*j - 'a'] % Q;
                ret[bi] = (ret[bi] + w) % Q;
            }

}

int main()
{
    int dd;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        char s[M];
        scanf("%s %d %d",s,&k,&n);
        REP(i,k+1) ret[i] = 0;
        q.clear();
        q.push_back("");
        REP(i,MM) u[i] = 0;
        REP(i,M) REP(j,MM) t[i][j] = 0;
        for(int i=0;s[i];i++) if(s[i]=='+') q.push_back("");
        else q.back()+=s[i];
        REP(i,n) 
        {
            scanf("%s",s);
            for(int j=0;s[j];j++) t[i][s[j]-'a']++;
        }
        go(0);
        printf("Case #%d:",cas);
        REP(i,k) printf(" %d",ret[i+1]);
        puts("");
    }
    return 0;
}
