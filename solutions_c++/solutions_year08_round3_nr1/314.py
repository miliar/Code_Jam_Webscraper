#include<stdio.h>
#include<algorithm>

using namespace std;

FILE* f, *fo;

int n;

 int i = 0, j= 0, p= 0;
long long res;
int  k, l;
unsigned int a[1000];//, poz[1000];


int main()
{
 f = fopen("in.txt","r");
 fo = fopen("out.txt","w");
 
 fscanf(f,"%d",&n);
 
 for(i=1; i<=n; i++)
 {
  fscanf(f,"%d%d%d",&p,&k,&l);
  
  
  for(j=0; j<l; j++)
  {
   fscanf(f,"%u",&a[j]);
   //poz[j] = j;
  }
  if(p*k<l)
  {
   fprintf(fo,"Case #%d: Impossible\n",i);
   continue;
  }
  
  sort(a,a+l);
  reverse(a,a+l);
  res = 0;
  p = 0;
  
  for(j=0; j<l; j++)
  {
   if(j%k==0)
    p++;
   
   res += a[j]*p;
  }
  
  fprintf(fo,"Case #%d: %lld\n",i,res); 
 }
 
 
 
 
 
 
 return 0;
}
