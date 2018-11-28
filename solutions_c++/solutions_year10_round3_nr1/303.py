#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
  int noCase,cases;
  cin>>cases;
  for(noCase=1;noCase<=cases;noCase++)
    {
      int n;
      int wire[1001][2];
      cin>>n;
      for(int i=0;i<n;i++)
	cin>>wire[i][0]>>wire[i][1];
      long long int ans=0;
      for(int i=0;i<n;i++)
	{
	  for(int j=i+1;j<n;j++)
	    {
	      if((wire[i][0]-wire[j][0])*(wire[i][1]-wire[j][1]) < 0)
		ans++;
	    }
	}
      
      
      
      
      cout<<"Case #"<<noCase<<": "<<ans<<endl;
    }
  
}
