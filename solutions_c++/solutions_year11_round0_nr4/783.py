#include <cstdio>
using namespace std;

int main ()
{
    freopen("input.in","r",stdin);freopen("output.out","w",stdout);
    int T,N,x;
    scanf("%d",&T);
    for (int z=1;z<=T;++z)
    {
        int cnt=0;
        scanf("%d",&N);
        for (int i=1;i<=N;++i) { scanf("%d",&x); if (x==i) ++cnt; }
        printf("Case #%d: %.6lf\n",z,(double)(N-cnt));
    }
    return 0;
}
