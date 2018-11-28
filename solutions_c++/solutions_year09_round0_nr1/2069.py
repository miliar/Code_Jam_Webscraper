#include<stdio.h>
#include<string.h>
int ans;
char s[10010];
char a[5010][20];
int main()
{
    int l,d,n;
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    scanf("%d%d%d",&l,&d,&n);
    for (int i=1;i<=d;i++)
        scanf("%s",a[i]);
    for (int i=1;i<=n;i++)
    {
        scanf("%s",s);
        ans=0;
        for (int j=1;j<=d;j++)
        {
            int k,t;
            bool ok=true;
            for (k=0,t=0;t<l;t++,k++)
                if (s[k]=='(')
                {
                    bool match=false;
                    for(k++;s[k]!=')';k++)
                        if (s[k]==a[j][t])
                            match=true;
                    if (!match) {ok=false;break;}
                }
                else
                {
                    if (s[k]!=a[j][t]) {ok=false;break;}
                }
            if (ok) ans++;
        }
        printf("Case #%d: %d\n",i,ans);
    }
}