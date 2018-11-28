#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
  ifstream input("B-large.in");
  ofstream outpt("output.txt");
  int T;
  input>>T;
  for(int counter = 1; counter<=T; counter++)
  {
      int c;
      int N;
      char co[36][4], o[28][3], arr[105];
      vector<char> my_vec;
      input>>c;
      for(int i =0; i<c; ++i)
      {
         input>>co[i];
      }
      int d;
      input>>d;
      for(int i =0; i<d; ++i)
      {
         input>>o[i];
      }
      input>>N;
      input>>arr;
      for(int i=0; i<N; ++i)
      {
         char ch = arr[i];
         my_vec.push_back(ch);
         for( int t = 0; t<c; t++)
         {
            if( co[t][0] == my_vec[my_vec.size()-1] && co[t][1] == my_vec[my_vec.size()-2] || co[t][0] == my_vec[my_vec.size()-2] && co[t][1] == my_vec[my_vec.size()-1])
            {
              my_vec.pop_back();
              my_vec.pop_back();
              my_vec.push_back(co[t][2]);
              t=-1;   
            }
         }        
         for( int t=0; t<d; t++)
         {
              if(o[t][0] == my_vec[my_vec.size()-1])
              {
                  for( int x=0; x<my_vec.size(); ++x)
                  {
                      if(my_vec[x] == o[t][1])
                       {
                         my_vec.clear();
                         break;        
                       } 
                  }      
              }
              else if(o[t][1] == my_vec[my_vec.size()-1])
              {
                  for( int x=0; x<my_vec.size(); ++x)
                  {
                      if(my_vec[x] == o[t][0])
                       {
                         my_vec.clear();
                         break;        
                       } 
                  }      
              }
         }      
      }
      
      outpt<<"Case #"<<counter<<": [";
      if(my_vec.size() >0)
       outpt<<my_vec[0];
      for(int x=1; x<my_vec.size(); ++x)
      {
         outpt<<", "<<my_vec[x];     
      }
      outpt<<"]"<<endl;
      
  }
  input.close();
  outpt.close();
  //system("pause");
}
