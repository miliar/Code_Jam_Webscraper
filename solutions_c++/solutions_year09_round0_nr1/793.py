#include <stdio.h>
#include <memory.h>
int l,d,n;
char ch[1000];
int v[50][300];
char st[5100][20];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d%d%d",&l,&d,&n);
    for (int i=0;i<d;i++)
    {
        scanf("%s",&st[i]);
    }
    memset(v,-1,sizeof(v));
    for (int i=0;i<n;i++)
    {
        printf("Case #%d: ",i+1);
        scanf("%s",ch);
        int k=0;
        for (int j=0;j<l;j++)
        {
            if (ch[k]!='(') v[j][ch[k]]=i,k++;
            else
            {
                k++;
                while (ch[k]!=')')
                {
                    v[j][ch[k]]=i;
                    k++;
                }
                k++;
            }
        }
        int ans=0;
        for (int j=0;j<d;j++)
        {
            for (k=0;k<l;k++)
                if (v[k][st[j][k]]!=i) break;
            if (k==l) ans++;
        }
        printf("%d\n",ans);
    }

}
