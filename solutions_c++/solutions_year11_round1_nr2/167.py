#include <stdio.h>
#include <string.h>
char s[1000][20];
char way[1000][100];
int score[10000],can[10000],use[1000];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;i++)
            scanf("%s",s[i]);
        for (int i=0;i<m;i++)
            scanf("%s",way[i]);
        printf("Case #%d:",ii);
        for (int i=0;i<m;i++)
        {
            memset(score,0,sizeof(score));
            for (int j=0;j<n;j++)
            {
                memset(can,-1,sizeof(can));
                memset(use,0,sizeof(use));
                int len=strlen(s[j]);
                for (int k=0;k<26;k++)
                {
                    bool find=false;
                    for (int l=0;l<n;l++)
                    {
                        if (!can[l]) continue;
                        int len2=strlen(s[l]);
                        if (len!=len2)
                        {
                            can[l]=0;
                            continue;
                        }
                        /*for (int m=0;m<len;m++)
                        {
                            if (use[m]&&s[j][m]!=s[l][m])
                            {
                                can[l]=0;
                                break;
                            }
                        }*/
                        if (can[l]==0) continue;
                        for (int m=0;m<len;m++)
                        {
                            if (s[l][m]==way[i][k])
                            {
                                find=true;
                                break;
                            }
                        }
                        if (find) break;
                    }
                    if (!find) continue;
                    find=false;
                    for (int l=0;l<len;l++)
                    {
                        if (s[j][l]==way[i][k])
                        {
                            use[l]=1;
                            find=true;
                        }
                    }
                    if (!find) score[j]++;
                    if (find)
                    {
                        for (int l=0;l<n;l++)
                        {
                            if (!can[l]) continue;
                            for (int m=0;m<len;m++)
                            {
                                if (s[l][m]==way[i][k]&&!use[m]) can[l]=0;
                                if (s[l][m]!=s[j][m]&&use[m]) can[l]=0;
                            }
                        }
                    }
                    else
                    {
                        for (int l=0;l<n;l++)
                        {
                            if (!can[l]) continue;
                            for (int m=0;m<len;m++)
                            {
                                if (s[l][m]==way[i][k]) can[l]=0;
                            }
                        }
                    }
                }
            }
            int maxx=score[0];
            int flag=0;
            for (int i=1;i<n;i++)
            {
                if (score[i]>maxx)
                {
                    maxx=score[i];
                    flag=i;
                }
            }
            printf(" %s",s[flag]);
        }
        printf("\n");
    }
    return 0;
}
