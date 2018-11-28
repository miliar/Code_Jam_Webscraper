#include <iostream>

#include <algorithm>
#include <vector> 
#include <string>
#include <set>

using namespace std;

int main()
{
  int T,C,D,N;
  
  cin>>T;
  
  vector<string> res_list;
  
  for(;T > 0; T--)
  { 
    cin>>C;
    
    vector<string> combines(C);   
    
    for(int i = 0; i < C; ++i)
      cin>>combines[i];
    
    cin>>D;
    
    vector<string> opposes(D);   
    
    for(int i = 0; i < D; ++i)
      cin>>opposes[i];
    
    cin>>N;
    
    string elements;
    
    cin>>elements;
    
    vector<char>    elem_list;
    multiset<char>  elem_set;
    
    for(int i = 0 ; i < elements.size(); ++i)
    {      
      char e = elements[i];
      
      bool is_combined = false;
      
      if(elem_list.size() > 0 )
      {
        char f = elem_list[elem_list.size()-1];
        
        for(int j = 0; j < C; ++j)
        {
          if(((combines[j][0]) == f && (combines[j][1] == e))||
             ((combines[j][0]) == e && (combines[j][1] == f)))
          {
            elem_list[elem_list.size()-1] = combines[j][2];
            
            elem_set.erase(elem_set.find(f));
            
            is_combined = true;
            
            break;
          }
        }
      }      
    
      if( is_combined == false)
      {
        elem_list.push_back(e);
        elem_set.insert(e);
        
        for(int j = 0; j < D; ++j)
        {
          if((elem_set.count(opposes[j][0]) != 0) &&
             (elem_set.count(opposes[j][1]) != 0))
          {
            elem_list.clear();
            elem_set.clear();
          }
        }
      }    
    }
    
    res_list.push_back(string(elem_list.begin(),elem_list.end()));
  }
  
  for(int i =0; i< res_list.size(); ++i)
  {
    string res = res_list[i];
    
    cout<<"Case #"<<i+1<<": [" ;        
   
    for(int j = 0 ; j < (((int)res.size())-1); ++j)
      cout<<res[j]<<", ";
    
    if(res.size() != 0)
      cout<<res[res.size()-1];
    
    cout<<"]"<<endl;
  }
}