#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

double WP[111], OWP[111], OOWP[111];
char map[111][111];

int main(){
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        
        for(int i=0;i<n;i++){
            scanf("%s",map[i]);
        }
        
        for(int i=0;i<n;i++){
            double all=0, t=0;
            for(int j=0;j<n;j++){
                if(map[i][j] != '.')all++;
                if(map[i][j] == '1')t++;
            }
            WP[i] = t/all;
        }
        
        for(int i=0;i<n;i++){
            double ans=0, avg=0;
            
            for(int j=0;j<n;j++){
                if(map[i][j]=='.')continue;
                
                double all=0, t=0;
                for(int k=0;k<n;k++){
                    if(k==i)continue;
                    if(map[j][k]!='.')all++;
                    if(map[j][k]=='1')t++;
                }
                ans += t/all;
                avg++;
            }
            OWP[i] = ans/avg;
        }
        
        for(int i=0;i<n;i++){
            double ans=0, t=0;
            for(int j=0;j<n;j++){
                if(map[i][j]=='.')continue;
                t++;
                ans+=OWP[j];
            }
            OOWP[i] = ans/t;
        }
        
        printf("Case #%d:\n",cas++);
        for(int i=0;i<n;i++){
            printf("%lf\n",0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
        }
    }
    return 0;
}

