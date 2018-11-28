#include<stdio.h>
#include<math.h>


int main()
{
    FILE *fin;
    FILE *fout;
    char a[100];
    int N,T,i;
    long int K,tmp;
    gets(a);
    fin=fopen(a,"r");
    fout=fopen("out.txt","w");
    fscanf(fin,"%d",&T);
    for(i=1;i<=T;i++)
    {
           fscanf(fin,"%d %d",&N,&K);
           tmp=(int)pow(2,N);
           K=K%tmp;
           if(K+1==tmp)
               fprintf(fout,"Case #%d: ON\n",i);
           else
               fprintf(fout,"Case #%d: OFF\n",i);                    
    }
    fclose(fin);
    fclose(fout);
}
