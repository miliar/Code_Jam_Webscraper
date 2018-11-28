#include <stdio.h>
#include <string>
#include <string.h>
#include <iostream>
using namespace std;


long t,i,k,l,a,b,T,an,bn,o,cur[10000],w[10000],p[10000],j;
char s[100];
string s1,s2;

void swap(long *x, long *y)
{long c;
 c=*x;
 *x=*y;
 *y=c;
}

main()
{
 freopen("train.in","r",stdin);
 freopen("train.out","w",stdout);
 scanf("%d",&t);
 
 for (j=0; j<t; j++)
 {
  scanf("%d",&T);
  scanf("%d %d\n",&an,&bn);
  for (l=0; l<an; l++)
  {
   gets(s);
   s1=s2=""; s1+=s[0]; s1+=s[1]; s2+=s[3]; s2+=s[4]; sscanf(s1.c_str(),"%d",&a); sscanf(s2.c_str(),"%d",&b);
   o=a*60+b;
   cur[2*l]=o; w[2*l]=0; p[2*l]=0;
   s1=s2=""; s1+=s[6]; s1+=s[7]; s2+=s[9]; s2+=s[10]; sscanf(s1.c_str(),"%d",&a); sscanf(s2.c_str(),"%d",&b);
   o=a*60+b+T;
   cur[2*l+1]=o; w[2*l+1]=0;  p[2*l+1]=1;   
  }
  
  for (l=0; l<bn; l++)
  {
   gets(s);
   s1=s2=""; s1+=s[0]; s1+=s[1]; s2+=s[3]; s2+=s[4];  sscanf(s1.c_str(),"%d",&a); sscanf(s2.c_str(),"%d",&b);
   o=a*60+b;
   cur[2*an+2*l]=o; w[2*an+2*l]=1; p[2*an+2*l]=0;
   s1=s2=""; s1+=s[6]; s1+=s[7]; s2+=s[9]; s2+=s[10]; sscanf(s1.c_str(),"%d",&a); sscanf(s2.c_str(),"%d",&b);
   o=a*60+b+T;
   cur[2*an+2*l+1]=o; w[2*an+2*l+1]=1;  p[2*an+2*l+1]=1;   
  }
  long n=(an+bn)*2;
  for (i=0; i<n; i++)
   for (k=0; k<n-1; k++)
    if (cur[k]>cur[k+1] || (cur[k]==cur[k+1] && p[k]<p[k+1]) )
     { swap(&cur[k],&cur[k+1]); swap(&p[k],&p[k+1]); swap(&w[k],&w[k+1]); }
  
 long ans[2],free[2]; free[0]=free[1]=ans[0]=ans[1]=0; 
 
 for (l=0; l<n; l++)
 {
  if (!p[l])
  {
   if ( free[w[l]] ) free[w[l]]--; else ans[w[l]]++;
  } else
  free[1-w[l]]++;
 }
  printf("Case #%d: %d %d\n",j+1,ans[0],ans[1]);
 }
 
}
