#include<stdio.h>
#include<cstring>
#include<algorithm>

using namespace std;

int main()
{
    int cases,ii,n,i,j,r[42],jj;
    char s[42][42];
    bool ud[42];
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%s",&s[i][1]);
            r[i]=0;
            for(j=1;j<=n;j++)if(s[i][j]=='1')r[i]=j;
        }
        memset(ud,0,sizeof(ud));
        int an=0;
        for(i=1;i<=n;i++)
        {
            for(j=i;j<=n;j++)if(r[j]<=i)
            {
                //fprintf(stderr,"i=%d j=%d\n",i,j);
                for(jj=j;jj>i;jj--)
                {
                    swap(r[jj],r[jj-1]);
                    an++;
                }
                break;
            }
        }
        printf("Case #%d: %d\n",ii,an);
    }
    fputs("END",stderr);
    while(1);
    return 0;
}
