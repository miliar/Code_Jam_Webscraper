#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int currentPosForO,currentPosForB,lastTimeForO,lastTimeForB,lastTime;

    char who;
    int which;

    int T,N;
    scanf("%d",&T);

    for(int i=0;i<T;i++)
    {
        currentPosForO=1;
        currentPosForB=1;
        lastTimeForO=0;
        lastTimeForB=0;
        lastTime=0;

        scanf("%d",&N);
        for(int j=0;j<N;j++)
        {
            getchar();
            who=getchar();
            scanf("%d",&which);
            if(who=='O')
            {
                int posDif;
                if(currentPosForO<which)
                  posDif=which-currentPosForO;
                else
                  posDif=currentPosForO-which;

                if(lastTimeForO+posDif>lastTime)
                   lastTime=lastTimeForO+posDif+1;
                else
                   lastTime=lastTime+1;
                currentPosForO=which;
                lastTimeForO=lastTime;
            }
            else
            {
                int posDif;
                if(currentPosForB<which)
                  posDif=which-currentPosForB;
                else
                  posDif=currentPosForB-which;

                if(lastTimeForB+posDif>lastTime)
                  lastTime=lastTimeForB+posDif+1;
                else
                  lastTime=lastTime+1;
                currentPosForB=which;
                lastTimeForB=lastTime;
            }
        }//for
        printf("Case #%d: %d\n",i+1,lastTime);
    }//for
    return 0;
}
