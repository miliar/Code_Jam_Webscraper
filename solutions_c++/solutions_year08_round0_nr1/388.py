
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int nbswitch(vector<string> S, vector<string> Q) {
  int R = 0;
  map<string, int> M;

  for(int i = 0; i < Q.size(); i++) {
    M[Q[i]]++;
    bool change = true;
    for(int k = 0; k < S.size(); k++)
      change = change && (M[S[k]] != 0);

    if(change) {
      R++;
      M.clear();
      M[Q[i]]++;
    }
  }
  return R;
}

int main() {
  string tmp;
  getline(cin, tmp);
  int N = atoi(tmp.c_str());
  for(int i = 1; i <= N; i++) {
    getline(cin, tmp);
    int S = atoi(tmp.c_str());
    vector<string> SE(S);
    for(int k = 0; k < S; k++) 
      getline(cin, SE[k]);
    getline(cin, tmp);
    int Q = atoi(tmp.c_str());
    vector<string> QU(Q);
    for(int k = 0; k < Q; k++)
      getline(cin, QU[k]);

    cout << "Case #" << i << ": " << nbswitch(SE, QU) << endl;
  }
}
