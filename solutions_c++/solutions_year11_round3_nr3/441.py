#include <cstdio>
using namespace std;

int T,N,L,H;
int A[101];
int main ()
{
    freopen("in.in","r",stdin);freopen("out.out","w",stdout);
    scanf("%d",&T);
    for (int z=1;z<=T;++z)
    {
        printf("Case #%d: ",z);
        scanf("%d %d %d",&N,&L,&H);
        for (int i=1;i<=N;++i) scanf("%d",&A[i]);
        bool ok;
        for (int i=L;i<=H;++i)
        {
            ok=1;
            for (int j=1;j<=N;++j) if (A[j]%i && i%A[j]) { ok=0; break; }
            if (ok) { printf("%d\n",i); break; }
        }
        if (!ok) printf("NO\n");
    }
    return 0;
}
