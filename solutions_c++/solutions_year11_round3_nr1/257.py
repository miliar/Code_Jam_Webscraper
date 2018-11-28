#include <iostream>
using namespace std;
int i,j,z,t,r,c;
char f[50][50];
int main()
{
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&t);
 for (int i=1;i<=t;++i)
 {
  printf("Case #%d:\n",i);
  cin>>r>>c; bool yes=true;
  for (j=0;j<r;++j)
   for (z=0;z<c;++z) cin>>f[j][z];
  for (j=0;j<r && yes;++j)
   for (z=0;z<c;++z) 
    if (f[j][z]=='#')
     if (z<c-1 && j<r-1 && f[j][z+1]=='#' && f[j+1][z]=='#' && f[j+1][z+1]=='#')
     {
      f[j][z]=f[j+1][z+1]='/';
      f[j+1][z]=f[j][z+1]='\\';
     }
     else
     {
      yes=false;
      break;
     }
  if (!yes) cout<<"Impossible\n"; else
   for (j=0;j<r;++j,cout<<endl)
    for (z=0;z<c;++z) cout<<f[j][z];
 }
}