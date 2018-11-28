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

   long long v1[1050];
   long long v2[1050];
int main ()
{
   int t;
   int n;

   long long saida;
   fscanf(fin,"%d",&t);
   for(int ppp=0;ppp<t;ppp++)
   {
        saida=0;
        fscanf(fin,"%d",&n);
        for(int i=0;i<n;i++)
            fscanf(fin,"%I64d ",&v1[i]);
            
        for(int i=0;i<n;i++)
        {
            fscanf(fin,"%I64d ",&v2[i]);   
            //fprintf(fout,"%d\n",v2[i]);
        }
       sort(v2,v2+n);
        sort(v1,v1+n);
        
        reverse(v1,v1+n);
        
        for(int i=0;i<n;i++)
        {
            saida+=v1[i]*v2[i];
            //fprintf(fout,"%I64d %I64d\n",v1[i],v2[i]);
        }   
        fprintf(fout,"Case #%d: %I64d\n",ppp+1,saida);
    }
    return 0;   
}
