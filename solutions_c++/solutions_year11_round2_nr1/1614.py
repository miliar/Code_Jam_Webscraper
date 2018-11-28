#include<stdio.h>
char a[111][111];
int win[111],num[111];
double wp[111],owp[111],oowp[111],rpi[111];
main()
{
    FILE *fout= fopen("RPI.txt","w");
    int l,t,n,i,j,count;
    double sum;
    char cc;
    scanf("%d",&t);
    for(l=0;l<t;l++)
    {
        scanf("%d\n",&n);
        for(i=0;i<n;i++)
        {
            win[i]=0;
            num[i]=0;
            for(j=0;j<n;j++)
            {
                scanf("%c",&a[i][j]);
                if(a[i][j]=='1') win[i]++;
                if(a[i][j]!='.') num[i]++;
            }
            scanf("%c",&cc);
        }
        for(i=0;i<n;i++)
        {
            wp[i]=(double)win[i]/(double)num[i];
            //printf("%d %lf\n",count,wp[i]);
        }
        //printf("yeah");
        //printf("aaaaa %lf\n",wp[0]);
        //for(i=0;i<n;i++) printf("%lf\n",wp[i]);
        for(i=0;i<n;i++)
        {
            count=0;
            sum=0.0;
            for(j=0;j<n;j++)
            {
                if(a[i][j]!='.')
                {
                    if(a[i][j]=='1')
                    {
                        sum+=(double)win[j]/(double)(num[j]-1);
                    }
                    else if(a[i][j]=='0')
                    {
                        sum+=(double)(win[j]-1)/(double)(num[j]-1);
                    }
                    count++;
                }
            }
            owp[i]=(double)sum/(double)count;
            //printf(" %lf\n",sum,owp[i]);
        }
        for(i=0;i<n;i++)
        {
            count=0;sum=0;
            for(j=0;j<n;j++)
            {
                if(a[i][j]!='.')
                {
                    sum+=owp[j];
                    count++;
                }
            }
            oowp[i]=(double)sum/(double)count;
        }
        for(i=0;i<n;i++)
        {
            rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
        }
        printf("Case #%d:\n",l+1);
        fprintf(fout,"Case #%d:\n",l+1);
        for(i=0;i<n;i++)
        {
            printf("%.10lf\n",rpi[i]);
            fprintf(fout,"%.10lf\n",rpi[i]);
        }
    }
}
