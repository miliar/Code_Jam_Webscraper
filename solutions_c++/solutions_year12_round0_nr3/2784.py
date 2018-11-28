#include <iostream>
#include <cstring>
#include <map>

using namespace std;

int main()
{
  int t,a,b;
  cin>>t;
  for(int k=1;k<=t;++k)
    {
      cin>>a>>b;
      int temp=a,length=0,mPower10=1;
      while(temp!=0)
	{
	  length++;
	  mPower10*=10;
	  temp/=10;
	}
      int result=0;
      for(int j=a;j<=b;++j)
	{
	  int power10=10;
	  map <int,int> rMap;
	for(int i=1;i<length;++i)
	  {
	    int t1=j%power10;
	    if(t1>=power10/10)
	      {
		int t2=j/power10;
		int t3=t2+t1*(mPower10/power10);
		if(t3>j && t3<=b && rMap.find(t3)==rMap.end()){result++;rMap[t3]=1;}
	      }
	    power10*=10;
	  }
      }
      cout<<"Case #"<<k<<": "<<result<<endl;
    }
}
