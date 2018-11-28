/*****************************************
*
* @ingroup UESTC_ACM,2012
* @param   A
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
const int N=1<<20               ;
const int M=1               ;
const ll P=10000000097ll    ;

struct dot
{
    int d, l, dis;
};

dot t[N];

int doit()
{
    MEM(t);
    int i,j,k;
    int n;
    int len;
    scanf("%d", &n);
    For(i, n)
    {
        scanf("%d %d", &t[i].d, &t[i].l);
    }
    scanf("%d", &len);
    t[0].dis = t[0].d;
    For(i, n)
    {
        checkmin(t[i].dis, t[i].l);
        if( t[i].d + t[i].dis >= len )
            return 1;
        for(j=i+1; j<n && t[i].d+t[i].dis>=t[j].d; j++)
        {
            checkmax(t[j].dis, t[j].d-t[i].d);
        }
    }
    return t[n-1].d + t[n-1].dis >= len;
}

int main()
{
    freopen("a.in","r", stdin);
    freopen("a.out", "w", stdout);
    int T,_=0;
    scanf("%d",&T);
    while( _++ < T )
    {
        int ans = doit();
        printf("Case #%d: %s\n", _, ans? "YES":"NO");
    }
    return 0;
}

/**

4
3
3 4
4 10
6 10
9
3
3 4
4 10
7 10
9
2
6 6
10 3
13
2
6 6
10 3
14

Case #1: YES
Case #2: NO
Case #3: YES
Case #4: NO

**/

