#include <iostream>
#include <fstream>

using namespace std;

ifstream iff;
ofstream of;

int main()
{
    iff.open("c.in");
    of.open("c.out");
    int t;
    iff>>t;
    for(int j=0; j<t; j++)
    {
      int n;
      iff>>n;
      int a;
      iff>>a;
      int k =a;
      int ans =  a;
      int sum =a;
      for(int i=1; i<n; i++)
      {
	iff>>a;
	sum +=a;
	if(ans > a)ans = a;
	k = k^a;
      }
      
      if(k == 0)of<<"Case #"<<j+1<<": "<<sum-ans<<endl;
      else of<<"Case #"<<j+1<<": "<<"NO"<<endl;
    }
    return 0;
}