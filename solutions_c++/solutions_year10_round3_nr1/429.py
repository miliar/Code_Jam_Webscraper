#include<iostream>
#include <ext/hash_map>
int pa[2000],pb[2000];
using namespace std;
int main()
{
    FILE * fin=fopen("c:/in.txt","r");
    FILE * fout=fopen("c:/out.txt","w");
    int t;
    fscanf(fin,"%d",&t);
    for(int a=1;a<=t;a++)
    {
       int n;
       fscanf(fin,"%d",&n);
       for(int b=0;b<n;b++)
       {
               fscanf(fin,"%d%d",pa+b,pb+b);
       }
       int cc=0;
       for(int i=0;i<n;i++)
       {
               for(int j=i+1;j<n;j++)
               {
                       if((pa[i]-pa[j])*(pb[i]-pb[j])>=0)
                           continue;
                       cc++;
               }
       }
       fprintf(fout,"Case #%d: %d\n",a,cc);
}
 fclose(fout);
 fclose(fin);  
}
