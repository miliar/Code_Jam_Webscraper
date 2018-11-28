#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
  freopen("A-small-attempt3.in","r",stdin);

  int i,T, N[10000], K[10000];
  int times;

  cin>>T;
  for (i=0; i<T; i++)
    {
      cin>>N[i]>>K[i];
      
    }

  //cout<<T<<endl;
   for (i=0; i<T; i++)
     {
       //cout<<N[i]<<" - "<<K[i]<<endl;
       if (K[i] == 0)
	 {
	   cout<<"Case #"<<i+1<<": OFF"<<endl;
	   continue;
	 }
       if (N[i] == 1)
	 {
	   if(K[i]%2==0)
	     cout<<"Case #"<<i+1<<": OFF"<<endl;
	   else
	     cout<<"Case #"<<i+1<<": ON"<<endl;
	   continue;
	 }

       

       times = int(K[i] % int(pow(2, N[i])));
       
       //cout<<K[i]<<"-"<<N[i]<<"-"<<times;

       times++;
       
       //cout<<"exp: "<<exponente<<endl;
       
       if (pow(2, N[i]) == times)
	 {
	   cout<<"Case #"<<i+1<<": ON"<<endl;
	 }
       else 
	 {
	   cout<<"Case #"<<i+1<<": OFF"<<endl;
	 }
     }


}
