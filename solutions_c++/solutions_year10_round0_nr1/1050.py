#include <iostream>
using namespace std;
int main()
{
    int f[60];
    int n,i,j;
    int a,b;
    bool ok;
    freopen( "C:/Users/FengJinwen/Desktop/A-large.in", "r", stdin );
    freopen( "C:/Users/FengJinwen/Desktop/ans.txt", "w", stdout );
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        memset(f,0,sizeof(f));
        ok=true;
        scanf("%d%d",&a,&b);
        j=0;
        while (b>0)
        {
            f[++j]=b%2;
            b/=2;
        }
        for (j=1;j<=a;j++)
        {
            if (f[j]==0)
            {
                ok=false;
                break;
            }
        }
        if (ok) printf("Case #%d: ON\n",i);
 else printf("Case #%d: OFF\n",i);
    }
}
