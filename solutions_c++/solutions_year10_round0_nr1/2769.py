#include<fstream>
using namespace std;

__int64 T,N,K;
__int64 fn[32];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    scanf("%lld",&T);

    for (int i=1;i<=30;i++)
        fn[i]=(1<<i);

    for (int u=1;u<=T;u++)
    {
        scanf("%lld%lld",&N,&K);
        __int64 ys=K%fn[N];
        printf("Case #%d: ",u);
        if (ys==fn[N]-1)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}
