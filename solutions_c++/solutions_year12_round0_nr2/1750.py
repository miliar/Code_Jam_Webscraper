#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int t,n,s,p,a[101],i,count,tempt,max;
    FILE *fp1,*fp2;
    if((fp1=fopen("B-large.in","r"))==NULL)exit(0);
    if((fp2=fopen("B-large.out","w"))==NULL)exit(0);
    fscanf(fp1,"%d",&t);
    for(count=1;count<=t;count++)
    {
         fscanf(fp1,"%d %d %d",&n,&s,&p);
         max=0;
         for(i=0;i<n;i++)    
         {
              fscanf(fp1,"%d",&a[i]);               
              tempt=a[i]/3;
              if(a[i]==0){if(p==0)max++;}              
              else if(a[i]%3==0)
              {
                   if(p==tempt+1){if((s--)>0)max++;}
                   else if(p<tempt+1)max++;
              }
              else if(a[i]%3==1)
              {
                   
                   if(p<=tempt+1)max++;
              }
              else
              {
                  if(p==tempt+2){if((s--)>0)max++;}
                  else if(p<tempt+2)max++;
              }                 
         }
         fprintf(fp2,"Case #%d: %d\n",count,max);                        
    }
    fclose(fp2);
    fclose(fp1);
    return 0;
}
