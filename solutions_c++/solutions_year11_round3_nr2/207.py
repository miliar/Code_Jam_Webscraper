#include<algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int a[1000010];
long long d[1000010];
int main()
{
  int T;
  cin>>T;
  for(int x=1;x<=T;x++)
    {
      int L,N,C,i,j;
      long long t,out;
      cin>>L>>t>>N>>C;
      t/=2;
      for(i=0;i<C;i++)
	cin>>a[i];
      d[0]=j=0;
      for(i=1;i<=N;i++)
	{
	  d[i]=d[i-1]+a[j++];
	  //	  cout<<d[i]<<"\n";
	  if(j==C)
	    j=0;
	}
      for(i=0;i<=N;i++)
	if(d[i]>t)
	  break;
      //      cout<<t<<"\n";
      if(i>N)
	out=d[N]*2;
      else if(L>=N+1-i)
	out=t+d[N];
      else{
	out=t*2;
	vector <int> v;
	v.push_back(d[i]-t);
	for(;i<N;i++)
	  v.push_back(d[i+1]-d[i]);
	//	cout<<v.size();
	sort(v.begin(),v.end());
	for(i=v.size()-1;i>=0;i--)
	  {
	    //  cout<<v[i]<<"\n";
	    out+=v[i];
	    if(i<v.size()-L)
	      out+=v[i];
	  }
      }
      cout<<"Case #"<<x<<": "<<out<<"\n";
    }
  return 0;
}
