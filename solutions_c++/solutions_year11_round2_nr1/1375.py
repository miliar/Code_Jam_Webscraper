#include <stdio.h>
#include <string.h>
struct{
    int num;
    int win;
} p[110];
char s[110][110];
double ans[110][4];

int main()
{
    int cas,n;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%s",s[i]);
        for(int i=0;i<n;i++)
        {
            int num=0;
            int win=0;
            ans[i][0]=0;
            for(int j=0;j<n;j++)
             if (s[i][j]!='.')
             {
                 num++;
                 if (s[i][j]=='1') win++;
             }
            if (num)
                ans[i][0]=win*1.0/(num*1.0);
            p[i].num=num;
            p[i].win=win;
        }
        for(int i=0;i<n;i++)
        {
            ans[i][1]=0;
            for(int j=0;j<n;j++)
             if (s[i][j]!='.')
             {
                 int t=p[j].num-1;
                 int q=p[j].win;
                 if (s[i][j]=='0') q--;
                 if (t) ans[i][1]+=q*1.0/(t*1.0);
             }
            if (p[i].num) ans[i][1]/=(p[i].num*1.0);
        }
        for(int i=0;i<n;i++)
        {
            ans[i][2]=0;
            for(int j=0;j<n;j++)
             if (s[i][j]!='.') ans[i][2]+=ans[j][1];
            if (p[i].num) ans[i][2]/=(p[i].num*1.0);
        }
        printf("Case #%d:\n",ll);
        for(int i=0;i<n;i++)
        {
            //printf("(%.3f %.3f %.3f)\n",ans[i][0],ans[i][1],ans[i][2]);
            printf("%.8f\n",0.25*ans[i][0]+0.5*ans[i][1]+0.25*ans[i][2]);
        }
    }
    return 0;
}

