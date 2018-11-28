/*

*/
#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
double wp[110],owp[110],oowp[110];
int Case,n,win[110],comp[110];
char g[110][110];
void display()
{
    scanf("%d",&Case);
    for (int ca=1;ca<=Case;ca++) {
        printf("Case #%d:\n",ca);
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
            scanf("%s",g[i]+1);
        memset(comp,0,sizeof(comp));
        memset(win,0,sizeof(win));
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=n;j++) {
                if (g[i][j]=='.') continue;
                comp[i]++;
                if (g[i][j]=='1') win[i]++;
            }
            wp[i]=double(win[i])/double(comp[i]);
        }
        for (int i=1;i<=n;i++) {
            owp[i]=0;
            for (int j=1;j<=n;j++)
                if (g[i][j]!='.') {
                    owp[i]+=double(g[j][i]=='1'?win[j]-1:win[j])/double(comp[j]-1);
                }
            owp[i]/=double(comp[i]);
        }
        for (int i=1;i<=n;i++) {
            oowp[i]=0;
            for (int j=1;j<=n;j++)
                if (g[i][j]!='.') {
                    oowp[i]+=owp[j];   
                }
            oowp[i]/=double(comp[i]);
        }
        for (int i=1;i<=n;i++)
            printf("%.6f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
}
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    display();
    return 0;
}

