#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
FILE *fpin=fopen("B-large.in","r");
FILE *fpout=fopen("b.out","w");
int a[30][30];
bool b[30][30];
char s1[40][5];
char s2[40][5];
char s[1000];
void init()
{
     int i,j,n,m,k,l; 
     memset(a,0,sizeof(a));
     memset(b,false,sizeof(b));
     fscanf(fpin,"%d",&n);
     for(i=1;i<=n;i++)
     {
        fscanf(fpin,"%s",s);
        a[s[0]-64][s[1]-64]=s[2];
        a[s[1]-64][s[0]-64]=s[2];
        
     }
     
     fscanf(fpin,"%d",&n);
     for(i=1;i<=n;i++)
     {
        fscanf(fpin,"%s",s);
        b[s[1]-64][s[0]-64]=true;
        b[s[0]-64][s[1]-64]=true;
     }
     fscanf(fpin,"%d",&n);
     fscanf(fpin,"%s",s);
     k=0;
     for(i=0;i<n;i++)
     {
        if(k==0)
         s[k]=s[i],k++;
        else
         {
           if(a[s[k-1]-64][s[i]-64]>0)
             s[k-1]=a[s[k-1]-64][s[i]-64];
           else 
           {
              l=0;
             for(j=0;j<k;j++)
              if(b[s[j]-64][s[i]-64])
               {k=0,l=1;break;}
             if(l==0)
             s[k]=s[i],k++;
           }
         }
     }
     fprintf(fpout,"[");
     for(i=0;i<k-1;i++)
      fprintf(fpout,"%c, ",s[i]);
     if(k>0)
       fprintf(fpout,"%c]\n",s[k-1]);
     else fprintf(fpout,"]\n");
}
int main()
{
    int p,o;
    fscanf(fpin,"%d",&p);
    for(o=1;o<=p;o++)
    {
        fprintf(fpout,"Case #%d: ",o);
        init();
    }
    fclose(fpin);
    fclose(fpout);
}
