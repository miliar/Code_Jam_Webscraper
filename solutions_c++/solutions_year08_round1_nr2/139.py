#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdlib>
using namespace std;
FILE *fin=fopen("entrada.in","r");
FILE *fout=fopen("saida.out","w");

int saida[3006];
int forca[3006];
int caga[3006];
struct consu
{  
    int vet[3006]; 
    int a;
};
consu pessoa[3006];
int main ()
{
    int c;
    fscanf(fin,"%d",&c);
    for(int ppp=1;ppp<=c;ppp++)
    {
        
        int n;
        int t;
        int fudeu=0;
        fscanf(fin,"%d",&n);
        for(int i=1;i<=n;i++)
        {
            saida[i]=0;
            forca[i]=0;
            caga[i]=0;
        }
        fscanf(fin,"%d",&t);
        
        for(int i=0;i<t;i++)
        {
            int aux;
            fscanf(fin,"%d",&aux);
            pessoa[i].a=aux;
            int as,bs;
            for(int j=1;j<=n;j++)
            {
                pessoa[i].vet[j]=0;    
            }
            
            for(int j=0;j<aux;j++)
            {
                
                
                fscanf(fin,"%d %d",&as,&bs);
                if(pessoa[i].vet[as]!=0)caga[i]=1;
                pessoa[i].vet[as]=(bs+1);    
                
            }
            if(aux==1)
            {
                if(bs==1)  
                {
                    saida[as]=1;  
                    forca[i]=1; 
                } 
            }
        }

            for(int i=0;i<t;i++)
            {
                if(caga[i]==1)continue;
                int flag=0;
                for(int j=1;j<=n;j++)
                {
                    if(pessoa[i].vet[j]==1 && saida[j]==0)//un
                    {
                        flag=1;
                        break;
                    }  
                    if(pessoa[i].vet[j]==2 && saida[j]==1)//un
                    {
                        flag=1;
                        break;
                    }  
                }
                if(flag==0)
                {
                    flag=-1;
                    for(int j=1;j<=n;j++)
                    {
                        if(pessoa[i].vet[j]==2)//mat
                        {
                            saida[j]=1;
                            flag=2;
                            break;
                        }  

                    }
                    
                }
                
              //  fprintf(fout,"%d\n",flag);
                if(flag==-1){fudeu=1; break;}
                if(flag==2)i=-1;
            }
        //fprintf(fout,"%d %d\n",pessoa[0].vet[1],saida[1]);
        fprintf(fout,"Case #%d:",ppp);
        if(!fudeu)
        {
            for(int i=1;i<=n;i++)
                fprintf(fout," %d",saida[i]);
            fprintf(fout,"\n"); 
        }   
        else
        {
               fprintf(fout," IMPOSSIBLE\n");
        }
        
    }
    return 0;   
}
