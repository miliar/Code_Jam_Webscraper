#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  int N;
  cin >> N;
  for (int i = 0; i < N; i++){
    int S, Q;
    cin >> S;
    vector<string> engines;
    char buf[101];      
    cin.getline(buf, 101);
    for (int j = 0; j < S; j++){
      cin.getline(buf, 101);
      string engine(buf);
      engines.push_back(engine);
    }
    cin >> Q;
    cin.getline(buf, 101);
    vector<string> queries;
    for (int j = 0; j < Q; j++){
      char buf[101];
      cin.getline(buf, 101);
      string query(buf);
      queries.push_back(query);
    }

    vector<vector<int> > sw(Q+1, vector<int>(S, 0));
    for (int j = 1; j <= Q; j++){
      for (int k = 0; k < S; k++){
        if (queries[j-1] == engines[k]){
          sw[j][k] = INT_MAX;
        }else{
          int min = INT_MAX;
          for (int l = 0; l < S; l++){
            if (k == l){
              if (sw[j-1][l] < min){
                min = sw[j-1][l];
              }
            }else{
              if ((sw[j-1][l] < INT_MAX) && (sw[j-1][l]+1 < min)){
                min = sw[j-1][l]+1;
              }
            }
          }
          sw[j][k] = min;
        }
      }
    }

    int min = INT_MAX;
    /*
    for (int j = 0; j <= Q; j++){
      for (int k = 0; k < S; k++){
        cout << sw[j][k] << ',';
      }
      cout << endl;
    }
    */

    for (int j = 0; j < S; j++){
      if (sw[Q][j] < min){
        min = sw[Q][j];
      }
    }


    cout << "Case #" << (i+1) << ": " << min << endl;
  }

  return 0;
}
