//kunal10
//Prob1
#include<stdio.h>
#include<algorithm>
using namespace std;
int main ()
{
    int i,j,k,t,n,count,temp1,temp2;
    float rpi[101],wp[101],owp[101],oowp[101];
    char s[101][101];
    int gw[101];
    int gp[101];
    scanf("%d",&t);
    j=1;

    while(j<=t){

        scanf("%d",&n);

        for(i=0;i<n;i++){
            gw[i]=0;gp[i]=0;
            scanf("%s",&s[i]);
            for(k=0;k<n;k++){
                if(s[i][k]=='.'){continue;}
                if(s[i][k]=='1'){
                    gw[i]++;
                }
                gp[i]++;
            }
            //printf("%d %d\n",gw[i],gp[i]);
        }

        for(i=0;i<n;i++){
            wp[i] =(float) gw[i]/ (float)gp[i];
            owp[i]=0;count=0;
            for(k=0;k<n;k++){

                if(s[i][k]=='.'){temp2=0;}
                else if (s[i][k]=='0'){temp1 = gw[k]-1;temp2=gp[k]-1;count++;}
                else{temp1 = gw[k];temp2=gp[k]-1;count++;}

                if (temp2!=0){owp[i] = owp[i] + (float) temp1/ (float) temp2;}
            }
            //printf("\n\n\n\n");
            //printf("\n%f %d\n",owp[i],count);
            if (count!=0){owp[i] = owp[i] / count;}
        }

        for (i=0;i<n;i++){
            count = 0;oowp[i]=0;
            for(k=0;k<n;k++)
            {
                if(s[i][k]=='.'){continue;}
                count++;
                oowp[i] = oowp[i]+ owp[k];
            }
            if (count!=0){oowp[i] = oowp[i] / count;}
            rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        }


        printf("Case #%d:\n",j);
        for(i=0;i<n;i++)
        {
            printf("%f\n",rpi[i]);
        }

        j++;
    }
    return 0;

}
