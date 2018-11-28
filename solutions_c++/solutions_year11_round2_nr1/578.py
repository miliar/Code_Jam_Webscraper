#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int32_t N=101;
char G[N][N];
int32_t win_num[N];
int32_t play_num[N];
double WP[N];
double OWP[N];
double OOWP[N];
int32_t n;

int32_t main(){
    int32_t cas, ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%d",&n);
        for(int32_t i=0;i<n;i++){
            scanf("%s",G[i]);
        }
        for(int32_t i=0;i<n;i++){
            int32_t num=0;
            int32_t win=0;
            for(int32_t j=0;j<n;j++){
                if(G[i][j]=='1'){
                    num++;
                    win++;
                }else if(G[i][j]=='0'){
                    num++;
                }
            }
            win_num[i]=win;
            play_num[i]=num;
            WP[i]=1.0*win/num;
        }
        for(int32_t i=0;i<n;i++){
            double sum=0.0;
            for(int32_t j=0;j<n;j++){
                if(G[i][j]=='1'){
                    sum+=1.0*win_num[j]/(play_num[j]-1);
                    //if(i==1) printf("1::j=%d,sum=%lf\n",j,sum);
                }else if(G[i][j]=='0'){
                    sum+=1.0*(win_num[j]-1)/(play_num[j]-1);
                    //if(i==1) printf("0::j=%d,sum=%lf\n",j,sum);
                }
            }
            sum/=play_num[i];
            OWP[i]=sum;
        }
        for(int32_t i=0;i<n;i++){
            double sum=0.0;
            for(int32_t j=0;j<n;j++){
                if(G[i][j]!='.'){
                    sum+=OWP[j];
                }
            }
            sum/=play_num[i];
            OOWP[i]=sum;
        }
        printf("Case #%d:\n", ic);
        for(int32_t i=0;i<n;i++){
            //printf("i=%d,wp=%lf,owp=%lf,oowp=%lf,win_num=%d,play_num=%d\n",i,WP[i],OWP[i],OOWP[i],win_num[i],play_num[i]);
            printf("%lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
        }
    }
    return 0;
}
