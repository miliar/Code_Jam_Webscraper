// --- BBG v2.1b ---
#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<time.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<utility>
#include<map>
#include<set>
#include<string.h>
#include<string>
//
using namespace std;
//
//#define ONLINE_JUDGE BOBOGEI
#ifdef ONLINE_JUDGE
#define PP ;
#else
#define PP system("pause");
#endif
#define REP(n,i) for(int (i)=0;(i)<(n);(i)++)
#define CDREP(n,i) for(int (i)=((n)-1);(i)>=0;(i)--)
#define FOR(s,e,i) for(int (i)=(s);(i)<(e);(i)++)
#define _SZ(n) memset((n),0,sizeof(n))
#define _SMO(n) memset((n),-1,sizeof(n))
#define _MC(n,m) memcpy((n),(m),sizeof(n))
#define _F first
#define _S second
#define _MP(a,b) make_pair((a),(b))
#define _PB(a) push_back((a))
//
typedef unsigned int uint;
typedef long long i64;
typedef unsigned long long ui64;
typedef vector<int> vint;
typedef pair<int,int> pii;
const int INF = 1029384756;
const double PI = acos(-1);
const double EPS = 0.0000000304;
//
typedef pair<i64,i64> pll;
const int MAX = 1234;
//
int T;
int N,W,L;
bool sw;
pii ip[MAX];
pii ans[MAX];
//
int main()
{
    freopen("cj/B2.in","r",stdin);
    freopen("cj/B4.out","w",stdout);
    scanf("%d",&T);
    REP(T,chiisanatenohira)
    {
        sw=0;
        scanf("%d%d%d",&N,&W,&L);
        if(W<L)
        {
            swap(W,L);
            sw=1;
        }
        REP(N,i)
        {
            int t;
            scanf("%d",&t);
            ip[i]=_MP(t,i);
        }
        sort(ip,ip+N);
        reverse(ip,ip+N);
        int nid=0,nr=-1,nx,ly,lx,my,qy;

        while(nid<N)
        {
            int ns=ip[nid]._F;
            if(nr==-1)
            {
                nr++;
                ans[ip[nid]._S]=_MP(0,0);
                nid++;
                lx=qy=0;
                nx=my=ly=ns;
            }else if(nr==0)
            {
                if(lx+ns>W)
                {
                    //puts("123");
                    nr++;
                    qy=my;
                    lx=0;
                }else if(ly==0)
                {
                    nx=lx+ns+ns;
                    //printf("%d,%d<",nx,lx);
                    //puts("123");
                    ans[ip[nid++]._S]=_MP(lx+ns,0);
                    ly=ns;
                }else if(ly+ns*2<=my)
                {//puts("1234");
                    ans[ip[nid++]._S]=_MP(lx+ns,ly+ns);
                    ly=ly+ns+ns;
                }else
                {
                    //puts("123");
                    //printf("%d,%d|",nx,lx);
                    lx=nx;
                    ly=0;
                }
            }else
            {
                if(lx==0)
                {
                    //puts("345");

                    my=qy+ns+ns;
                    ans[ip[nid++]._S]=_MP(0,qy+ns);
                    ly=qy;
                    lx=ns;
                }else if(lx+ns>W)
                {
                    //printf("%d ",lx);
                    nr++;
                    qy=my;
                    lx=0;
                }else if(ly+ns*2<=my)
                {
                    //printf("%d=",lx);
                    ans[ip[nid++]._S]=_MP(lx+ns,ly+ns);
                    if(ly==qy)
                    {
                        nx=lx+ns+ns;
                    }
                    //printf("%d|",lx+ns);
                    ly+=ns*2;
                }else
                {
                    lx=nx;
                    //printf("%d<",lx);

                    ly=qy;
                }
            }
        }
        printf("Case #%d:",chiisanatenohira+1);
        REP(N,i)
        {
            if(sw)
            {
                swap(ans[i]._F,ans[i]._S);

            }
            printf(" %d %d",ans[i]._F,ans[i]._S);
        }
    }
}
