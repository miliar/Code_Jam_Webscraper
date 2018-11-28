#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct
{
       double prob; 
       char propiedad[20]; 
       int si;
       int no; 
} nodo;

char props[1000][20];

nodo nodos[1000];
int nnodos, pro;
char s[1000];
FILE *in;

int read()
{
     double d;
     int pp=0;
     int n = nnodos;
     nnodos++;
     char c = fgetc(in);
     while(c!='(') c = fgetc(in);
     c = fgetc(in);
     while(c==' '||c=='\n') c = fgetc(in);
     while(c!=' '&&c!='\n'&&c!=')'){ s[pp++] = c; c=fgetc(in);}
     s[pp]=0;
         d=atof(s);
     while(c==' '||c=='\n') c = fgetc(in);
         if(c==')')
         {
                            nodos[n].prob = d;
                            nodos[n].propiedad[0]=0;
                           //ES HOJA
         }
         else
         {
                            //NO ES HOJA
                            nodos[n].prob = d;
                            pp=0;
                            while(c!=' '&&c!='\n'&&c!=')'){ s[pp++] = c; c=fgetc(in);}
                            s[pp]=0;
                            strcpy(nodos[n].propiedad,s);
                            nodos[n].si = read();
                            nodos[n].no = read();
                            while(c!=')') c = fgetc(in);
         }
     return n;
}

double solve(int n)
{
       if(nodos[n].propiedad[0]==0) return nodos[n].prob;
       for(int i=0;i<pro;i++)
               if(strcmp(nodos[n].propiedad, props[i])==0)
                                             return nodos[n].prob * solve(nodos[n].si);
       return nodos[n].prob * solve(nodos[n].no);
}

main()
{
      int T,nc=1, lines;
      //in = fopen("a.txt","r");
      //in = fopen("A-small-attempt1.in","r");
      //FILE *out = fopen("A-small.out","w");
      in = fopen("A-large.in","r");
      FILE *out = fopen("A-large.out","w");
      fgets(s,999,in);
      T = atoi(s);
      while(T--)
      {
             fgets(s,999,in);
             lines = atoi(s);
             nnodos=0;
             read();
             /*for(int i=0;i<nnodos;i++)
             {
                     printf("%d %lf -%s- %d %d\n", i, nodos[i].prob, nodos[i].propiedad, nodos[i].si, nodos[i].no);
             }*/
             fscanf(in,"%d",&lines);
             fprintf(out,"Case #%d:\n",nc++);
             for(int i=0;i<lines;i++)
             {
                    fscanf(in,"%s %d",s,&pro);
                    for(int j=0;j<pro;j++)
                    {
                            fscanf(in,"%s",props[j]);
                    }
                    fprintf(out,"%lf\n",solve(0));
             }      
             fprintf(out,"");
      }
      system("PAUSE");
      fclose(out);
      return 0;
}
