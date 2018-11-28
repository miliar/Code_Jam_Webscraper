#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>

char s[10000];
char g[10000];
int l,k,br,c,min;
char ch;
int p[10];

void resi(int pos)
{
 if (pos==k)
 {
   int i,j,m;
   m=l/k;
   for (i=0;i<m;i++)
   {
    for (j=1;j<=k;j++)
     g[i*k+j]=s[i*k+p[j]];
   }
   int pom=1;
   for (i=2;i<=l;i++)
    if (g[i]!=g[i-1]) pom++;
   if (pom<min) min=pom; 
 }
 else
 {
  pos++;
  for (int i=1;i<=k;i++)
  {
   bool pom=true; p[pos]=i;
   for (int j=1;j<pos;j++) if (p[j]==p[pos]) pom=false;
   if (pom) resi(pos);
  }   
 }    
}

int main()
{
 freopen("D-small-attempt0.in","r",stdin);
 freopen("zadatak.out","w",stdout);   
 scanf("%d",&c);
 for (br=1;br<=c;br++)
 {
   scanf("%d",&k);
   ch=' ';
   while ((ch<'a')||(ch>'z')) scanf("%c",&ch);
   l=0;
   while ((ch>='a')&&(ch<='z'))
   {
    l++; s[l]=ch;
    scanf("%c",&ch);     
   } 
   min=l+1;
   resi(0);
   printf("Case #%d: ",br);
   printf("%d\n",min);
 }
 return 0;
}
