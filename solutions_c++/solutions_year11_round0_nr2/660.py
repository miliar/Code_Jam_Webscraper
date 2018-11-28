#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int s[20000],a1[30][30],a2[30][30];

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int ca=0,t,i,op1,op2,now,pre,f,r,n,j;
    char c1,c2,c3,cc;
    scanf("%d",&t);
    while(t--)
    {
        ++ca;
        memset(a1,0,sizeof(a1));
        memset(a2,0,sizeof(a2));
        scanf("%d",&op1);
        for(i=1;i<=op1;i++)
        {
            scanf(" %c%c%c",&c1,&c2,&c3);
            a1[c1-'A'+1][c2-'A'+1]=c3-'A'+1;
            a1[c2-'A'+1][c1-'A'+1]=c3-'A'+1;
        }
        scanf("%d",&op2);
        for(i=1;i<=op2;i++)
        {
            scanf(" %c%c",&c1,&c2);
            a2[c1-'A'+1][c2-'A'+1]=1;
            a2[c2-'A'+1][c1-'A'+1]=1;
        }
        scanf("%d",&n); getchar();
        f=0; r=0;
        for(i=1;i<=n;i++)
        {
            scanf("%c",&cc);
            now=cc-'A'+1;
            if(f==r&&r==0) { s[++r]=now; f++; continue;}
            s[++r]=now;
            pre=s[r-1];
            if(a1[pre][now])
            {
     //           printf("*********\n");
                s[r-1]=a1[pre][now];
                r=r-1;
            }
            else
            {
                for(j=f;j<r;j++)
                {
                    pre=s[j];
                    if(a2[now][pre])
                    {
                        f=0; r=0;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: ",ca);
        if(f==0&&r==0)
        {
            printf("[]\n");
            continue;
        }
        printf("[");
        for(i=f;i<r;i++)
            printf("%c, ",s[i]-1+'A');
        printf("%c]\n",s[i]-1+'A');
    }
    return 0;
}