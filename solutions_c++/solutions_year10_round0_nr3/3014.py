#include<stdio.h>
#include<conio.h>

int main()
{
    FILE *fin;
    FILE *fout;
    char a[100];
    long int R,K,N,g[1000],h[1000],sum,money;
    int i,T,j,m,t[1000],tmp,flag;  
    gets(a);  
    fin=fopen(a,"r");
    fout=fopen("out.txt","w");
    fscanf(fin,"%d",&T);
    for(i=1;i<=T;i++)
    {
               money=0;      
               fscanf(fin,"%d %d %d",&R,&K,&N);
               for(j=0;j<N;j++)
                  fscanf(fin,"%d",&g[j]);                                 
               for(j=0;j<N;j++)
               {
                  sum=0;
                  m=0;
                  flag=0;
                  while((sum<=K)&&(m<N))
                  {
                     tmp=(j+m)%N;
                     sum+=g[tmp];
                     m++;
                  }
                  if(sum>K)
                  sum-=g[(j+m-1)%N];
                  t[j]=(j+m-1)%N;
                  h[j]=sum;
               }
               m=0;
               for(j=0;j<R;j++)
               {
                   money+=h[m];
                   m=t[m];
               }             
               fprintf(fout,"Case #%d: %d\n",i,money);
    }
    fclose(fin);
    fclose(fout);
}
