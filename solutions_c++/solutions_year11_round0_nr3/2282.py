#include <cstdio>
#include <algorithm>

using namespace std;
int X[2000];
int sum(int p,int q)
{
    int z=0;
    int i;
    for(i=p;i<=q;i++)
        z+=X[i];
    return z;
}

int XOR(int p,int q)
{
    int z=0;
    int i;
    for(i=p;i<=q;i++)
        z^=X[i];
    return z;
}
int main()
{
    int test_num;
    int i,j;
    int A,B;
    int n,t;
    int ok=0;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&test_num);
    for(t=1;t<=test_num;t++)
    {
        ok=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&X[i]);
        }
        sort(X,X+n);
        for(i=0;i<n-1;i++)
        {
            if(XOR(0,i) == XOR(i+1,n-1))
            {
                printf("Case #%d: %d\n",t,sum(i+1,n-1));
                ok=1;
                break;
            }
        }
        if(!ok)
            printf("Case #%d: NO\n",t);
    }
}
