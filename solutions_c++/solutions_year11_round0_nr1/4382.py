#include <stdio.h>
#include <stdlib.h>

char robot[200];
int  id[200];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outa.out", "w", stdout);

    int t, count=1;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf(" %c %d", &robot[i], &id[i]);
        int otime=0;
        int btime=0;
        int opos=1;
        int bpos=1;
        int total=0;
        for (int i=0;i<n;i++)
        {
            if (robot[i]=='O')
            {
                if (btime>=abs(id[i]-opos))
                {
                    otime+=1;
                    total+=1;
                    btime=0;
                }
                else
                {
                    otime+=abs(id[i]-opos)+1-btime;
                    total+=abs(id[i]-opos)+1-btime;
                    btime=0;
                }
                opos=id[i];
            }
            else
            {
                if (otime>abs(id[i]-bpos))
                {
                    btime+=1;
                    total+=1;
                    otime=0;
                }
                else
                {
                    btime+=abs(id[i]-bpos)+1-otime;
                    total+=abs(id[i]-bpos)+1-otime;
                    otime=0;
                }
                bpos=id[i];
            }
        }
        printf("Case #%d: %d\n", count++, total);
    }
    return 0;
}
