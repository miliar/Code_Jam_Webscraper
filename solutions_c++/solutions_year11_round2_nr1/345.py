#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
using namespace std;
char map[120][120];
int game[120];
double WP[120];
double OWP[120];
double OOWP[120];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,n;
    scanf("%d",&cas);
    for(int ca=1;ca<=cas;ca++){
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%s",&map[i]);
        for(int i=0;i<n;i++){
            int t = 0,tt=0;
            for(int j=0;j<n;j++){
                if(map[i][j]=='1'){
                    tt++;
                    t++;
                }else if(map[i][j]=='0'){
                    t++;
                }
            }
            game[i]=t;
            WP[i]=tt*1.0/(t*1.0);
        }
        for(int i=0;i<n;i++){
            int t=0;
            double sum=0;
            for(int j=0;j<n;j++){
                if(map[i][j]=='1'){
                    sum+=(WP[j]*game[j])/(game[j]-1);
                    t++;
                }else if(map[i][j]=='0'){
                    sum+=(WP[j]*game[j]-1)/(game[j]-1);
                    t++;
                }
            }
            OWP[i]=sum/(t*1.0);
        }
        for(int i=0;i<n;i++){
            int t=0;
            double sum=0;
            for(int j=0;j<n;j++){
                if(map[i][j]!='.'){
                    sum+=OWP[j];
                    t++;
                }
            }
            OOWP[i]=sum/(t*1.0);
        }
        printf("Case #%d:\n",ca);
        for(int i=0;i<n;i++){
            double ans=0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
            printf("%0.12lf\n",ans);
        }
    }
    return 0;
}
