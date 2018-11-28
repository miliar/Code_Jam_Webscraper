#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

int main()
{
  int cas;
  int N;

  cin >> N;

  for (cas = 1; cas <= N; cas++) {
    int M;
    cin >> M;

    vector<int> v;
    for (int i = 0; i < M; i++) {
      int mx = 0;
      for (int j = 0; j < M; j++) {
        char c;
        cin >> c;
        if (c == '1') {
          mx = j+1;
        }
      }
      v.push_back(mx);
    }

    int cnt = 0;
    for (int i = 0; i < M; i++) {
      if (v[i] > i+1) {
        int j;
        for (j = i+1; j < M; j++) {
          if (v[j] <= i+1) break;
        }
        for (; j > i; j--) {
          swap(v[j], v[j-1]);
          cnt++;
        }
      }
    }
    
    cout << "Case #" << cas << ": " << cnt << endl;
  }

  return 0;
}

