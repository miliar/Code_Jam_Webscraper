

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {

  ifstream in("input");
  ofstream out("output");
  ofstream o("in");
  
  int T;
  in >> T;
  for(int k = 0; k < T; k++){

    long long L, t, N, C;
    in >> L >> t >> N >> C;
    o << L << " " << t << " " << N << " " << C << " ";
    vector<double> a(C);
    for(int i = 0; i < C; i++){
      in >> a[i];
      o << a[i] << " ";
    }
    o << "\n";
    
    vector<double> d(N); 
    for(int j = 0, i = 0; i < N; j++, i++){
      if(j == C) j = 0;
      d[i] = a[j];        
    }
    
    double time = 0;
    
    double sum = 0;
    for(int i = 0; i < N; i++) 
    { 
      sum += d[i];
    }
    
    if(sum > t*(0.5)){

      double no_booster = t*0.5;

      vector<double> d_with_boosters;
      double dim = no_booster;
      for(int i = 0; i < N; i++){
        dim -= d[i]; 
        if(dim < 0){  
          for(int j = 0; j < N-i; j++){
            d_with_boosters.push_back(d[i+j]);
          }
          d_with_boosters[0] = -dim;
          break;  
        }
      }

      time = t;

      if(d_with_boosters.size() > L){
        for(int i = 0; i < L; i++){
          int max_j = 0;
          for(int j = 0; j < d_with_boosters.size(); j++){
            if(d_with_boosters[j] > d_with_boosters[max_j])
            { 
              max_j = j;
            }
          }
          time += d_with_boosters[max_j];
          d_with_boosters.erase(d_with_boosters.begin()+max_j);
        }

        int sum = 0;
        for(int i = 0; i < d_with_boosters.size(); i++){
          sum += d_with_boosters[i];
        }
        time += sum/(0.5);

      }else{
        double sum = 0;
        for(int i = 0; i < d_with_boosters.size(); i++){
          sum += d_with_boosters[i]; 
        }
        time += sum;
      }
    
    }else time = sum/(0.5);
    
    out << "Case #" << k+1 << ": " << int(time) << "\n";
  }


  return 0;
}



