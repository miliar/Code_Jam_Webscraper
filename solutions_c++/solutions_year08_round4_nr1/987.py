#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#define INF 999999
using namespace std;

FILE *fin=fopen("entrada.in","r");
FILE *fout=fopen("saida.out","w");
 int gate[15000];
 int val[15000];
 int lista[15000];
 int pode [15000];
 int dah[15000][5];
 int melhor;
 int m;
int forca(int pos, int value)
{
    if(dah[pos][value]!=-1)return dah[pos][value];
  
    if(pos>=(m+1)/2)
    {

                    if(value==val[pos])return 0;
      
                    return INF;                
    }
      int mn = INF;
    if(pode [pos]==1)
    {
        if(gate[pos]==0) //fica and   
        {
             if(value==1)               
                 mn=min(mn,forca(2*pos,1)+forca(2*pos+1,1)+1);                       
             else
             {
                 mn=min(mn,forca(2*pos,0)+forca(2*pos+1,1)+1);
                 mn=min(mn,forca(2*pos,1)+forca(2*pos+1,0)+1);
                 mn=min(mn,forca(2*pos,0)+forca(2*pos+1,0)+1);
             }
        }
        else//fica or
        {
            if(value==1)
            {
                 mn=min(mn,forca(2*pos,0)+forca(2*pos+1,1)+1);
                  mn=min(mn,forca(2*pos,1)+forca(2*pos+1,1)+1);
                   mn=min(mn,forca(2*pos,1)+forca(2*pos+1,0)+1);
            }
            else
            {
                 mn=min(mn,forca(2*pos,0)+forca(2*pos+1,0)+1);
            }
        }
    }             
    if(gate[pos]==1) //and   
        {
             if(value==1)               
             mn=min(mn,forca(2*pos,1)+forca(2*pos+1,1));                       
             else
             {
                 mn=min(mn,forca(2*pos,0)+forca(2*pos+1,1));
                 mn=min(mn,forca(2*pos,1)+forca(2*pos+1,0));
                 mn=min(mn,forca(2*pos,0)+forca(2*pos+1,0));
             }
        }
        else//or
        {
            if(value==1)
            {
                 mn=min(mn,forca(2*pos,0)+forca(2*pos+1,1));
                  mn=min(mn,forca(2*pos,1)+forca(2*pos+1,1));
                   mn=min(mn,forca(2*pos,1)+forca(2*pos+1,0));
            }
            else
            {
                 mn=min(mn,forca(2*pos,0)+forca(2*pos+1,0));
            }
        }               
    
    dah[pos][value]=mn;
    return mn;
}
int main ()
{
    int qwe;
    fscanf(fin,"%d",&qwe);
    int v;
    for(int ppp=1;ppp<=qwe;ppp++)
    {  
       fscanf(fin,"%d %d",&m,&v);
       int saida=0;
       int qte=0;
       for(int i=1;i<=(m-1)/2;i++)
       {
               fscanf(fin,"%d %d",&gate[i],&pode[i]);
               
       }
       for(int i=(m+1)/2;i<=m;i++)
       {
               fscanf(fin,"%d",&val[i]);       
       }
       for(int i=1;i<=m;i++)
               dah[i][0]=dah[i][1]=-1;

       saida=forca(1,v);


       if(saida>=INF)fprintf(fout,"Case #%d: IMPOSSIBLE\n",ppp);
       else fprintf(fout,"Case #%d: %d\n",ppp,saida);
       
    }
    fclose(fout);
    printf("Fim");
    scanf(" %*c");
};
