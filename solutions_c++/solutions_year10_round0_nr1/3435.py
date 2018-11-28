#include<iostream>
#include<cmath>

using namespace std;

void main()
{
  unsigned long int N,K,T;
  double div;
  int dev,dev2;

  cin>>T;
  for(int i=0;i<T;i++)
  {
     cin>>N>>K;
	 if(K==0)
		 cout<<"Case #"<<i+1<<": OFF"<<endl;
	 else
	 {
		 if(int(pow(2,N)-1)==K)
		 {
			 cout<<"Case #"<<i+1<<": ON"<<endl;
		 }
		 else
		 {
			 div = (K+1.0)/pow(2,N);
			 dev = int((K+1)/pow(2,N));
			 dev2 = int(ceil(div));
			if(dev==dev2)
			 cout<<"Case #"<<i+1<<": ON"<<endl;
			else
		     cout<<"Case #"<<i+1<<": OFF"<<endl;
		 }  
	 }
  }

  
}