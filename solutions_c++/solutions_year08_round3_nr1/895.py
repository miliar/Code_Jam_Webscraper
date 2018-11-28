#include<stdio.h>
#include<conio.h>


int main()
{
     long int i,j,n,p,k,l,prob[1005],flag=1,temp,ans;
    FILE *fp,*tp;
    fp=fopen("input.in","r");
    tp=fopen("out.txt","w");
    fscanf(fp,"%ld",&n);
    for(i=0;i<n;i++)
    {
    fscanf(fp,"%ld%ld%ld",&p,&k,&l);
    for(j=0;j<l;j++)
    {
    fscanf(fp,"%ld",&prob[j]);
    }
    flag=1;
    
    while(flag)
    {
    flag=0;
    for(j=0;j<l-1;j++)
    {
    if(prob[j]<prob[j+1]){temp=prob[j];prob[j]=prob[j+1];prob[j+1]=temp;flag=1;}
    }        
    }
   // sort(prob,prob+n);
    
    for(j=0;j<l;j++)
    {
    printf("%ld\n",prob[j]);
    }
    ans=0;
    for(j=0;j<l;j++)
    {
    ans=ans+prob[j]*(j/k+1);
    printf("int %ld",prob[j]*(j/k+1));
    }
    

    printf("Case #%ld: %ld\n",i,ans);
    fprintf(tp,"Case #%ld: %ld\n",i+1,ans);

}
getch();
}
