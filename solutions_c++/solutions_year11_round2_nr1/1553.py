#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define maxn 200
int T,n;
char mp[maxn][maxn];
double wp[maxn],owp[maxn],oowp[maxn];
double wp_ex[maxn][maxn];
double ans[maxn];
int main()
{
    int i,j;
    int win,cnt,win2;
    double tmp;
    char ch;
    int cs;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    while(scanf("%d",&T)!=EOF)
    {
        cs = 1;
        while(T--){
        scanf("%d",&n);
        scanf("%c",&ch);
        for(i = 0 ; i < n; i++)
        {
            scanf("%s",mp[i]);
        }
        for(i = 0 ; i < n; i++)
        {
            win = 0; cnt = 0; win2 = 0;
            for(j = 0 ; j < n; j++)
            {
                if(mp[i][j]!='.')
                {
                    if(mp[i][j] == '1')
                    {
                        win++;
                    }
                    cnt++;
                }
            }
            wp[i] = win/(double)cnt;
            for(j = 0; j < n ; j++)
            {
                if(mp[i][j]!='.')
                {
                    if(mp[i][j] == '1')
                        wp_ex[i][j] = (win - 1)/(double)(cnt-1);
                    else
                        wp_ex[i][j] = win/(double)(cnt-1);
                }
            }
       //     printf("%lf\n",wp[i]);
        }
      //  for(i = 0 ; i < n; i++)
      //  {
       //     for(j = 0; j < n;j++)
        //    {
        //        printf("%.5lf ",wp_ex[i][j]);
        //    }
           // printf("\n");
        //}
        for(i = 0 ; i < n; i++)
        {
            tmp = 0.0; cnt = 0;
            for(j = 0; j < n; j++)
            {
                if(mp[i][j] != '.')
                {
                    tmp += wp_ex[j][i];
                    cnt++;
                }
            }
            owp[i] = tmp/(double)cnt;
           // printf("%lf\n",owp[i]);
        }
        for(i = 0; i < n; i++)
        {
            tmp = 0.0; cnt = 0;
            for(j = 0 ; j < n; j++)
            {
                if(mp[i][j] != '.')
                {
                    tmp += owp[j];
                    cnt++;
                }
            }
            oowp[i] = tmp/(double)cnt;
        }
        //printf("===============\n");
      //  for(i = 0; i < n; i++)
      //  {
     //       printf("%lf\n",oowp[i]);
     //   }
        for(i = 0 ; i < n ;i++)
        {
            ans[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        }
        printf("Case #%d:\n",cs++);
        for(i = 0 ; i < n ; i++)
        {
            printf("%.12lf\n",ans[i]);
        }
        }
    }
}

