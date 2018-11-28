#include <stdio.h>
#include <string.h>

long i,t,l,n,ind,o,k,m[1002][1002],j;
char ss[2000],s[201][2000];

main()
{
 freopen("universe.in","r",stdin);
 freopen("universe.out","w",stdout);
 scanf("%d",&t);

 for (i=0; i<t; i++)
 {
  scanf("%d\n",&n);
  for (l=0; l<n; l++) gets(s[l]);
  scanf("%d\n",&o);
  
  for (l=0; l<=o; l++)
   for (k=0; k<=n; k++) m[l][k]=1000000000;
   
  gets(ss);
  for (k=0; k<n; k++) 
    if (!strcmp(ss,s[k])) { ind=k; break; }  
    
  for (l=0; l<=n; l++) m[0][l]=0; m[0][ind]=1000000000;
    
  for (l=1; l<o; l++)
  {
   gets(ss);
   for (k=0; k<n; k++) 
    if (!strcmp(ss,s[k])) { ind=k; break; }
   
   for (k=0; k<n; k++)
    for (j=0; j<n; j++)
     if (j!=ind)
      if ( m[l-1][k]+ (k!=j) < m[l][j]) m[l][j]=m[l-1][k]+(k!=j);
  }
  long ans=1000000000;
  if (o==0) ans=0;
  for (l=0; l<n; l++)
   if (ans>m[o-1][l]) ans=m[o-1][l];
  printf("Case #"); printf("%d",i+1); printf(": ");  printf("%d\n",ans);
 }
 
}

