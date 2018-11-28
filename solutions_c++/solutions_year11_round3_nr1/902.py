#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<numeric>
#include<sstream>
using namespace std;


string str(int i) 
{
  stringstream ss;
  ss << i;
  string ret;
  ss >> ret;
  return ret;
}



int main() {
    ifstream input("in.txt");
    ofstream out("out.txt");
    int T;
    input >> T;
    for(int z = 0; z < T; z++)
    {
      int N, C;
      input >> N >> C;
      vector<string> v(N);
      v.clear();
      for(int i = 0; i < N; i++)
      {
        input >> v[i];
      }
      for(int i = 0; i < N; i++)
      {
        for(int j = 0; j < v[i].size(); j++)
        {
          if(v[i][j] == '#') {
            if(j + 1 < v[i].size() && i + 1 < N)
            {
             if(v[i][j+1] == '#' && v[i+1][j] == '#' && v[i+1][j+1] == '#')
             {
              v[i][j] = '/';
              v[i][j+1] = '\\';
              v[i+1][j] = '\\';
              v[i+1][j+1] = '/';
             }
             else {
              out<<"Case #"<<(z + 1)<<":"<<endl; 
              out<<"Impossible"<<endl;
              goto hell;
             }
            }
            else {
              out<<"Case #"<<(z + 1)<<":"<<endl; 
              out<<"Impossible"<<endl;
              goto hell;
            }
          }
        }
      }
      for(int i = 0; i < N; i++)
        for(int j = 0; j < v[i].size(); j++)
           if(v[i][j] == '#')
           {
              out<<"Case #"<<(z + 1)<<":"<<endl; 
              out<<"Impossible"<<endl;
              goto hell;
           }
      out<<"Case #"<<(z + 1)<<":"<<endl; 
      for(int i = 0; i < N; i++){
        for(int j = 0; j < v[i].size(); j++)
          out<<v[i][j];
        out<<endl;
      }    
      hell:;
    }
 }
