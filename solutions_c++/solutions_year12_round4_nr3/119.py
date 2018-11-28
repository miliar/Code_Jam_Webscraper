/*****************************************
*
* @ingroup UESTC_ACM,2012
* @param   C
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
const int N=3<<10               ;
const int M=1               ;
const ll P=10000000097ll    ;

int h[N];
int n;
int v[N];

void read()
{
    scanf("%d", &n);
    int i;
    For(i, n-1)
        scanf("%d", &h[i]);
}

int imp()
{
    int i,j,k;
    for(i=0; i<n-1; i++)
    {
        int t = h[i];
        for(j=i+1; j<t-1; j++)
            if( h[j] > t )
                return 1;
    }
    return 0;
}

int chk(int id,int m)
{
    m--;
    int i;
    int y2 = v[m]-v[id];
    int x2 = m - id;
    for(i=id+1; i<m; i++)
    {
        int y1 = v[i] - v[id];
        int x1 = i - id;
        if( y2*x1 <= y1*x2 )
            return 0;
    }
    for(i=m+1; i<n; i++)
    {
        int y1 = v[i] - v[id];
        int x1 = i - id;
        if( y2*x1 < y1*x2 )
            return 0;
    }
    return 1;
}

int rad()
{
    int i,j,k;
    For(i, n)
        v[i] = rand();
    For(i, n-1)
        if( !chk(i, h[i]) )
        {
//            printf(" %d \n", i);
//            For(i, n)
//                printf(" %d", v[i]);
//            system("pause");
            return 0;
        }
    For(i, n)
        printf(" %d", v[i]);
    return 1;
}

void doit()
{
    if( imp() )
    {
        puts(" Impossible");
        return ;
    }
    while( !rad() )
        ;
    puts("");
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int T,_=0;
    scanf("%d",&T);
    while( _++ < T )
    {
        read();
        printf("Case #%d:", _);
        doit();
    }
    return 0;
}

/**

4
6
2 3 4 5 6
4
4 4 4
4
3 4 4
4
4 3 4

Case #1: 10 10 10 10 10 2
Case #2: 10 20 40 80
Case #3: Impossible
Case #4: 5 3 6 8

**/


