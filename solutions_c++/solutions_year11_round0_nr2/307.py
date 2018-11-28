#include <cstdio>
#include <cmath>
#include <queue>
using namespace std;
int c,d,n;
char C[50][5];
char D[50][5];
char ch[105];
char ans[105];
int len;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int ca;
    scanf("%d",&ca);
    for(int pp=1; pp<=ca; pp++)
    {
        len=0;
        scanf("%d",&c);
        for(int i=0; i<c; i++)
        {
            scanf(" %s",C[i]);
        }
        scanf("%d",&d);
        for(int i=0; i<d; ++i)
            scanf(" %s",D[i]);
        scanf("%d %s",&n,ch);
        for(int i=0; i<n; i++)
        {
            ans[len]=ch[i];
            bool fg=1;
            bool f=1;
            while(fg)
            {
                fg=0;
                if(len>0)
                {
                    for(int j=0; j<c&&!fg; j++)
                    {
                        if(ans[len]==C[j][0]&&ans[len-1]==C[j][1])
                            ans[len-1]=C[j][2],fg=1,f=0,len--;
                        else if(ans[len]==C[j][1]&&ans[len-1]==C[j][0])
                            ans[len-1]=C[j][2],fg=1,f=0,len--;
                    }
                    for(int j=0; j<d&&!fg; j++)
                    {
                        for(int k=0; k<len; k++)
                        {
                            if(ans[k]==D[j][0]&&ans[len]==D[j][1])
                                len=-1,f=0;
                            else if(ans[k]==D[j][1]&&ans[len]==D[j][0])
                                len=-1,f=0;
                        }
                    }
                }
            }
            len++;
        }
        printf("Case #%d: ",pp);
        printf("[");
        for(int i=0; i<len; i++)
        {
            if(i) printf(", ");
            printf("%c",ans[i]);
        }
        puts("]");
    }
    return 0;
}
