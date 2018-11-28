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

#define M 113

int u[M*M];

int uw(int x)
{
    if(x==u[x]) return x;
    return u[x] = uw(u[x]);
}

int ww[M][M];
int bla[M*M];
int xx[4]={-1,0,0,1};
int yy[4]={0,-1,1,0};

int main()
{
    int dd;
    scanf("%d",&dd);    
    REP(cas,dd)
    {
        int h,w;
        scanf("%d %d",&h,&w);
        REP(i,h) REP(j,w) scanf("%d",&ww[i][j]);
        REP(i,h) REP(j,w) 
        {
            int mi = ww[i][j], kier = -1;
            REP(k,4) if(i+xx[k]>=0 && i+xx[k]<h && j+yy[k]>=0 && j+yy[k]<w && ww[i+xx[k]][j+yy[k]]<mi)
            {
                kier = k;
                mi = ww[i+xx[k]][j+yy[k]];
            }
            if(kier==-1) u[i*w+j] = i*w+j;
            else u[i*w+j] = (i+xx[kier])*w+(j+yy[kier]);
            bla[i*w+j] = 0;
        }
        REP(i,w*h) uw(i);
        int g=1;
        REP(i,w*h) if(!bla[u[i]]) bla[u[i]] = g++;
        printf("Case #%d:\n",cas+1);
        REP(i,h) REP(j,w) printf("%c%c",'a'+bla[u[i*w+j]]-1,j==w-1?'\n':' ');
    }
    return 0;
}
