
#include <math.h>
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
    int n;
    int m;
    int ostep, bstep;
    int op, bp;
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&n);
    char robot[8];
    int postion;
    int count;
    int i;
    for(i=0; i<n; i++)
    {
        scanf("%d",&m);
        op = 1;
        bp = 1;
        ostep = 0;
        bstep = 0;
        int count = 0;
        while(m--)
        {
            scanf("%s %d",robot,&postion);
            if(robot[0] == 'B')
            {
                int push = max(abs(postion - bp) - bstep,0) + 1;
                bstep = 0;
                ostep += push;
                count += push;
                bp = postion;
            }
            else
            {
                int push = max(abs(postion - op) - ostep,0) + 1;
                ostep = 0;
                bstep += push;
                count += push;
                op = postion;
            }
        }
        printf("Case #%d: %d\n",i+1,count);
    }
	return 0;
}

