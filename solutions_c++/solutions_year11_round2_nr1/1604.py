#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
double wp[110],owp[110],oowp[110];
int win[110],lose[110];
char bisai[110][110];
int T,n,k,i,j;

int main()
{
        freopen("data.in","r",stdin);
        freopen("data.out","w+",stdout);
        scanf("%d",&T);getchar();
        for(k=1;k<=T;k++) {
            scanf("%d",&n);getchar();
            memset(lose,0,sizeof(lose));
            memset(win,0,sizeof(win));
            memset(wp,0,sizeof(wp));
            memset(owp,0,sizeof(owp));
            memset(oowp,0,sizeof(oowp));
            for(i=1;i<=n;i++) {
                for(j=1;j<=n;j++) {
                    scanf("%c",&bisai[i][j]);
                    if (bisai[i][j]=='0') {
                        lose[i]++;
                    }
                    if (bisai[i][j]=='1') {
                        win[i]++;
                    }
                }
                getchar();
                wp[i]=(double)win[i]/((double)(lose[i]+win[i]));
                //printf("wp %f\n",wp[i]);
            }
            for(i=1;i<=n;i++) {
                for(j=1;j<=n;j++) {
                    if (bisai[i][j]=='1') {

                            owp[i]+=(double)(win[j])/((double)(lose[j]+win[j]-1));
                    }
                    if (bisai[i][j]=='0') {

                        owp[i]+=(double)(win[j]-1)/((double)(lose[j]+win[j]-1));
                    }
                }
                owp[i]/=(double)(lose[i]+win[i]);
                //printf("owp %f\n",owp[i]);
            }
            for(i=1;i<=n;i++) {
                for(j=1;j<=n;j++) {
                    if (bisai[i][j]!='.') {
                        oowp[i]+=owp[j];
                    }
                }
                oowp[i]/=(double)(lose[i]+win[i]);
                //printf("oowp %f\n",oowp[i]);
            }
            printf("Case #%d:\n",k);
            for(i=1;i<=n;i++) {
                printf("%f\n",(double)(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]) );
            }
        }

        return 0;
}
