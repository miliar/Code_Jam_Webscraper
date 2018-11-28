#include <iostream>

#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <sstream>
#include <cstdlib>


using namespace std;


int freq[10000];

// int all_primes[100000000];


int GCD(int a, int b)
{
  while(b != 0)
  {
    int t= b;
    
    b = a %b;
    
    a = t;  
  }
  return a;
}



int main()
{
  int T;
  
  cin>>T;
  
  vector<string> res_list;
  
  
  for(int t = 0 ;t < T; ++t)
  {
    int N,L,H;
    
    std::cin>>N>>L>>H;
    
    for(int n = 0 ; n < N; ++n)
    {
      cin>>freq[n];
    }
    
    bool nosol = true;
    
    for( int i = L ; i <= H; ++i)
    {
      bool is_possible = true;
      
      for(int n = 0 ; n < N; ++n)
      {
        if((i > freq[n] && i %freq[n] != 0)||
           (i <= freq[n] && freq[n]%i != 0))
        {
          is_possible = false;
          break;
        }          
      }
      
      if( is_possible)
      {
        stringstream ss;
        ss<<i;
        res_list.push_back(ss.str());
        nosol = false;
        break;
      }
    }
    
    if(nosol)
    {
      res_list.push_back("NO");
    }   
    
  }
  
  for( int  t = 0 ; t < res_list.size() ; ++t)
    cout<<"Case #"<<t+1<<": " <<res_list[t]<<endl;    
}