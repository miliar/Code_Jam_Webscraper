#include<iostream>
using namespace std;
int main()
{
    int t,n,k,i,cycle;
    
    FILE *fp1=fopen("A-large.in","r");
    FILE *fp2=fopen("out.txt","w");
    
    fscanf(fp1,"%d",&t);
    for(i=1;i<=t;i++)
    {
       fscanf(fp1,"%d%d",&n,&k);
       cycle=(1<<n);
       fprintf(fp2,"Case #%d: ",i);
       if(!((k+1)%cycle))fprintf(fp2,"ON\n");
       else fprintf(fp2,"OFF\n");
              
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
