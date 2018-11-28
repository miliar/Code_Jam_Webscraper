#include<iostream>

using namespace std;

int main()
{
    int T,N,sum,xsum,min,c;

    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        sum = 0;
        xsum = 0;
        min = 1000001;
        scanf("%d",&N);
        while(N--)
        {
            scanf("%d",&c);
            if(c<min)
            {
                min = c;
            }
            xsum^=c;
            sum+=c;
        }

        if(!xsum)
        {
            printf("Case #%d: %d\n",i+1,sum-min);
        }
        else
        {
            printf("Case #%d: NO\n",i+1);
        }
    }

    return 0;
}
