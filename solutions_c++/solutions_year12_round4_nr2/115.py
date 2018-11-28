/*****************************************
*
* @ingroup UESTC_ACM,2012
* @param    B
* @author  a180285
*
*****************************************/

# include <assert.h>
# include <math.h>
# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <algorithm>
# include <iostream>
# include <string>
# include <queue>
# include <stack>
# include <map>
# include <set>
# include <vector>
# include <cstring>
# include <list>
# include <ctime>
# include <sstream>

# pragma comment (linker,"/STACK:16777216")

# define For(i,a)   for(i=0; i<(a); i++)
# define sz(a)      (sizeof(a))
# define MEM(a)     (memset((a),0,sizeof(a)))
# define MEME(a)    (memset((a),-1,sizeof(a)))
# define MEMX(a)    (memset((a),0xf,sizeof(a)))
# define pb(a)      push_back(a)

using namespace std;

typedef long long           ll      ;
typedef unsigned long long  ull     ;
typedef unsigned int        uint    ;
typedef unsigned char       uchar   ;
typedef istringstream        Iss     ;

template<class T> inline const T& MIN(const T& a,const T& b){return a<b? a : b;}
template<class T> inline const T& MAX(const T& a,const T& b){return a>b? a : b;}
template<class T> inline void checkmin(T &a,const T& b){if(a>b) a=b;}
template<class T> inline void checkmax(T &a,const T& b){if(a<b) a=b;}

const int oo=1<<30          ;
const double eps=1e-7       ;
const int N=1<<10               ;
const int M=1               ;
const ll P=10000000097ll    ;

struct cir
{
    double r, x, y;
    int id;
};

cir c[N];
int h,w;
int n;

int cmp_r(const cir& a,const cir& b)
{
    return a.r > b.r;
}

int cmp_id(const cir& a,const cir& b)
{
    return a.id < b.id;
}

int sgn(double x)
{
    return (x>eps) - (x<-eps);
}

int fcmp(double a,double b)
{
    return sgn(a-b);
}

double sqr(double x)
{
    return x*x;
}

void doit()
{
    scanf("%d", &n);
    scanf("%d %d", &w, &h);
    int i,j,k;
    For(i, n)
    {
        scanf("%lf", &c[i].r);
        c[i].id = i;
    }
    sort(c, c+n, cmp_r);
    c[0].x = c[0].y = 0.0;
    for(int i=1; i<n; i++)
    {
        double tx = c[i-1].x + c[i-1].r + c[i].r;
        double ty = 0;
        if( fcmp(tx, w) > 0 )
            tx = 0;
        For(j, i)
        {
            double dis = fabs(tx-c[j].x);
            if( fcmp(dis, c[j].r+c[i].r) > 0 )
                continue;
            double R = c[i].r + c[j].r;
            double dy = sqrt(R*R - dis*dis);
            checkmax(ty, c[j].y + dy);
        }
        assert( fcmp(ty, h) <= 0 );
        c[i].x = tx;
        c[i].y = ty;
    }
    sort(c, c+n, cmp_id);
    For(i, n)
        printf(" %lf %lf", c[i].x, c[i].y);
    puts("");
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T,_=0;
    scanf("%d",&T);
    while( _++ < T )
    {
        printf("Case #%d:", _);
        doit();
    }
    return 0;
}

/**

2
2 6 6
1 1
3 320 2
4 3 2
Case #1: 0.0 0.0 6.0 6.0
Case #2: 0.0 0.0 7.0 0.0 12.0 0.0

**/

