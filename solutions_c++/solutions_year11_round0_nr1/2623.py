#include <iostream>

#include <algorithm>
#include <vector> 


using namespace std;

int main()
{
  int T,N;
  
  std::cin>>T;
  
  std::vector<int> res_list;
  
  for(;T > 0; T--)
  { 
    std::cin>>N;
    
    std::vector<char> R(N);
    std::vector<int>  P(N);    
    
    for(int i = 0; i < N; ++i)
    {      
      std::cin>>R[i];
      std::cin>>P[i];      
    }
    
    int O_pos = 1;
    int B_pos = 1;
    
    int O_gain = 0;
    int B_gain = 0;
    
    int total_moves = 0;
    
    for(int i = 0; i < N; ++i)
    {      
      if (R[i] == 'O')
      {
        int num_moves = max((abs(O_pos-P[i]) - O_gain),0)+1;
        
        O_gain  = 0;        
        B_gain += num_moves;
        
        total_moves += num_moves;
        
        O_pos = P[i];
      }
      else
      {        
        int num_moves = max((abs(B_pos-P[i]) - B_gain),0)+1;
        
        B_gain  = 0;        
        O_gain += num_moves;
        
        total_moves += num_moves;
        
        B_pos = P[i];        
      }
    }
    
    res_list.push_back(total_moves);
  }
  
  for(int i =0; i< res_list.size(); ++i)
  {
    std::cout<<"Case #"<<i+1<<": "<<res_list[i]<<std::endl;
  }
}