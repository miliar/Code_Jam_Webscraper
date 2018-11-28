#include <iostream>
#include <fstream>
#include <vector>
#include <set>
using namespace std;

int main(){

  ifstream in;
  ofstream out;
  
  in.open("b.in");
  
  out.open("b.out");
  
  int T;
  
  in >> T;
  
  for(int t=1; t<=T; t++){
  
      int N,S,p;
      
      in >> N >> S >> p;
  
      vector<int> vals;
      vector<int> as;
      vector<int> bests;
      vals.resize(N);
      as.resize(N);
      bests.resize(N);
      for(int i=0; i<N; i++){
        in >> vals[i];
        if(vals[i]%3 == 2){
          as[i] = (vals[i]+1)/3;
          bests[i] = as[i];
        }
        else if(vals[i]%3 == 1){
          as[i] = vals[i] / 3;
          bests[i] = as[i] + 1;
        }
        else{
          as[i] = vals[i] / 3;
          bests[i] = as[i];
        }
      }      
      
      int c = 0;
      for(int i=0; i<N; i++)
         if(bests[i] >= p)
          c++;
      
      for(int i=0; i<N; i++){
        if(S>0 && vals[i] % 3 != 1 && vals[i] >= 2 && vals[i] <= 28 && bests[i] < p){
          if(bests[i]+1 >= p){
            c++;
            S--;
          }
        }
      
      }
      out << "Case #" << t << ": " << c << endl;
  }
  return 0;
}
