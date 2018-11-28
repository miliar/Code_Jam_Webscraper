/*****************************************
*
* 2011,UESTC_ACM
* Bot Trust
* By a180285
*
*****************************************/

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

# define For(i,a)   for((i)=0;i<(a);(i)++)
# define MAX(x,y)   ((x)>(y)? (x):(y))
# define MIN(x,y)   ((x)<(y)? (x):(y))
# define sz(a)      (sizeof(a))
# define MEM(a)     (memset((a),0,sizeof(a)))
# define MEME(a)    (memset((a),-1,sizeof(a)))
# define MEMX(a)    (memset((a),0x7f,sizeof(a)))
# define pb(a)      push_back(a)

using namespace std;

typedef long long           ll      ;
typedef unsigned long long  ull     ;
typedef unsigned int        uint    ;
typedef unsigned char       uchar   ;


template<class T> inline void checkmin(T &a,T b){if(a>b) a=b;}
template<class T> inline void checkmax(T &a,T b){if(a<b) a=b;}

const int oo=1<<30          ;
const double eps=1e-7       ;
const int N=128               ;
const int M=1               ;
const ll P=10000000097ll    ;

queue<int> a,b;
int q[N];
int n;

void read()
{
    while( a.size()>0 )
        a.pop();
    while( b.size()>0 )
        b.pop();
    int t;
    char s[8];
    int i;
    scanf("%d",&n);
    For(i,n)
    {
        scanf("%s%d", s, &t);
        q[i] = ('B'!=s[0]);
        if( 'B' == s[0] )
            a.push(t);
        else
            b.push(t);
    }
}

int doit()
{
    int ans = 0;
    int ta,tb;
    int now;
    int na,nb;
    int to;
    na = nb = 1;
    ta = tb = now = 0;
    int i,j,k;
    For(i,n)
    {
        if( q[i] == 0 )
        {
            to = a.front();
            a.pop();
            ta += abs(to-na) + 1;
            checkmax(ta, now+1);
            now = ta;
            na = to;
        }
        else
        {
            to = b.front();
            b.pop();
            tb += abs(to-nb) + 1;
            checkmax(tb, now+1);
            now = tb;
            nb = to;
        }
        //printf("now = %d\n",now);
    }
    return now;
}

int main()
{
    int T,_=0;
    int ans;

//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);

    scanf("%d",&T);
    while( _++ < T )
    {
        read();
        ans = doit();
        printf("Case #%d: %d\n",_,ans);
    }
    return 0;
}
