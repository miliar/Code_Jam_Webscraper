#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
FILE *fin=fopen("entrada.in","r");
FILE *fout=fopen("saida.out","w");

char nomes[305][500];
int dp[2050][305];
int lista[2050];
int main ()
{
    int n,s,q;
    fscanf(fin,"%d",&n);
    for(int qw=1;qw<=n;qw++)
    {
       fscanf(fin,"%d ",&s);
       char ent[500];
        for(int i=0;i<s;i++)
        {
             fgets(nomes[i],500,fin);
           //  nomes[i][strlen(nomes[i])-1]=0;
            //printf("%s",nomes[i]);
        }
        fscanf(fin,"%d ",&q);
        //printf("%d\n",q);
        for(int i=1;i<=q;i++)
        {
            fgets(ent,500,fin);
           //ent[strlen(ent)-1]=0;
            //fprintf(fout,"%s ",ent);
            int flag=1;
            for(int j=0;j<s;j++)  if(strcmp(ent,nomes[j])==0){lista[i]=j;}
            
        }    
       // printf("%d\n",q);
        for(int i=0;i<s;i++)
            dp[q][i]=0;
        dp[q][lista[q]]=1;
        int menor=0;
        for(int i=q-1;i>0;i--)
        {
            for(int j=0;j<s;j++)
                if(j!=lista[i])dp[i][j]=dp[i+1][j]; 
                else 
                {
                    int men=99999;
                    for(int k=0;k<s;k++)
                    {
                        if(k==j)continue;
                        if(dp[i+1][k]<men)men=dp[i+1][k];
                     }
                    dp[i][j]=men+1; 
                }
            menor=99999;
             for(int j=0;j<s;j++)if(dp[i][j]<menor)menor=dp[i][j];
            
        }
       /*
        for(int i=q;i>0;i--)
        {
             for(int j=0;j<s;j++)
                fprintf(fout,"%d ",dp[i][j]);
              fprintf(fout,"\n");  
        }*/
        fprintf(fout,"Case #%d: %d\n",qw,menor);
    }
    
    return 0;   
}
