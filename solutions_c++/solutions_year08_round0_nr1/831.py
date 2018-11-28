#include<stdio.h>
#include<conio.h>
#include<string.h>

int main()
{
     char strsev[1001][105],ser[105],query[1001][105];
     int cases,sern,qlen,i,j,serp,iquery[1001],nswt,coun,qi;
     short int flag[1000];
     FILE *fp,*tp;
     
     tp=fopen("output.txt","w");     
     fp=fopen("A-large.in","r");
     fscanf(fp,"%d",&cases);
     fgets(ser,105,fp);
     for(i=0;i<cases;i++)
     {
         fscanf(fp,"%d",&sern);
         fgets(ser,105,fp);
         for(j=0;j<sern;j++)
         {
                            fgets(strsev[j],105,fp);
                            printf("%s",strsev[j]);
         }
         fscanf(fp,"%d",&qlen);
         fgets(ser,105,fp);
         for(j=0;j<qlen;j++)
         {
                            fgets(query[j],105,fp);
                            for(serp=0;serp<sern;serp++)
                            {
                              if(strcmp(query[j],strsev[serp])==0)break;
                            }
                            printf("%d %s",serp,query[j]);
                            iquery[j]=serp;
         }


     for(j=0;j<sern;j++)
     {
                        flag[j]=1;
     }
     
     nswt=0;
     coun=0;
     for(qi=0;qi<qlen;qi++)
     {
     if(flag[iquery[qi]]){coun++;flag[iquery[qi]]=0;}
     if(coun==sern){
                    coun=1;
                    for(j=0;j<sern;j++)
                       {
                         flag[j]=1;
                       }
                    printf("qy %s",query[qi]);
                    flag[iquery[qi]]=0;
                    nswt++;
                    
                    }
     }
    printf("Count #%d:\n",coun);
 //    if(coun!=1&&coun>0)nswt++;
     printf("Case %d: %d\n",i+1,nswt);
     fprintf(tp,"Case #%d: %d\n",i+1,nswt);

     }

getch();
fclose(fp);
fclose(tp);
}     
