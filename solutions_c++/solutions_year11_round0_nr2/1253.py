#include <iostream>
#include <cstring>
using namespace std;

char co[300][300];
bool op[300][300];
char f[1000];
int n,m;

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&m);
        memset(co,0,sizeof(co));
        memset(op,0,sizeof(op));
        for (int i=1;i<=m;i++)
        {
            getchar();
            char c1,c2,c3;
            c1=getchar();
            c2=getchar();
            c3=getchar();
            co[c1][c2]=c3;
            co[c2][c1]=c3;
        }
        scanf("%d",&m);
        for (int i=1;i<=m;i++)
        {
            getchar();
            char c1,c2;
            c1=getchar(); c2=getchar();
            op[c1][c2]=1; op[c2][c1]=1;
        }
        scanf("%d",&n); getchar();
        int size=0;
        for (int i=1;i<=n;i++)
        {
            char ch=getchar();
            f[++size]=ch;
            while (size>1&&co[f[size-1]][f[size]]) f[--size]=co[f[size]][f[size+1]];
            for (int i=1;i<size;i++)
                if (op[f[i]][f[size]])
                {
                   size=0;
                   break;
                }
        }
        printf("Case #%d: [",cas);
        for (int i=1;i<size;i++) printf("%c, ",f[i]);
        if (size) printf("%c",f[size]);
        printf("]\n");
    }
    return 0;
}
        
