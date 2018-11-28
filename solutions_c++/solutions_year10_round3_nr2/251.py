#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
  int noCase,cases;
  cin>>cases;
  for(noCase=1;noCase<=cases;noCase++)
    {
      int l,p,c;
      double temp,fact;
      cin>>l>>p>>c;
      fact=log(c);
      temp=ceil((double)p/l);
      temp=ceil(log(temp) /fact);
      cout<<"Case #"<<noCase<<": "<<ceil(log(temp)/log(2))<<endl;
    }
  
}
