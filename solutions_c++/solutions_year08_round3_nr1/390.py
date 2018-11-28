#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include<stack>
#include<memory.h>
#include<queue>
#include<map>
#include<set>
using namespace std;

int main()
{
  freopen("A-large.in","rt",stdin);
  freopen("A-large.out","wt",stdout);
  int N;
  cin>>N;
  long long P,K,L;
  vector<long long> lets;
  for(int i = 0 ; i< N ; i ++)
  {
          cin>>P>>K>>L;
          lets.resize(L);
          for(int j = 0 ; j < L ; j ++)
          cin>>lets[j];
          long long c = 0;
          if(L>(P*K))
          {
                     cout<<"Case #"<<i+1<<": Impossible"<<endl;
                     continue;
          }
          sort(lets.rbegin(),lets.rend());
         // bool flag = 1;
          for(int j = 0 ; j < lets.size() ; j ++)
          {
                  c+=(lets[j])*(long long)((j/K)+1);
          }
          cout<<"Case #"<<i+1<<": "<<c<<endl;
          
  }
  
                                                
  return 0;  
}
