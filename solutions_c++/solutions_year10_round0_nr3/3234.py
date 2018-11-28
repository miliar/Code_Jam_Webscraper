#include<stdio.h>
#include<queue>

using namespace std;


int main()
{
    int r,k,n,t;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int tmp;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
    {
        queue<int> q;
        scanf("%d%d%d",&r,&k,&n);
        for(int j = 0; j < n; j++)
        {
            scanf("%d",&tmp);
            q.push(tmp);
        }
        int euro = 0;
        for(int j = 0; j < r; j++)
        {
            int sum = 0;
            for(int x = 0; x < n; x++)
            {
                sum += q.front();
                if(sum <= k)
                {
                    q.push(q.front());
                    euro += q.front();
                    q.pop();
                }
                else
                    break;
            }
        }
        printf("Case #%d: %d\n",i,euro);
    }
    return 0;
}
