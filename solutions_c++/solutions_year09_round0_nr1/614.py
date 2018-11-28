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

#define M 30
#define D 5013
#define L 17

char s[D][L];
bool t[L][M];
char buf[L];

int main()
{
    int l,d,n;
    scanf("%d %d %d",&l,&d,&n);    
    REP(i,d) scanf("%s",s[i]);
    REP(cas,n)
    {
        scanf("%s",buf);
        REP(j,l) REP(i,M) t[j][i] = 0;
        {int j=0;
        for(int i=0;buf[i];i++) if(buf[i]=='(')
        {
            while(buf[++i]!=')')
                t[j][buf[i]-'a']=1;
            j++;
        }
        else t[j++][buf[i]-'a']=1;}
        int ret = 0;
        REP(i,d)
        {
            bool ok = 1;
            REP(j,l) if(!t[j][s[i][j]-'a']) 
            {
                ok=0;
                break;
            }
            if(ok) ret++;
        }
        printf("Case #%d: %d\n",cas+1,ret);
    }
    return 0;
}
