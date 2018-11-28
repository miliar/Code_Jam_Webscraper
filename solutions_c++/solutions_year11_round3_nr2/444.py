#include <iostream>
#include <vector>
#define sz(a) ((int)(a).size())
using namespace std;

int testcase;
long long L, T, N, C;
vector<long long> a;
long long b[10000];

int main(int argc, char *argv[]) {
  cin >> testcase;
  for (int tn = 1; tn <= testcase; ++tn) {
    cin >> L >> T >> N >> C;
    for (int i = 0; i < C; ++i) {
      cin >> b[i];
    }
    a.clear();
    while(true) {
      for (int i = 0; i < C; ++i) {
        a.push_back(b[i]);
        if(sz(a) == N) break;
      }
      if(sz(a) == N) break;
    }

    long long minv=21000000000000;
    if (L == 0) {
      minv = 0;
      for (int i = 0; i < N; ++i) {
        minv = minv + a[i] * 2;
      }
    } else if ( L == 1) {
      for (int k = 0; k < N; ++k) {
        long long now = 0;
        long long boostpos = T/2;
        int flag = 0;
        int pos = 0;
        for (int i = 0; i < N; ++i) {
          pos += a[i];
          if (flag == 0 && pos >= boostpos && k == i) {
            now -= min(pos - boostpos, a[i]);
            flag = 1;
          }
          now += a[i] * 2;
        }
        // cout << k << " " << now << endl;
        minv = min(minv, now);
      }
    } else if( L==2) {
      for (int i = 0; i < N-1; ++i) {
        for (int j = i+1; j < N; ++j) {
          long long now = 0;
          long long boostpos = T/2;
          int flag = 0;
          int pos = 0;
          for (int k = 0; k < N; ++k) {
            pos += a[k];
            if (flag == 0 && pos >= boostpos && k == j) {
              now -= min(pos - boostpos, a[j]);
              flag = 1;
            }
            if (flag == 0 && pos >= boostpos && k == i) {
              now -= min(pos - boostpos, a[i]);
              now -= a[j];
              flag = 1;
            }

            now += a[k] * 2;
          }
          minv = min(minv, now);
        }
      }
    }
    cout << "Case #" << tn << ": " << minv << endl;
  }
    
  return 0;
}
