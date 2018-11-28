#include <iostream>

#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))

using namespace std;

int arr[15000];
int dist[15000];
int length[15000];

int main() {
  int t; cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    int n; cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> dist[i] >> length[i];
      arr[i] = -1;
    }
    int love_d; cin >> love_d;

    arr[0] = dist[0];
    bool success = false;

    for (int i = 0; i < n; ++i) {
      if (arr[i] == -1) continue; // not reachable
      int max_dist = dist[i] + arr[i];
      if (max_dist >= love_d) success = true;
      for (int j = i + 1; j < n; ++j) {
        if (dist[j] <= max_dist) {
          arr[j] = MAX(arr[j], MIN(dist[j] - dist[i], length[j]));
        } else {
          break;
        }
      }
    }

    if (success) {
      cout << "Case #" << case_num << ": YES" << endl;
    } else {
      cout << "Case #" << case_num << ": NO" << endl;
    }
  }
  return 0;
}