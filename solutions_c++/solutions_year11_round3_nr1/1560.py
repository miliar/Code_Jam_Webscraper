#include "cstdio"

using namespace std;

int main(void)
{
    int t,a,b,i,j,k;
    char pict[100][100];
    bool able;

    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%d%d\n",&a,&b);
        for(i=0;i<a;i++)scanf("%s",pict[i]);

        printf("Case #%d:\n",j);
        able=true;

        for(i=0;i<a;i++)
        {
            for(k=0;k<b;k++)
            {
                if(pict[i][k]=='#')
                {
                    pict[i][k]='/';
                    if(pict[i][k+1]=='#')pict[i][k+1]='\\';
                    else
                    {
                        able=false;
                        break;
                    }
                    if(pict[i+1][k]=='#')pict[i+1][k]='\\';
                    else
                    {
                        able=false;
                        break;
                    }
                    if(pict[i+1][k+1]=='#')pict[i+1][k+1]='/';
                    else
                    {
                        able=false;
                        break;
                    }
                }
            }
        }

        if(able)
        {
            for(i=0;i<a;i++)printf("%s\n",pict[i]);
        }
        else printf("Impossible\n");
    }
    
    return 0;
}
