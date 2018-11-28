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

#define M 57
#define inf (1<<25)

char s[M][M],org[M][M];
int t[M][M][2*M];
bool cc[M][M][3];

void ruch(int i,int j,int cost,int f,int uu=0)
{
    while(s[i+1][j]!='#') i++,f--,uu=0;
    if(f<0) return;
  //  printf("%d %d %d :: %d (%d)\n",i,j,uu,cost,t[i][j][uu]);
    t[i][j][uu] = min(t[i][j][uu], cost);
}

int main()
{
    int dd;
    scanf("%d",&dd);    
    FOR(cas,1,dd)
    {
        int r,c,f;
        scanf("%d %d %d",&r,&c,&f);
        REP(i,r) scanf("%s",s[i]);
        REP(j,c) s[r][j] = '#';
        REP(i,r) REP(j,c) REP(uu,2*M) t[i][j][uu] = inf, cc[i][j][uu] = 0, org[i][j] = s[i][j];
        t[0][0][0] = 0;
        REP(i,r-1) while(1)
        {
            int j = 0, ju = 0;
            while(ju<2*M && cc[i][j][ju])
            {
                while(j<c && cc[i][j][ju]) j++;
                if(j==c) ju++,j=0;
            }
            if(ju==2*M) break;
            REP(k,c) REP(uu,2*M) if(cc[i][k][uu]==0 && t[i][k][uu] < t[i][j][ju]) j=k,ju=uu;
            if(t[i][j][ju] >= inf) break;
//           printf("%d %d %d :: %d\n",i,j,ju,t[i][j][ju]);
            if(ju <  M) FOR(q,0,ju) s[i][j+q] = '.';
            if(ju >= M) FOR(q,0,ju-M) s[i][j-q] = '.';

            if(j && s[i][j-1]=='.') 
            {
                if(ju && ju<M) ruch(i,j-1,t[i][j][ju],f,ju+1);
                if(ju >= M)    ruch(i,j-1,t[i][j][ju],f, ju==M+1 ? 0 : (ju-1) );
                if(ju == 0)    ruch(i,j-1,t[i][j][ju],f, 1);
            }
            if(j+1<c && s[i][j+1]=='.') 
            {
                if(ju && ju<M) ruch(i,j+1,t[i][j][ju],f,ju-1);
                if(ju >= M)    ruch(i,j+1,t[i][j][ju],f,ju+1);
                if(ju == 0)    ruch(i,j+1,t[i][j][ju],f, M+1);
            }
            if(j && s[i][j-1]!='#' && s[i+1][j-1]=='#') ruch(i+1,j-1,t[i][j][ju]+1,f-1);
            if(j+1<c && s[i][j+1]!='#' && s[i+1][j+1]=='#') ruch(i+1,j+1,t[i][j][ju]+1,f-1);

            {
            int q = 2, ok = 1;
            if(s[i][j+1]=='.' && s[i+1][j+1]=='#')
            while(j+q<c && s[i][j+q]=='.' && s[i+1][j+q]=='#') 
            {
                ruch(i+1,j+1,t[i][j][ju]+q,f-1,q-1);
                if(s[i+2][j+q-1]=='.') ok = 0;
                if(ok) ruch(i+1,j+q,t[i][j][ju]+q,f,q-1+M);
                q++;
            }

            q = 2; ok = 1;
            if(s[i][j-1]=='.' && s[i+1][j-1]=='#')
            while(j>=q && s[i][j-q]=='.' && s[i+1][j-q]=='#') 
            {
                ruch(i+1,j-1,t[i][j][ju]+q,f-1,q+M-1);
                if(s[i+2][j-q+1]=='.') ok = 0;
                if(ok) ruch(i+1,j-q,t[i][j][ju]+q,f,q-1);
                q++;
            }
            }

//            if(j>=2 && s[i][j-1]=='.' && s[i][j-2]=='.' && s[i+1][j-1]=='#' && s[i+1][j-2]=='#') ruch(i+1,j-1,t[i][j][ju]+2,f-1,2);

            if(ju <  M) FOR(q,0,ju) s[i][j+q] = org[i][j+q];
            if(ju >= M) FOR(q,0,ju-M) s[i][j-q] = org[i][j-q];

            cc[i][j][ju] = 1;
        }
        int ret = inf;
        REP(j,c) ret = min(ret, t[r-1][j][0]);
        printf("Case #%d: ",cas);
        if(ret < inf) printf("Yes %d\n",ret);
        else puts("No");
    }
    return 0;
}
