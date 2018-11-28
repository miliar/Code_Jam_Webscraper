#include <stdio.h>
#include <iostream>
using namespace std;

long t,o,l,p,best,S[200][100][3],fix[200],per[20],i,n,k,a,b,q,pasuxi[20];

main()
{
 freopen("milkshakes.in","r",stdin);
 freopen("milkshakes.out","w",stdout);
 scanf("%d",&t);
 for (long i=0; i<t; i++)
 {
  memset(S,0,sizeof(S));
  memset(per,0,sizeof(per));
  scanf("%d",&n);  scanf("%d",&p);
  for (l=0; l<p; l++)
  {
   scanf("%d",&o);
   for (k=0; k<o; k++) 
    { scanf("%d%d",&a,&b); a--; S[l][a][b]=1; }
  }
  long ans=2*n;
  per[0]=-1;
  
  while (!per[n])
  {
   memset(fix,0,sizeof(fix));
   per[0]++;
   q=0;   k=0;
   while (per[k]>1) { per[k]=0; per[++k]++; }
   for (l=0; l<n; l++) 
    if (per[l])  q++;
    
   for (l=0; l<p; l++) 
   {
    for (k=0; k<n; k++)
     if (S[l][k][per[k]]) fix[l]=1;
   }
   long boo=1;
   for (l=0; l<p; l++) 
    if (!fix[l]) { boo=0; break; }
   
   if (boo && q<ans) 
    { 
     ans=q; 
     for (l=0; l<n; l++)
      pasuxi[l]=per[l];
    }
  }
  
  cout<<"Case #"<<i+1<<": ";
  if (ans==2*n) cout<<"IMPOSSIBLE"<<endl;
  else
  {
   cout<<pasuxi[0];
   for (l=1; l<n; l++) cout<<" "<<pasuxi[l];
   cout<<endl;
  }
  
  
 }
 
}
 
