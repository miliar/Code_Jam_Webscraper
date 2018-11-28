#include <iostream>
using namespace std;

int main()
{
  int C,tc;
  cin>>C;
  for(tc=1;tc<=C;tc++)
    {
      cout<<"Case #"<<tc<<": ";
      int N,K,T,i,j,ans=0;
      long long int B;
      long long int x[50];
      int v[50],a[50];
      cin>>N>>K>>B>>T;
      for(i=0;i<N;i++)
	cin>>x[i];
      for(i=0;i<N;i++)
	{
	  cin>>v[i];
	  a[i]=0;
	  if(v[i]*T >= B-x[i])
	   a[i]=1;
	}
      for(i=N-1,j=0;i>=0&&j<K;i--)
	if(a[i])
	  ans+=(N-1-(j++)-i);
      if(j<K)
	cout<<"IMPOSSIBLE\n";
      else
	cout<<ans<<"\n";
    }
}
