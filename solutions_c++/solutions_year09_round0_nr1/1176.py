#include <stdio.h>
#include <iostream>
#include <string.h>
#define u 6000

using namespace std;

long l,D,N,L,k,j,ans,fix[150];
char s[u][30],s1[u];
bool boo;

main()
{
 freopen("A.in","r",stdin);
 freopen("A.out","w",stdout);
 scanf("%d%d%d\n",&L,&D,&N);
 for (l=0; l<D; l++) gets(s[l]);

 for (long i=1; i<=N; i++)
 {
  gets(s1);
  ans=0;
  for (l=0; l<D; l++)
  {
   memset(fix,0,sizeof(fix));
   boo=true; k=0;
   for (j=0; j<L; j++)
   {
    if (s1[k]=='(')
    while (1)
    {
     k++;
     if (s1[k]==')') { k++; break; }
     fix[ s1[k] ]=j+1;
    }
    else fix[ s1[k++] ]=j+1;
    if (fix[ s[l][j] ]!=j+1) { boo=false; break; }
   }
   if (boo) ans++;
  }
  printf("Case #%d: %d\n",i,ans);
 }
  
}
