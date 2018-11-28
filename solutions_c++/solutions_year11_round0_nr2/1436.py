#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long ll;

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    int c, d, n;
    char conv[26][26];
    for(int i = 0; i < 26; ++i) fill_n(conv[i], 26, -1);
    cin >> c;
    for(int i = 0; i < c; ++i){
      char a, b;
      cin >> a >> b;
      cin >> conv[a-'A'][b-'A'];
      conv[b-'A'][a-'A'] = conv[a-'A'][b-'A'];
    }
    bool opp[26][26];
    for(int i = 0; i < 26; ++i) fill_n(opp[i], 26, false);
    cin >> d;
    for(int i = 0; i < d; ++i){
      char a, b;
      cin >> a >> b;
      opp[a-'A'][b-'A'] = opp[b-'A'][a-'A'] = true;
    }
    char list[100];
    int cur = 0;
    cin >> n;
    for(int i = 0; i < n; ++i){
      cin >> list[cur++];
      while(cur >= 2){
        if(conv[list[cur-2] - 'A'][list[cur-1] - 'A'] != -1){
          list[cur-2] = conv[list[cur-2] - 'A'][list[cur-1] - 'A'];
          --cur;
        }
        else{
          break;
        }
      }
      bool clear = false;
      for(int j = 0; j < cur-1; ++j)
        if(opp[list[j] - 'A'][list[cur-1] - 'A']){
          clear = true;
          break;
        }
      if(clear)
        cur = 0;
    }
    cout << "Case #" << k + 1 << ": ";
    cout << "[";
    for(int i = 0; i < cur; ++i){
      if(i > 0) cout << ", ";
      cout << list[i];
    }
    cout << "]" << endl;
  }

  return 0;
}
