#include<stdio.h>
#include<string.h>

int main(){
    int T, map[101][101], n, i, j, k, op[101],win[101],tol[101],cnt;
    char tmp[101][101];
    double owp[101],oowp[101],wp[101],sum;
    scanf("%d",&T);
    cnt = 0;
    while(T--){
        cnt++;
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%s",tmp[i]);
        for(i=0;i<n;i++)
            for(j=0;j<n;j++){
                if(tmp[i][j] == '.') map[i][j] = 2;
                else if(tmp[i][j] == '0') map[i][j] = 0;
                else if(tmp[i][j] == '1') map[i][j] = 1;
            }
        for(i=0;i<n;i++){
            tol[i] = win[i] = 0;
            for(j=0;j<n;j++){
                if(map[i][j] != 2) tol[i]++;
                if(map[i][j] == 1) win[i]++;
            }
            wp[i] = ((double)win[i])/((double)tol[i]);
        }
        for(i=0;i<n;i++){
            sum = 0.0;
            for(j=0;j<n;j++){
                if(map[j][i] == 0) sum+=(((double)win[j])/(tol[j]-1.0));
                else if(map[j][i] == 1) sum+=((win[j]-1.0)/(tol[j]-1.0));
            }
            owp[i] = sum/tol[i];
        }
        for(i=0;i<n;i++){
            sum = 0.0;
            for(j=0;j<n;j++){
                if(map[j][i]!=2) sum += owp[j];
            }
            oowp[i] = sum/tol[i];       
        }
        printf("Case #%d:\n",cnt);
        for(i=0;i<n;i++)
            printf("%lf\n",0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);  
    }

    return 0;
}
