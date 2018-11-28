#include<stdio.h>
#include<string.h>

FILE* fi,* fo;

int n;

int ns, q;

int i, b;
char P[100];

char s[100][100];

int t[100], p[100];
int mt, mp = 0;


int main()
{
 fi = fopen("in.txt","r");
 fo = fopen("out.txt","w");
 
 fscanf(fi,"%d",&n);
 
 for(b=1; b<=n; b++)
 {
  fscanf(fi,"%d",&ns);
  fgetc(fi);
  for(i=0; i<ns; i++)
   fgets(s[i],100,fi);
  
  fscanf(fi,"%d",&q);
  fgetc(fi);
  
  mp = 0;
  
  for(i=0; i<ns; i++)
   p[i] = 0;
   
  while(q--)
  {
   fgets(P,100,fi);
   for(i=0; i<ns; i++)
    if(strcmp(s[i],P)==0)
     t[i] = -1;
    else
    {
     if(p[i]==-1)
      t[i] = p[mp]+1;
     else
      t[i] = p[i]>p[mp]+1?p[mp]+1:p[i];
     
     if(mt == -1 || t[mt]>t[i])
      mt = i;
    }
    
   mp = mt;
   mt = -1;
   for(i=0; i<ns; i++)
    p[i] = t[i];
  }
  
  fprintf(fo,"Case #%d: %d\n",b,p[mp]);
 }
 
 return 0;
}
