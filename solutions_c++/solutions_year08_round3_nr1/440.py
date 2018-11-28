#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define ll long long
typedef pair<long long ,long long > pll;
int main()
{
   ll t,c=1;
   cin>>t;
   while(t--)
   {
      ll p,n,i,j,k,l,count=0,f[10000]={0}; 	
      cin>>p>>k>>l;
      vector<long long >freq;
      for(i=0;i<l;i++)
      {
          cin>>j;
          freq.push_back(j);
      }
      sort(freq.begin(),freq.end());
      i=freq.size()-1;
      ll increment=0;
      while(i>=0)
      {
        increment++; 
        for(j=0;j<k;j++)
      	{ 
      	  if(i>=0)
      	  {
      	    f[i]=(freq[i]*increment);
      	    count+=f[i];
//      	    cout<<f[i]<<endl;
      	    i--;
      	  }
      	}
      }	
      cout<<"Case #"<<c++<<": "<<count<<endl;
      
   }
}

