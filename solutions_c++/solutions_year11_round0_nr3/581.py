#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[1005],N;

int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("out.txt","w",stdout);

    int T,cas = 0;scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&N);
        for(int i = 0; i < N ;i++)scanf("%d",&a[i]);
        sort(a, a+N);
        int ans = 0, sum = 0;
        for(int i = 0; i < N; i++)
        {
            ans = ans^a[i];
            sum += a[i];
        }
        printf("Case #%d: ",++cas);
        if(ans)puts("NO");
        else printf("%d\n",sum-a[0]);
    }


    return 0;
}
