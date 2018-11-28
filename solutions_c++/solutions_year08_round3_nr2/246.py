#include<stdio.h>
#include<algorithm>

using namespace std;

FILE* f, *fo;

int n, i;

char a[40];

int res;

int poz = 0; 

void DFS(long long p, long long t, long long z)
{
 if(a[poz]=='\n')
 {
  if(z==-1)
  {
   p = t;
  }
  else
  if(z==0)
  {
   p+=t;
  }
  else
   p -=t;
  
  if(p<0)
  p*=-1;
  if(p%3==0 || p%5==0 || p%7==0 || p%2==0 || p==0)
   res++;
//  fprintf(fo,"%d ",p);
  return;
 }
 

  poz++;
 DFS(p,t*10+a[poz-1]-'0',z);
 //t/=10;
 
 if(z==-1 && poz==1)
 {poz--;
  return;
}
 
 
 if(z==-1)
 {
  p = t;
 }
 else
 if(z==0)
 {
  p+=t;
 }
 else
  p -=t;
  
 
 
 DFS(p,a[poz-1]-'0',0);
 
 
 DFS(p,a[poz-1]-'0',1);
 
 poz--;
}

int main()
{
 f = fopen("in.txt","r");
 fo = fopen("out.txt","w");
  
 fscanf(f,"%d",&n);
 fgetc(f);
 for(i=1; i<=n; i++)
 {
  res = 0;
  fgets(a,100,f);
  DFS(0,0,-1);
  fprintf(fo,"Case #%d: %d\n",i,res);
 }
 
 
 return 0;
}
