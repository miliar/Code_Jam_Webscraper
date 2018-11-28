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

int W,L,N;
LL r[1111];
LL x[1111],y[1111];



LL dist(LL x, LL y, LL xx, LL yy)
{ return (xx-x)*(xx-x)+(yy-y)*(yy-y); }


bool good(int num, LL xc, LL yc)
{
    FI(i,num) if (dist(x[i],y[i],xc,yc)<(r[i]+r[num])*(r[i]+r[num])) return false;
    return true;
}

bool pl(int num, LL xs, LL ys, LL xe, LL ye)
{
    while (xs<xe || ys<ye)
    {
        LL mx=xs+(xe-xs)/2;
        LL my=ys+(ye-ys)/2;
        if (good(num,mx,my)) { xe=mx; ye=my;}
        else {xs=(xs==xe)?xs:(mx+1); ys=(ye==ys)?ys:(my+1);}
    }
    if (good(num,xe,ye))
    {
        x[num]=xe;
        y[num]=ye;
        return true;
    } else return false;
}


void solution()
{
    int tn;
    scanf("%d",&tn);
    FI(it,tn)
    {
        scanf("%d%d%d",&N,&W,&L);
        FI(i,N) scanf("%lld",&r[i]);
        bool g=false;
        if (N==1) x[0]=0,y[0]=0,g=true; else
        do
        {
            x[0]=0;
            y[0]=0;
            bool placed=false;
            FOR(i,1,N)
            {
                placed=false;
                
                /*
                dout(i);
                FI(i,N) dout(x[i] << ' ' << y[i]);*/
                
                if (placed = pl(i,0,0,W,0))  continue;
                if (!placed) if (placed = pl(i,W,0,W,L))  continue;
                if (!placed) if (placed = pl(i,W,L,0,L))  continue;
                if (!placed) if (placed = pl(i,0,L,0,0))  continue;
                break;
            }
            if (placed) {g=true; break;}
            break;
        } while (next_permutation(r,r+N));
        
        printf("Case #%d:",it+1);
        if (!g) cout << "VERY BAD\n";
        FI(i,N) printf(" %lld %lld",x[i],y[i]);
        cout << endl;
        

        
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
