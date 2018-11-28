#include <iostream>
using namespace std;
int i,j,z,t;
int main()
{
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&t);
 for (int i=1;i<=t;++i)
 {
  printf("Case #%d: ",i);
  int n,l,h,fr[100];
  cin>>n>>l>>h;
  for (j=0;j<n;++j) cin>>fr[j];
  bool yes1=false;
  for (j=l;j<=h;++j)
  {
   bool yes=true;
   for (z=0;z<n;++z)
    if ((fr[z]%j)!=0 && (j%fr[z])!=0) { yes=false; break; }
   if (yes) { yes1=true; break; }
  }
  if (yes1) cout<<j; else cout<<"NO";
  cout<<endl;
 }
}