/*****************************************
*
* 2011,UESTC_ACM
* Magicka
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
const int N=1               ;
const int M=1               ;
const ll P=10000000097ll    ;

char to[32][32];
bool op[32][32];
string in,out;
int has[32];

void read()
{
    int n;
    int i,j,k;
    char s[8];
    int u,v,t;
    MEM(to);
    MEM(op);
    scanf("%d",&n);
    For(i,n)
    {
        scanf("%s",s);
        u = s[0] - 'A';
        v = s[1] - 'A';
        t = s[2];
        to[u][v] = to[v][u] = t;
    }
    scanf("%d",&n);
    For(i,n)
    {
        scanf("%s",s);
        u = s[0] - 'A';
        v = s[1] - 'A';
        op[u][v] = op[v][u] = 1;
    }
    scanf("%d",&n);
    cin >> in;
    //printf("in ok!\n");
}

char can(char u,char v)
{
    u -= 'A';
    v -= 'A';
    return to[u][v];
}

int cls(char u)
{
    u -= 'A';
    int i;
    For(i,32)
        if( op[i][u] && has[i] )
            return 1;
    return 0;
}

void doit()
{
    int i,n;
    n = in.size();
    int tn;
    out = "";
    MEM(has);
    For(i,n)
    {
        tn = out.size();
        if( tn <= 0 )
        {
            has[ in[i]-'A' ]++;
            out += in[i];
        }
        else if( can(out[tn-1],in[i])>0 )
        {
            has[ out[tn-1]-'A' ]--;
            out[ tn-1 ] = can(out[tn-1],in[i]);
        }
        else if( cls(in[i]) )
        {
            MEM(has);
            out = "";
        }
        else
        {
            has[ in[i]-'A' ]++;
            out += in[i];
        }
    }
}

void pt()
{
    int n;
    int i;
    n = out.size();
    if( n>0 )
        putchar(out[0]);
    for(i=1;i<n;i++)
        printf(", %c",out[i]);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T,_=0;
    scanf("%d",&T);
    while( _++ < T )
    {
        read();
        doit();
        printf("Case #%d: [",_);
        pt();
        puts("]");
    }
    return 0;
}
