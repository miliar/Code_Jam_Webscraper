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
      int N, mi, ma;
      input >> N >> mi >> ma;
      vector<int> f(N);
      for(int i = 0; i < N; i++)
        input >> f[i];
      for(int i = mi; i <= ma; i++)
      {
        int isOK = 1;
        for(int j = 0; j < f.size(); j++) {
    
          if(!(f[j] % i == 0 or i % f[j] == 0))
          {
            isOK = 0;
            break;
          }
        }
        if(isOK) {
          out<<"Case #"<<(z+1)<<": "<<i<<endl;
          goto hell;
        }
      }
      out<<"Case #"<<(z+1)<<": NO"<<endl;
      hell:;
    }
 }
