#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
char s[100][100];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        int r,c,d;
        scanf("%d%d%d",&r,&c,&d);
        for (int i=0;i<r;i++)
            scanf("%s",s[i]);
        int anss=-1;
        for (int i=min(r,c);i>=3&&anss==-1;i--)
        {
            for (int j=0;j<=r-i;j++)
                for (int k=0;k<=c-i;k++)
                {
                    double sumx=0,sumy=0,cntx=0,cnty=0;
                    for (int l=j;l<j+i;l++)
                        for (int m=k;m<k+i;m++)
                        {
                            if (l==j&&m==k) continue;
                            if (l==j&&m==k+i-1) continue;
                            if (l==j+i-1&&m==k) continue;
                            if (l==j+i-1&&m==k+i-1) continue;
                            cntx+=s[l][m]-'0'+d;
                            sumx+=l*(s[l][m]-'0'+d);
                            cnty+=s[l][m]-'0'+d;
                            sumy+=m*(s[l][m]-'0'+d);
                        }
                    double ansx=sumx/cntx;
                    double ansy=sumy/cnty;
                    double mbx=j+0.5*(i-1);
                    double mby=k+0.5*(i-1);
                    if (fabs(ansx-mbx)<1e-8&&fabs(ansy-mby)<1e-8)
                    {
                        anss=i;
                    }
                }
        }

        printf("Case #%d: ",ii);
        if (anss==-1) puts("IMPOSSIBLE");
        else printf("%d\n",anss);
    }
    return 0;
}
