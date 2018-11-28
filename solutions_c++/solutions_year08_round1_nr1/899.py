#include<stdio.h>
#include<conio.h>

int main()
{
    int t,n,x[1000],y[1000],fx[1000],fy[1000],i,j,min,max,u,rem;
    FILE *fp,*tp;
    long int sum=0;
    
    fp=fopen("A-small-attempt0(2).in","r");
    tp=fopen("output.txt","w");
    fscanf(fp,"%d",&t);
    for(i=0;i<t;i++)
    {
    fscanf(fp,"%d",&n);
    for(j=0;j<n;j++)fscanf(fp,"%d",&x[j]);
    for(j=0;j<n;j++)fscanf(fp,"%d",&y[j]);
    sum=0;
    for(j=0;j<n;j++){fx[j]=1;fy[j]=1;}

    for(j=0;j<n;j++){
                     
    //find min    
    min=100003;
    for(u=0;u<n;u++)
    {
    if(x[u]<min&&fx[u]){min=x[u];rem=u;}
    }
    printf("%d %d\n",min,rem);    
    fx[rem]=0;
    //find max
    max=-100001;
    for(u=0;u<n;u++)
    {
    if(y[u]>max&&fy[u]){max=y[u];rem=u;}
    }
    fy[rem]=0;
    printf("%d %d\n",max,rem);    
    sum=sum+min*max;    
    }

    printf("Case #%d: %d\n",i+1,sum);
    fprintf(tp,"Case #%d: %d\n",i+1,sum);
     }
 getch();              
fclose(fp);
fclose(tp);
}
