#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

int main() {
  
  
  ifstream in("in.txt");
  ofstream out("out.txt");
  int N,k1;
  string n;
  char min,c, max;
  int mk;
  vector<char> V;
  in >> N;
  for (int i = 1; i <= N; i++) {
    in >> n;
    if (n.size() == 1) {
      out<<"Case #"<<i<<": "<<n<<"0"<<endl;
      continue;
    }
    for (int j = n.size() - 2; j >= 0; j--) {
      min = n[j];
      max = '9' + 1;
      mk = j;
      for (int k = j + 1; k < n.size(); k++) {
          if (n[k] > min and n[k] <= max) {
              max = n[k];
              mk = k;
          }
      }
      if (mk != j) {
        V.clear();
        c = n[j];
        n[j] = n[mk];
        n[mk] = c;
        for (int k = j + 1; k < n.size(); k++) {
          V.push_back(n[k]);
        }
        sort(V.begin(),V.end());
        for (int k = j + 1; k < n.size(); k++) {
          n[k] = V[k - j - 1];
        }
        out<<"Case #"<<i<<": "<<n<<endl;
        break;
      }
      else {
        if (j == 0) {
          V.clear();
          for (int k = 0; k < n.size(); k++) {
            V.push_back(n[k]);
          }
          sort(V.begin(),V.end());
          n.clear();
          if (V[0] == '0'){
            for (k1 = 0; k1 < V.size(); k1++) {
              if (V[k1] != '0') {
                V[0] = V[k1];
                break;
              }
            }
            V[k1] = '0';
            sort(V.begin() + 1, V.end());
          }
          n += V[0];
          n += '0';
          for (int k = 1; k < V.size(); k++)
            n += V[k];
          out<<"Case #"<<i<<": "<<n<<endl;
          break;
       }
     }
   }
 }
}
            
          
        
                  
        
      