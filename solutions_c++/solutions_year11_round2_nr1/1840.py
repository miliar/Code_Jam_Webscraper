#include<stdio.h>

int main() {
     int t,n;
     char str[120][120];
     int w[120];
     int l[120];
     double wp[120];
     double owp[120];
     double oowp[120];
     scanf("%d",&t);
     for(int i=0;i<t;i++){
             scanf("%d",&n);
             for(int j=0;j<n;j++){
                     scanf("%s",str[j]);
             }
             for(int j=0;j<n;j++){    
                     w[j]=0;
                     l[j]=0;
                     for(int k=0;k<n;k++){
                             if(str[j][k] == '1') w[j]++;
                             else if(str[j][k] == '0') l[j]++;        
                     }
                     wp[j] = double(w[j])/double(w[j]+l[j]);
             }   
             for(int j=0;j<n;j++){  
                     double sum=0;
                     int count =0;
                     for(int k=0;k<n;k++){
                             if(str[j][k] == '1') {sum+=double(w[k])/double(w[k]+l[k]-1); count++;}
                             else if(str[j][k] == '0') {sum+=double(w[k]-1)/double(w[k]+l[k]-1);  count++;}
                     }
                     owp[j] = sum/double(count);
             }      
             for(int j=0;j<n;j++){  
                     double sum=0;
                     int count =0;
                     for(int k=0;k<n;k++){
                             if(str[j][k] == '1'||str[j][k] == '0') 
                             {sum+=owp[k];  count++;}
                     }
                     oowp[j] = sum/double(count);
             }    
             
             printf("Case #%d:\n",i+1);
             for(int j=0;j<n;j++){  
                     //printf("%lf %lf %lf\n",wp[j],owp[j],oowp[j]);
                     printf("%.12lf\n",.25*wp[j]+.5*owp[j]+.25*oowp[j]);
             }
     }             
}
