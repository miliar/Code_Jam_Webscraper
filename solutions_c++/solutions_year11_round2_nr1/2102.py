#include<stdio.h>

int main(){
    int cs;
    scanf("%d",&cs);
    for(int ct=1;ct<=cs;ct++){
        int n;
        scanf("%d",&n);getchar();
        char mat[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                scanf("%c",&mat[i][j]);
            }
            getchar();
        }
        double wp[n],owp[n][n],owp1[n],oowp[n];
        
        for(int i=0;i<n;i++){
            double na=0,nb=0;
            for(int j=0;j<n;j++){
                if(mat[i][j]=='.')continue;
                if(mat[i][j]=='1')na++;
                nb++;
            }
            wp[i]=na/nb;
            //printf("wp[%d]=%lf\n",i,wp[i]);
        }
        
        for(int i=0;i<n;i++){
            
            for(int j=0;j<n;j++){
                double na=0,nb=0;
                for(int k=0;k<n;k++){
                    if(i==k)continue;
                    if(mat[j][k]=='.')continue;
                    if(mat[j][k]=='1')na++;
                    nb++;
                }
                owp[j][i]=na/nb;
            }
        }
        
        for(int i=0;i<n;i++){
            double na=0,nb=0;
            for(int j=0;j<n;j++){
                if(mat[i][j]=='.')continue;
                na+=owp[j][i];
                nb++;
            }
            owp1[i]=na/nb;
            //printf("owp[%d]=%lf\n",i,owp1[i]);
        }
        
        for(int i=0;i<n;i++){
            double na=0,nb=0;
            for(int j=0;j<n;j++){
                if(mat[i][j]=='.')continue;
                na+=owp1[j];
                nb++;
            }
            oowp[i]=na/nb;
            //printf("oowp[%d]=%lf\n",i,oowp[i]);
        }
        //RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        printf("Case #%d:\n",ct);
        for(int i=0;i<n;i++){
            printf("%.12lf\n",0.25*wp[i]+0.5*owp1[i]+0.25*oowp[i]);
        }
    }
    return 0;
}
