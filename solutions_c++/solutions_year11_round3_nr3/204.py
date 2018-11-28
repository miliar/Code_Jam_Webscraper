#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      int N,L,H,i,j;
      cin>>N>>L>>H;
      int f[110];
      for(i=0;i<N;i++)
	cin>>f[i];
      int out=0;
      for(i=L;i<=H;i++)
	{
	  for(j=0;j<N;j++)
	    if((f[j]%i)&&(i%f[j]))
	      break;
	  if(j==N) {
	    out=i;
	    break;
	  }
	}
      cout<<"Case #"<<t<<": ";
      if(out)
	cout<<out<<"\n";
      else 
	cout<<"NO\n";
    }
  return 0;
}
