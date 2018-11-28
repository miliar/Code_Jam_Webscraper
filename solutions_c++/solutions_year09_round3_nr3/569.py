#include<iostream.h>
#include<fstream.h>

int lev=-1,n,val[50],a[50],ans,p,q,occ[150],start;

void permu(int k)
{
  int i;
  val[k]=++lev;
  if(lev==n)
  {
    int j,k,bribe=0,release,tmp;
    for(i=0;i<n;i++)
    {
      // a[val[i]] is the person that is released
//      cout<<a[val[i]]<<" ";
      release=a[val[i]];
      occ[release]=0;
      j=release-1;
      tmp=0;
      while(j>=1 && occ[j])
        {  bribe++;  j--;  tmp++;}
//        cout<<" lb: "<<bribe<<"  ";
      j=release+1;
      while(j<=p && occ[j])
        {  bribe++;  j++;  tmp++;}
//        cout<<" hb: "<<bribe<<"  "<<endl;
//      cout<<" tmp : "<<tmp<<"  ";
    }
//    cout<<"  Bribe : "<<bribe<<endl;
    if(start)
    {
      ans=bribe;
      start=0;
    }
    else
    if(bribe<ans)
    ans=bribe;
    for(i=1;i<=p;i++)
    occ[i]=1;

  }
  for(i=0;i<n;i++)
  if(val[i]==0)
  permu(i);
  lev--;
  val[k]=0;
}

int main()
{
//  ifstream ip("ip.txt");
  ifstream ip("ipc.txt");
  ofstream op("op.txt");
  int tests,t,i,j;
  ip>>tests;
  
  for(t=1;t<=tests;t++)
  {
    ip>>p>>q;
    n=q;
    for(i=1;i<=p;i++)
    occ[i]=1;
    for(i=0;i<q;i++)
    {
      val[i]=0;
      j=i+1;
      ip>>a[j];
    }
    start=1;
    permu(0);
//    cout<<"Case #"<<t<<": "<<ans<<endl;
    op<<"Case #"<<t<<": "<<ans<<endl;
  }
  ip.close();
  op.close();
//  getchar();
  return 1;
}
