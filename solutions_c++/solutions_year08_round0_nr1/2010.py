#include <iostream>
#include <string>

using namespace std;

int minimum_switches_,S,Q,iteration_depth_=0,case_num_=0;
string* engines_;
string* queries_;

void exhaustiveSolve(int engine_num, int query_num)
{
    iteration_depth_++;
    
    for(int i=0;i<S;i++)
    {
      if(i==engine_num)//prevent infinite recursion loops
        continue;
        
      for(int j=query_num;j<Q;j++)
      {
        if(queries_[j]==engines_[i])
        {//have to switch
//          if(S==2 || j!=(query_num+1))
          if(j-query_num>S-2)
          {//ensure you're not chosing a case where you switch and then switch back
            exhaustiveSolve(i,j);
            iteration_depth_--;
          }
          break;
        }
                
        //if this is reached then this is a solution
        if((j+1)==Q && iteration_depth_ < minimum_switches_)
        {
          minimum_switches_=iteration_depth_;           
        }
      }
    }
    
    return;     
}

void solve()
{
    if(case_num_!=1)
    {
      cout << endl;
    } 
    
    for(int i=0;i<S;i++)
    {
      for(int j=0;j<Q;j++)
      {
        if(queries_[j]==engines_[i])
        {
          if(j!=0)
          {//prevent cases where you are switching on the first outbound
           //for slight optimization
            exhaustiveSolve(i,j);
            iteration_depth_--;
          }
          break;
        }
        
        //if this is reached then this is a solution
        if((j+1)==Q && iteration_depth_ < minimum_switches_)
        {
          minimum_switches_=iteration_depth_;           
        }
      }

      if(minimum_switches_==0)
      {//prevent unnecessary iterations
        break;
      }  
    }
   
    cout << "Case #" << case_num_ << ": " << minimum_switches_;
    
    return;
}

int main (int argc, const char** argv) 
{
    string temp;
    int N;
    cin >> N;
    for(int i=0;i<N;i++)
    {
      cin>>S;
      getline(cin, temp);
      string* engines = new string[S];
      for(int i=0;i<S;i++)
      {
          getline(cin, engines[i]);
      }
      cin >> Q;
      getline(cin, temp);
      string* queries = new string[Q];
      for(int i=0;i<Q;i++)
      {
          getline(cin, queries[i]);
      }

      engines_ = engines;
      queries_ = queries;
      minimum_switches_ = Q;
      case_num_++;
      solve();
    }
    
    return 0;
}
