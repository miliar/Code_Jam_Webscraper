#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int cas,cc;
    int r,k,n,i,temp,num;
    double sum;
    scanf("%d",&cas);
    for(cc=1;cc<=cas;cc++)
    {
        scanf("%d %d %d",&r,&k,&n);
        sum=0;
        queue <int> q;
        for(i=0;i<n;i++)
        {
            scanf("%d",&temp);
            q.push(temp);
        }
        for(i=0;i<r;i++)
        {
            num=0;
            queue <int> in;
            for(;;)
            {
                if(q.empty()) break;
                if(num+q.front()>k) break;

                num+=q.front();
                in.push(q.front());
                q.pop();
            }
            sum+=num;
            while(!in.empty())
            {
                q.push(in.front());
                in.pop();
            }
        }
        printf("Case #%d: %.0lf\n",cc,sum);
    }

    return 0;
}
