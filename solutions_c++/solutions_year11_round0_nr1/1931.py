#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define MAX 100
struct Order
{
    char who;
    int pos;
    int dis;
}orders[MAX];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int nT,t=0;
    scanf("%d",&nT);
    while(nT--)
    {
        int n;
        int oLastPos=1;
        int bLastPos=1;
        int oLastTime=0;
        int bLastTime=0;
        bool oFirst=true;
        bool bFirst=true;
        int time=0;
        scanf("%d",&n);
        for(int i=0;i<n;++i)
        {
            char who;
            int pos;
            scanf(" %c%d",&who,&pos);
            int dis;
            if(who=='O')
            {
                dis=abs(pos-oLastPos);
                oLastPos=pos;
				oLastTime=oLastTime+dis+1;
                if(oLastTime>=time)
                	time=oLastTime;
				else
					oLastTime=time;
				//printf("oLasttime: %d\n",oLastTime);
            }
            else
            {
                dis=abs(pos-bLastPos);
                bLastPos=pos;
                bLastTime=bLastTime+dis+1;
                if(bLastTime>time)
                	time=bLastTime;
				else
					bLastTime=time;
            }
            ++time;
        }
        printf("Case #%d: %d\n",++t,time-1);
    }
}
