#include <stdio.h>
#include <string.h>

int mp[30][30],op[30][30];
int qu[200];

int tr(char x)
{
    return x-'A'+1;
}
char s[200];
int c,d,n;

int main()
{
    int cas;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d",&c);
        memset(mp,0,sizeof(mp));
        while(c--)
        {
            scanf("%s",s);
            mp[tr(s[0])][tr(s[1])]=tr(s[2]);
            mp[tr(s[1])][tr(s[0])]=tr(s[2]);
        }
        scanf("%d",&d);
        memset(op,0,sizeof(op));
        while(d--)
        {
            scanf("%s",s);
            op[tr(s[0])][tr(s[1])]=1;
            op[tr(s[1])][tr(s[0])]=1;
        }
        scanf("%d",&n);
        scanf("%s",s);
        int top=-1;
        for(int i=0;i<n;i++)
        {
            qu[++top]=tr(s[i]);
            while(top>0&&mp[qu[top]][qu[top-1]])
            {
                qu[top-1]=mp[qu[top]][qu[top-1]];
                top--;
            }
            if (top)
            {
                for(int i=0;i<top;i++)
                 if(op[qu[i]][qu[top]])
                 {
                     top=-1;
                     break;
                 }
            }
        }
        printf("Case #%d: [",ll);
        for(int i=0;i<=top;i++)
        {
            printf("%c",qu[i]+'A'-1);
            if(i!=top) printf(", ");
        }
        printf("]\n");
    }
    return 0;
}
