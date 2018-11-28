#include<iostream>
#include<vector>
using namespace std;
int main()
{
  int t,i,j,c;
  unsigned long r,k,n,gi,st,earn,grps;
  vector<unsigned long> g;
  cin>>t;
  for(i=1;i<=t;++i)
    {
      g.clear();
      cin>>r>>k>>n;
      for(j=0;j<n;++j)
	{
	  cin>>gi;
	  g.push_back(gi);
	}
      c=0;
      earn=0;
      for(j=0;j<r;++j)
	{
	  st=0;
	  grps=0;
	  while(st+g[c]<=k && grps<n)
	    {
	      earn+=g[c];
	      st+=g[c];
	      c=(c+1)%n;
	      ++grps;
	    }
	}
      cout<<"Case #"<<i<<": "<<earn<<endl;
    }
  return 0;
}
