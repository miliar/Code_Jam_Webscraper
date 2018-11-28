#include <cstdio>
#include <deque>
#include <cstring>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);//*/
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;++t)
    {
        int N,min=10E7,sum=0,xr=0,x;
        scanf("%d",&N);
        for (int i=0;i<N;++i)
        {
            scanf("%d",&x);
            if (min>x)
                min = x;
            sum += x;
            xr ^= x;
        }
        printf("Case #%d: ",t);
        if (xr)
            printf("NO\n");
        else
            printf("%d\n",sum-min);
    }
    fclose(stdin);
    fclose(stdout);//*/
    return 0;
}
