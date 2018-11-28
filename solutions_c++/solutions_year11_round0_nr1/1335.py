#include<cstdio>
#include<algorithm>
using namespace std;
struct steps
{
    int x;
    bool flag;
}step[100];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++)
    {
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
            char c;
            int x;
            scanf(" %c%d",&c,&x);
            if (c=='O')
                step[i].flag=1;
            else
                step[i].flag=0;
            step[i].x=x;
        }
        int pot=0,pbt=0;
        int pop=1,pbp=1;
        int t=0;
        for (int i=0;i<n;i++)
            if (step[i].flag)
            {
                pot=t=max(pbt,abs(step[i].x-pop)+pot)+1;
                pop=step[i].x;
            }
            else
            {
                pbt=t=max(pot,abs(step[i].x-pbp)+pbt)+1;
                pbp=step[i].x;
            }
        printf("Case #%d: %d\n",cas,t);
    }
    return 0;
}
