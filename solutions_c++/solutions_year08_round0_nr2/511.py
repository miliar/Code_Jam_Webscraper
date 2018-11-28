#include<stdio.h>
#include<algorithm>

using namespace std;

FILE* fi,* fo;

int n;

int i, b;

int t;

int na, nb;

int pa[100], da[100], pb[100], db[100];

int p1, p2;

int ret;

int main()
{
 fi = fopen("in.txt","r");
 fo = fopen("out.txt","w");
 
 fscanf(fi,"%d",&n);
 
 for(b=1; b<=n; b++)
 {
  fscanf(fi,"%d%d%d",&t,&na,&nb);
  
  for(i=0; i<na; i++)
  {
   fscanf(fi,"%d:%d",&p1,&p2);
   pa[i] = p1*60+p2;
   fscanf(fi,"%d:%d",&p1,&p2);
   db[i] = p1*60+p2+t;
  }
  
  for(i=0; i<nb; i++)
  {
   fscanf(fi,"%d:%d",&p1,&p2);
   pb[i] = p1*60+p2;
   fscanf(fi,"%d:%d",&p1,&p2);
   da[i] = p1*60+p2+t;
  }
  
  ret = 0;
  
  sort(pa,pa+na);
  sort(da,da+nb);
  
  p1 = 0;
  p2 = 0;
  
  while(p1<na && p2<nb)
  {
   if(pa[p1]<da[p2])
   {
    p1++;
    ret++;
   }
   else
   {
    p1++;
    p2++;
   }
  }
  
  if(p1<na)
   ret += na - p1;
  
  fprintf(fo,"Case #%d: %d",b,ret);
  
  ret = 0;
  
  sort(pb,pb+nb);
  sort(db,db+na);
  
  p1 = 0;
  p2 = 0;
  
  while(p1<nb && p2<na)
  {
   if(pb[p1]<db[p2])
   {
    p1++;
    ret++;
   }
   else
   {
    p1++;
    p2++;
   }
  }
  
  if(p1<nb)
   ret += nb - p1;
  
  fprintf(fo," %d\n",ret);
  
 }
 
 return 0;
}
