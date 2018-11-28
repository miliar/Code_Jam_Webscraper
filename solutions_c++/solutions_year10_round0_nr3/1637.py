#include<iostream>
using namespace std;
int main()
{
    int i,j;
    unsigned __int64 t,r,k,n,a[2000],b[2000],c,g[2000],s,sum;
    FILE *fp1=fopen("C-large.in","r");
    FILE *fp2=fopen("out.txt","w");
    
    fscanf(fp1,"%I64u",&t);
    for(i=1;i<=t;i++)
    {
       fscanf(fp1,"%I64u%I64u%I64u",&r,&k,&n);
       fprintf(fp2,"Case #%d: ",i);
       
       for(j=0;j<n;j++)fscanf(fp1,"%I64u",&g[j]);
       
       memset(a,0,sizeof(a));
       for(j=0;j<n;j++)
       {
           c=0;
           while(c<n&&(a[j]+g[(j+c)%n])<=k)
           {
                a[j]+=g[(j+c)%n];
                c++;
           }
           b[j]=(j+c)%n;
       }
       
       s=0;sum=0;
       while(r--)
       {
            sum+=a[s];
            s=b[s];
       }
       
       fprintf(fp2,"%I64u\n",sum);
    }
    fclose(fp1);
    fclose(fp2);
    
    return 0;
}
