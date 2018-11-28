#include <iostream>

#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <sstream>
#include <cstdlib>


using namespace std;


char tiles[50][50];


int main()
{
  int T;
  
  cin>>T;
  
  vector<string> res_list;
  
  
  for(int t = 0 ;t < T; ++t)
  {
    int R,C;
    
    std::cin>>R>>C;
    
    for(int r = 0 ; r < R; ++r)
    {
      string ln;
      cin>>ln;
      for(int c = 0 ; c < C; ++c)
      {
        tiles[r][c] = ln[c];        
      }
    }
    
    bool is_possible = true;
    
    
    
    for(int r = 0 ; r < R; ++r)
    {
      for(int c = 0 ; c < C; ++c)
      {
        if (tiles[r][c] == '#')
        {
          if(r+1<R && c+1 <C &&
            tiles[r+1][c] == '#' &&
            tiles[r][c+1] == '#' &&
            tiles[r+1][c+1] == '#')
          {
            tiles[r][c] = '/';
            tiles[r+1][c] = '\\';
            tiles[r][c+1] = '\\';
            tiles[r+1][c+1] = '/';          
          }
          else
          {
            is_possible = false;
            break;
          }        
        }
      }
      if (is_possible == false)
      {
        break;
      }
    }
    
    stringstream ss;
    
    if(is_possible)
    {
      ss<<endl;
      for(int r = 0 ; r < R; ++r)
      {
        for(int c = 0 ; c < C; ++c)
        {
          ss<<tiles[r][c];
        }
        ss<<endl;
      }
    }
    else
    {
      ss<<endl<<"Impossible"<<endl;
    }
    res_list.push_back(ss.str());
  }
  
  for( int  t = 0 ; t < res_list.size() ; ++t)
    cout<<"Case #"<<t+1<<": " <<res_list[t];    
}