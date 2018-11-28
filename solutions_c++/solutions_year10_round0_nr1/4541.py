#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
int main()
{
    FILE *archivo,*in;
    archivo=fopen("snaper.txt","w");
    
    int t=0,n=0,k=0,vec[30],index=0,suma=0;
       scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d%d",&n,&k);      
        for(int i=0;i<n;i++)
          vec[i]=0;
          suma=0;
        for(int j=0;j<k;j++)
        {
                     index=0;
                     while(index<n)
                     {
                        if(vec[index]==0)
                        {
                           vec[index]=1;
                           suma++;
                           break;                 
                        }    
                        else
                        {
                            vec[index]=0;
                            suma--;
                            index++;
                        }          
                     }
        }
      
        if(suma==n)
        fprintf(archivo,"Case #%d: ON\n",i+1);
        else
        fprintf(archivo,"Case #%d: OFF\n",i+1);
    }
    

    return 0;
}
