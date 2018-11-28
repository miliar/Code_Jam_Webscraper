#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    int i,j,k,temp,count,win;
    char match[120][120]={0};
    
    int t,n;
    double rpi[120];
    FILE* fin = fopen("A-large.in","r");
    FILE* fout=fopen("A-large.out","w");
    
    
    fscanf(fin,"%d",&t);
    
    for (i=1;i<=t;++i){
        int nmatch[120]={0};
        double wp[120]={0},owp[120]={0},oowp[120]={0};
        
        fscanf(fin,"%d",&n);
        for (j=0;j<=n-1;++j){
            fscanf(fin,"%s",match[j]);
        }
        
        for (j=0;j<=n-1;++j){
            nmatch[j]=0;
            win=0;
            for (k=0;k<=n-1;++k){
                if (match[j][k]=='1'){
                   nmatch[j]++;
                   win++;
                }
                if (match[j][k]=='0') nmatch[j]++;
            }
            wp[j] = (double)win/nmatch[j];
        }
        
        for (j=0;j<=n-1;++j){
            for (k=0;k<=n-1;++k){
                if (match[j][k]=='1'){
                   owp[j] += wp[k]*(double)nmatch[k]/((nmatch[k]-1)*nmatch[j]);
                }
                if (match[j][k]=='0'){
                   owp[j] += (wp[k] - (double)1.0/nmatch[k])*(double)nmatch[k]/((nmatch[k]-1)*(double)nmatch[j]);
                }
            }
        }
        
        for (j=0;j<=n-1;++j){
            for (k=0;k<=n-1;++k){
                if (match[j][k]=='1' || match[j][k]=='0'){
                   oowp[j] += owp[k]/nmatch[j];
                }
            }
        }
        
        for (j=0;j<=n-1;++j){
            rpi[j] = 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j];
        }
        
        fprintf(fout,"Case #%d:\n",i);
        for (j=0;j<=n-1;++j){
            //printf("%c, nmatch=%d, wp=%lf, owp=%lf, oowp=%lf, rpi=%lf\n",j+'A',nmatch[j],wp[j],owp[j],oowp[j],rpi[j]);
            fprintf(fout,"%.12lf\n",rpi[j]);
        
        }
        
    }
    
   // system("PAUSE");
    return 0;
}
                
