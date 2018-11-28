#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int test;
    int cas=0;
    scanf("%d",&test);
    while(test--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",++cas);
        int t=(1<<n);
        if(k<t-1) printf("OFF\n");
        else if((k-t+1)%t!=0) printf("OFF\n");
        else printf("ON\n");
    }
    return 0;
}
