#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
#define mp make_pair 
#define pb push_back 
FILE *fin=fopen("entrada.in","r");
FILE *fout=fopen("saida.out","w");


int main ()
{
    int n,a,b,t;
    fscanf(fin,"%d",&n);
    vector < int > saia;//horario que sai de a 
    vector < int > saib;
    vector < int > chea;//chega em a
    vector < int > cheb;
    for(int qw=1;qw<=n;qw++)
    {
        fscanf(fin,"%d",&t);
       fscanf(fin,"%d %d ",&a,&b);
       saia.resize(0);
       saib.resize(0);
       chea.resize(0);
       cheb.resize(0);
       int sa=0,sb=0;
       for(int i=0;i<a;i++)
       {
            char x1,x2,x3,x4,x5;
            int t1,t2;
            fscanf(fin,"%c%c%c%c%c ",&x1,&x2,&x3,&x4,&x5); 
            //fprintf(fout,"%c%c%c%c%c   
            t1=(10*(x1-'0')+x2-'0')*60 + 10*(x4-'0')+x5-'0';
            fscanf(fin,"%c%c%c%c%c ",&x1,&x2,&x3,&x4,&x5);    
            t2=t+(10*(x1-'0')+x2-'0')*60 + 10*(x4-'0')+x5-'0';
            
            saia.pb(t1);
            cheb.pb(t2);
            //fprintf(fout,"%d %d\n",t1,t2);
       }
       for(int i=0;i<b;i++)
       {
            char x1,x2,x3,x4,x5;
            int t1,t2;
            fscanf(fin,"%c%c%c%c%c ",&x1,&x2,&x3,&x4,&x5);    
            t1=(10*(x1-'0')+x2-'0')*60 + 10*(x4-'0')+x5-'0';
            fscanf(fin,"%c%c%c%c%c ",&x1,&x2,&x3,&x4,&x5);    
            t2=t+(10*(x1-'0')+x2-'0')*60 + 10*(x4-'0')+x5-'0';
            saib.pb(t1);
            chea.pb(t2);
           // fprintf(fout,"%d %d\n",t1,t2);
       }
       int tema=0;
       int temb=0;
       
       for(int tempo=-1;tempo<=24*60;tempo++)
       {
            for(int i=0;i<cheb.size();i++)
            {
                if(cheb[i]==tempo)
                {
                    temb++;   
                }
            }
            for(int i=0;i<chea.size();i++)
            {
                if(chea[i]==tempo)
                {
                    tema++;   
                }
            }     
            for(int i=0;i<saia.size();i++)
            {
                if(saia[i]==tempo)
                {
                    if(tema==0)sa++;
                    else tema--;   
                }
            }
            for(int i=0;i<saib.size();i++)
            {
                if(saib[i]==tempo)
                {
                    if(temb==0)sb++;
                    else temb--;   
                }
            }
            
       }
       fprintf(fout,"Case #%d: %d %d\n",qw,sa,sb);
    }
    
    return 0;   
}
