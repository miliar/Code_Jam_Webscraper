
#include <iostream>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int kCase=1;kCase<=T;kCase++)
    {
        int BPos = 1;
        int BTime = 0;
        int OPos = 1;
        int OTime = 0;

        int N;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            char color;
            int num;
            scanf(" %c %d",&color, &num);
            switch(color)
            {
            case 'B':
                BTime += abs(num - BPos) + 1;
                if(BTime<=OTime)
                {
                    BTime = OTime+1;
                }
                BPos = num;
                break;
            case 'O':
                OTime += abs(num - OPos) + 1;
                if(OTime<=BTime)
                {
                    OTime=BTime+1;
                }
                OPos = num;
                break;
            }
        }
        printf("Case #%d: %d\n",kCase, max(BTime,OTime));
    }
}



namespace{
struct Test
{
    Test()
    {
        freopen("../Resource/A-large.in","r",stdin);
        freopen("../Resource/A-large.out","w",stdout);
    }

    ~Test()
    {
        //scanf("%*s");
    }
}g_Test;
}

