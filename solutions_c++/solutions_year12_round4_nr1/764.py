#pragma comment (linker, "/STACK:16777216")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <numeric>
#include <complex>
#include <string>
#ifdef IGEL_ACM
#include <ctime>
#endif

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> pnt;
typedef vector <int> VI;

#define FI(i,a) for (int i=0; i<(a); ++i)
#define FOR(i,s,e) for (int i=(s); i<(e); ++i)
#define MEMS(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair
#define ALL(a) a.begin(),a.end()
#define V(t) vector < t >
#define sz size()


#define dout(a) cerr << a << endl
#define sout(a) cerr << a << "  "


const double pi = 3.14159265358979323846264338327950288419716939937511;
const double eps = 1e-12;
//*
char ch_ch_ch[1<<20];
string gs() {scanf("%s",ch_ch_ch); return string(ch_ch_ch);}
string gl() {gets(ch_ch_ch); return string(ch_ch_ch);}
inline int gi() {int x; scanf("%d",&x); return x;}
//*/


// code starts here

int N,n;
int d[11111], l[11111], pr[11111];

void solution()
{
    int tn;
    scanf("%d",&tn);
    FI(it,tn)
    {
        scanf("%d",&N);
        n=N;
        FI(i,n) scanf("%d%d",&d[i+1],&l[i+1]);
        d[0]=0; l[0]=0;
        scanf("%d",&d[N+1]);
        l[N+1]=0;
        FI(i,N+2) pr[i]=-1;
        pr[1]=d[1];
        FOR(i,1,N+2) if (-1==pr[i]) break;
        else
        {
            int dx=pr[i];
            FOR(j,i+1,N+2) if (d[j]-d[i]>dx) break;
            else pr[j]=max(pr[j],min(l[j],d[j]-d[i]));
        }
        
        printf("Case #%d: ",it+1);
        if (pr[N+1]==-1) printf("NO\n"); else printf("YES\n");
        
    }
    
    
}

// code ends here

int main(int argc, char** argv)
{


#ifdef IGEL_ACM
    freopen("in.txt","r",stdin);
    //*
    freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout); //*/
    clock_t beg_time = clock();
#else
    //freopen(argv[1],"r",stdin);
    //freopen("c3.in", "r", stdin);
    //freopen("c3.out", "w", stdout);
#endif

        solution();


#ifdef IGEL_ACM
    fprintf(stderr,"*** Time: %.3lf ***\n",1.0*(clock()-beg_time)/CLOCKS_PER_SEC);
#endif

    return 0;
}
