#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main ()
{
  int T,a,b,n,x,last;
  cin>>T;
  int count=0;
    
  for(int i=0;i<T;i++)
  {
		cin>>a>>b;
		n=a;
		x=1;
		while(n!=0)
		{
			x*=10;
			n/=10;
		}
		x/=10;
		count=0;
		for(int j=a;j<b;j++)
    {
			n=j;
			last=n%10;
			n=n/10;
			n=last*x+n;
			while(n!=j)
			{
				if(n>j && n<=b)
					count++;
				last=n%10;
				n=n/10;
				n=last*x+n;
			}			
		}
		cout<<"Case #"<<(i+1)<<": "<<count<<endl;
	}  
  return 0;
}
