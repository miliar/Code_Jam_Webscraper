//In the name of God
#include <iostream>
#include <algorithm>
using namespace std;

void solve()
{
  int n,s,p;
  cin>>n>>s>>p;
  int normal=0,with=0;
  while(n--)
    {
      int score;
      cin>>score;
      bool n=false,w=false;
      for(int i=0;i<=10;++i)
	for(int j=i;j<=10 and j-i<=2;++j)
	  for(int k=j;k<=10 and k-i<=2;++k)
	      if(i+j+k==score and k>=p)
		if(k-i<2)
		  n=true;
		else
		  w=true;
      if(n)
	normal++;
      else if(w)
	with++;
    }
  cout<<normal+min(with,s)<<endl;
}

int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;++i)
    {
      cout<<"Case #"<<i<<": ";
      solve();
    }
  return 0;
}
