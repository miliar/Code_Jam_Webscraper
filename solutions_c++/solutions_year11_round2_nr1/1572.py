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
      int N;
      input >> N;
      vector<bool> a[N];
      vector<string> V(N);
      vector<double> ww(N), owp(N);
      for(int i = 0; i < N; i++)
        input >> V[i];
      for(int i = 0; i < N; i++) {
        int sum = 0;
        int w = 0;
        vector<bool> hasp(N,0);
        fill(hasp.begin(),hasp.end(),0);
        for(int j = 0; j < N; j++) {
          if(V[i][j] != '.') { sum++; hasp[j] = 1; }
          if(V[i][j] == '1') w++;
        }
        double wp = w/double(sum); 
        double ave = 0;
        for(int k = 0; k < N; k++) {
          int sum1 = 0;
          int w1 = 0;
          if(k != i and hasp[k]) {
            for(int j = 0; j < N; j++){
              if(j != i) {
                if(V[k][j] == '1' or V[k][j] == '0') sum1++;
                if(V[k][j] == '1') w1++;
              }
            }
            ave += w1/double(sum1)/(sum);
             
          }
         
        }
        ww[i] = wp;
        owp[i] = ave;
        a[i] = hasp;
      }
      out<<"Case #"<<(z+1)<<":"<<endl;
      for(int i = 0; i < N; i++) {
        double s = 0;
        for(int j = 0; j < N; j++)
          if(i != j && a[i][j]) s += owp[j]/accumulate(a[i].begin(), a[i].end(), 0);
        
        out<<0.25*ww[i] + 0.5*owp[i] + 0.25*s<<endl;
      }
    }
}
