#include <iostream>
#include <string>

using namespace std;

const int SMAX = 100;
const int QMAX = 1000;

int main(void){
  int t;
  int s, q;
  string query, name[SMAX];
  bool used[SMAX];
  int cnt, res;

  cin >> t;
  for(int k = 0; k < t; ++k){
    cin >> s;
    getline(cin, name[0]);
    for(int i = 0; i < s; ++i)
      getline(cin, name[i]);

    res = 0;
    cnt = s;
    fill_n(used, s, false);

    cin >> q;
    getline(cin, query);
    for(int i = 0; i < q; ++i){
      getline(cin, query);

      for(int j = 0; j < s; ++j)
        if(!used[j] && name[j] == query){
          if(cnt == 1){
            cnt = s;
            fill_n(used, s, false);
            ++res;
          }

          used[j] = true;
          --cnt;
        }
    }

    cout << "Case #" << k+1 << ": " << res << endl;
  }

  return 0;
}
