#include <stdio.h>
#include <string>
#include <iostream>
#define MOD 10000
#define u 1000
using namespace std;

long N,p,i,l,n,D[u][u],k;
char s[u];
string S;

main()
{
 freopen("C.in","r",stdin);
 freopen("C.out","w",stdout);
 scanf("%d\n",&N);
 S="welcome to code jam"; p=S.size();
 
 for (i=1; i<=N; i++)
 {
  memset(D,0,sizeof(D));
  gets(s); n=strlen(s);
  if (s[0]=='w') D[0][1]=1; D[0][0]=1;
  for (l=1; l<n; l++)
  {
   for (k=0; k<p; k++)
   {
    D[l][k]+=D[l-1][k]; D[l][k]%=MOD;
    if (D[l-1][k] && s[l]==S[k]) { D[l][k+1]+=D[l-1][k]; D[l][k+1]%=MOD; }
   }  
  }
  long ans=0;
  for (l=0; l<n; l++)
   if (D[l][p]) { ans+=D[l][p]; ans%=MOD; }
  
  printf("Case #%d: %.04d\n",i,ans);
 } 
 
}
