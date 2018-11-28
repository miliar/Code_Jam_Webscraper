#include <iostream>
#include <cstdio>
#include <list>
using namespace std;
list<int>g;
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int x,y=0;
    scanf("%d",&x);
    while (x--)
    {
        g.clear();
        y++;
        int r,k,n,i,j;
        scanf("%d %d %d",&r,&k,&n);
        int temp;
        for (i=0;i<n;i++)
        {
            scanf("%d",&temp);
            g.push_back(temp);
        }
        int sum=0;
        for (i=0;i<r;i++)
        {
            int sum1=0;
            for (j=0;j<n;j++)
            {
                int temp1;
                sum1+=g.front();
                if (sum1<=k)
                {
                    temp1=g.front();
                    g.pop_front();
                    g.push_back(temp1);

                }
                else
                {
                    sum1-=g.front();
                    break;
                }
            }
            sum+=sum1;
        }
        printf("Case #%d: %d\n",y,sum);
    }
}
