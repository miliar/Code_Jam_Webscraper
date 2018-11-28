#include<stdlib.h>
#include<stdio.h>

int main()
{
    int T,N;
    freopen("A-large.in","r",stdin);
    freopen("large-attempt.out","w",stdout);
    scanf("%d",&T);
    //printf("%d",T);
    for(int i=0;i<T;i++)
    {
            scanf("%d",&N);
            //printf("%d",N);
            char a[100][100];
            for(int j=0;j<N;j++)
            {
                   scanf("%s",a[j]);
            }
            double RPI,wp[100],owp[100],oowp[100];
            int total[100];
            for(int j=0;j<N;j++)
            {
                    total[j]=0;
                    wp[j]=0.0;
                    owp[j]=0.0;
                    oowp[j]=0.0;
                    for(int k=0;k<N;k++)
                    {
                            if(a[j][k]=='.')
                                            continue;
                            else
                            {
                                total[j]++;
                                wp[j]+=a[j][k]-'0';                                                                                                                                                                                                                               
                            }
                               
                    }
                 //   printf("%f\n",wp[j]);
                    wp[j]=wp[j];
            }
            for(int j=0;j<N;j++)
            {
                    for(int k=0;k<N;k++)
                    {
                            if(a[j][k]=='.')
                                            continue;
                            else
                                owp[j]+=(wp[k]-(a[k][j]-'0'))/(total[k]-1.0);
                    }
                    owp[j]=owp[j]/total[j];
            }
            for(int j=0;j<N;j++)
            {
                    for(int k=0;k<N;k++) 
                    {
                            if(a[j][k]=='.')
                                            continue;
                            else
                                oowp[j]+=owp[k];        
                    } 
                    oowp[j]=oowp[j]/total[j];   
                    wp[j]=wp[j]/total[j];  
            }
            
            printf("Case #%d:\n",i+1);
            for(int j=0;j<N;j++)
            {
                    RPI=wp[j]*0.25+owp[j]*0.5+oowp[j]*0.25;
                   // printf("%lf %lf %lf\n",wp[j],owp[j],oowp[j]);      
                    printf("%.10lf\n",RPI); 
            }
    }
            //system("pause"); 
}
