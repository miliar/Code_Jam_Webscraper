#include <iostream>
using namespace std;

int main()
{
  int T,tcase;
  cin>>T;
  for(tcase=1;tcase<=T;tcase++)
    {
      int N,i,j,ans=0,a[1000],b[1000];
      cin>>N;
      for(i=0;i<N;i++)
	{
	  cin>>a[i]>>b[i];
	  for(j=0;j<i;j++)
	    if((a[i]-a[j])*(b[i]-b[j])<0)
	      ans++;
	}
      cout<<"Case #"<<tcase<<": "<<ans<<"\n";
    }
}
