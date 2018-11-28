#include <stdio.h>
#include <string.h>
char ts[200],s[200],ss[200];
int g[100][100],g2[100][100];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int iii=1; iii<=t; iii++)
    {
        memset(g,0,sizeof(g));
        memset(g2,0,sizeof(g2));
        int c,d,n;
        scanf("%d",&c);
        for (int i=0; i<c; i++)
        {
            scanf("%s",s);
            g[s[0]-'A'][s[1]-'A']=s[2]-'A';
            g[s[1]-'A'][s[0]-'A']=s[2]-'A';
        }
        scanf("%d",&d);
        for (int i=0; i<d; i++)
        {
            scanf("%s",s);
            g2[s[0]-'A'][s[1]-'A']=1;
            g2[s[1]-'A'][s[0]-'A']=1;
        }
        scanf("%d",&n);
        scanf("%s",ss);
        int len=0;
        for (int ii=0; ii<n; ii++)
        {
            bool change=false;
            s[len++]=ss[ii];
            s[len]=0;
            int i=len-1;
            if (g[s[i]-'A'][s[i-1]-'A']!=0)
            {
                change=true;
                for (int j=0; j<i-1; j++)
                    ts[j]=s[j];
                int cnt=i-1;
                ts[cnt]=g[s[i]-'A'][s[i-1]-'A']+'A';
                cnt++;
                ts[cnt]=0;
            }
            else
            {
                change=false;
                for (int j=0; j<i; j++)
                    if (g2[s[i]-'A'][s[j]-'A']==1)
                    {
                        change=true;
                        int cnt=0;
                        ts[cnt]=0;
                        break;
                    }
            }
            if (change)
            {
                len=strlen(ts);
                strcpy(s,ts);
            }
        }
        printf("Case #%d: [",iii);
        for (int i=0; i<len-1; i++)
            printf("%c, ",s[i]);
        if (len>0) printf("%c",s[len-1]);
        printf("]\n");
    }
    return 0;
}
