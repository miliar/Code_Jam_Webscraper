#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int num;
  cin>>num;
  int* times=new int[num];
  for(int i=0;i<num;i++)
    {
      int n;
      cin>>n;
      int s;
      cin>>s;
      int p;
      cin>>p;
      vector<int> vec;
      times[i]=0;
      int k=0;
      for(int j=0;j<n;j++)
	{
	  int x;
	  cin>>x;
	    if(x>=3*p-2)
	      times[i]++;
	    else if(x>=p)
	      {
		vec.push_back(x);
	      }
	}
      
      for(int j=0;j<vec.size()&&k<s;j++)
	{
	  if( vec[j]>=3*p-4)
	    {  
	      times[i]++;
	      k++;
	    }
	}

   
     


    }


  for(int i=0;i<num;i++)
    cout<<"Case #"<<i+1<<": "<<times[i]<<endl;



  return 0;

}
