#include <stdio.h>
#include <algorithm>

using namespace std;

int p[10000][2],c[10000];
int n,m,a;
int i,j,ok,T;

int main()
{
        freopen("triang.in","r",stdin);
        freopen("triang.out","w",stdout);

        scanf("%d",&T);

        for (int nrt=1;nrt<=T;nrt++)
                {
                        printf("Case #%d: ",nrt);
                        scanf("%d %d %d",&n,&m,&a);

                        memset(c,0,sizeof(c));
                        for (i=0;i<=n;i++)
                                for (j=0;j<=m;j++)
                                        {
                                                c[i*j]=1;
                                                p[i*j][0]=i;
                                                p[i*j][1]=j;
                                        }

                        ok=0;
                        for (i=0;i<=a;i++)
                                if ( (c[i])&&(c[i+a]) )
                                        {
                                                printf("0 0 %d %d %d %d\n",p[i][0],p[i+a][1],p[i+a][0],p[i][1]);
                                                ok=1;
                                                break;
                                        }
                        if (!ok) printf("IMPOSSIBLE\n");                        
                }
        return 0;
}
