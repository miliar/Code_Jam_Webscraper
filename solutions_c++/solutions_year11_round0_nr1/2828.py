#include <cstdio>

using namespace std;
const char BotB='B';
const char BotO='O';
#define MAXN 100
//int bArr[MAXN];
//int oArr[MAXN];
int absoluteV(int val)
{
    return val<0?-val:val;
}
int main()
{
    int T,N,dis,round=1;
    scanf("%d",&T);
    char lab[2];
    while(T--)
    {
        int now=0,lastPosB=1,lastPosO=1,lastTimeB=0,lastTimeO=0;//,passedB=0,passO=0;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%s",lab);
            scanf("%d",&dis);
            if(lab[0]==BotB)
            {
                if(now-lastTimeB-absoluteV(dis-lastPosB)<0)
                    now+=absoluteV(dis-lastPosB)-now+lastTimeB+1;
                else now++;
                lastTimeB=now;
                lastPosB=dis;
            }else
            {
                if(now-lastTimeO-absoluteV(dis-lastPosO)<0)
                    now+=absoluteV(dis-lastPosO)-now+lastTimeO+1;
                else now++;
                lastTimeO=now;
                lastPosO=dis;
            }
        }
        printf("Case #%d: %d\n",round++,now);
    }
    return 0;
}
