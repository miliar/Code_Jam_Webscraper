#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;++t)
    {
        int N,L,H,a[10010],ans;
        scanf("%d%d%d",&N,&L,&H);
        for (int i=0;i<N;++i)
            scanf("%d",&a[i]);
        bool f=false;
        for (ans=L;ans<=H&&!f;++ans)
        {
            f=true;
            for (int i=0;i<N&&f;++i)
                f = (a[i]%ans==0) || (ans%a[i]==0);

        }
        if (f)
            printf("Case #%d: %d\n",t,ans-1);
        else
            printf("Case #%d: NO\n",t);

    }

    return 0;
}
