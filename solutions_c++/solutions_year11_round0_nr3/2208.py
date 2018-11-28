/*****************************************
*
* 2011,UESTC_ACM
* Candy Splitting
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
const int N=1024               ;
const int M=1               ;
const ll P=10000000097ll    ;

int n;
int a[N];
int sum;

void read()
{
    int i;
    scanf("%d",&n);
    For(i,n)
        scanf("%d",&a[i]);
    sum = 0;
    For(i,n)
        sum ^= a[i];

}

int def()
{
    if( sum!=0 )
        return 0;
    sort(a,a+n);
    int ans = 0;
    int i;
    for(i=1;i<n;i++)
        ans += a[i];
    return ans;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,_=0;
    int ans;
    scanf("%d",&T);
    while( _++ < T )
    {
        read();
        ans = def();
        printf("Case #%d: ",_);
        if( ans>0 )
            printf("%d\n",ans);
        else
            puts("NO");
    }
    return 0;
}
