#include <iostream>

#include <algorithm>
#include <vector> 

int main()
{
  int T,N;
  
  std::cin>>T;
  
  std::vector<int> res_list;
  
  for(;T > 0; T--)
  { 
    std::cin>>N;
    
    std::vector<int> C(N);
    
    int total_xor_sum = 0;
    
    int total_sum     = 0;
    
    for(int i = 0; i < N; ++i)
    {
      std::cin>>C[i];
      
      total_xor_sum ^= C[i];
      total_sum     += C[i];
    }
    
   
    if(total_xor_sum == 0)
      res_list.push_back(total_sum - *std::min_element(C.begin(),C.end()));
    else
      res_list.push_back(-1);   

  }
  
  for(int i =0; i< res_list.size(); ++i)
  {
    if(res_list[i] >= 0)
      std::cout<<"Case #"<<i+1<<": "<<res_list[i]<<std::endl;
    else
      std::cout<<"Case #"<<i+1<<": NO"<<std::endl;      
  }
}