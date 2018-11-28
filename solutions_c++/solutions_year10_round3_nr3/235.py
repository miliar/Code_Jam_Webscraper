#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <utility>

using namespace std;

#define FOR_EACH(it_var, container) \
  FOR_EACH_RANGE(it_var, (container).begin(), (container).end())

#define FOR_EACH_R(it_var, container) \
  FOR_EACH_RANGE(it_var, (container).rbegin(), (container).rend())

#define FOR_EACH_RANGE(it_var, begin, end) \
  for (typeof(begin) it_var = (begin); it_var != (end); ++it_var)

void zmain() {
  int mat[512][512];
  int R[512][512];
  memset(mat, 0, sizeof(int)*512*512);
  memset(R, 0, sizeof(int)*512*512);
  int a, b; cin >> a >> b;
  for (int i=0;i<a;i++) {
    string S; cin >> S;
    //cout << "\n";
    for (int j=0;j<b;j+=4) {
      char x = (S[j/4] >= 'A') ? (10 + S[j/4] - 'A') : (S[j/4] - '0');
      mat[i][j]   = (x & 8) ? 1 : 0;
      mat[i][j+1] = (x & 4) ? 1 : 0;
      mat[i][j+2] = (x & 2) ? 1 : 0;
      mat[i][j+3] = (x & 1) ? 1 : 0;
      //for (int l=0;l<4;++l)
      //cout << mat[i][j+l];
    }
  }
  map<int, int> s;
  int max = 10;
  while (max > 0) {
    max = 0;
    int X = 0, Y = 0;
    for (int i=a-1;i>=0;--i) {
      //cout << "\n";
      for (int j=b-1;j>=0;--j) {
        //cout << mat[i][j];
        if (mat[i][j] <= 1) {
          R[i][j] = 1;
          if ((i < a-1) && (j < b-1)) {
            if ((mat[i][j] + mat[i][j+1]) == 1)
              if ((mat[i+1][j] + mat[i][j]) == 1)
                if (mat[i+1][j+1] == mat[i][j])
                  R[i][j] =
                    std::max(R[i][j],
                             std::min(R[i][j+1] + 1,
                                      std::min(R[i+1][j] + 1,
                                               R[i+1][j+1] + 1)));
          }
          if (R[i][j] >= max) {
            max = R[i][j];
            X = i; Y = j;
          }
        } else {
          R[i][j] = 0;
        }
        //cout << i << ", " << j << " :: " << R[i][j] << "\n";;
      }
    }
    //return;
    //cout << max << " :: " << X << ", " << Y << "\n";
    if (max > 0) {
      s[max]++;
      for (int i=0;i<max;++i)
        for (int j=0;j<max;++j)
          mat[X+i][Y+j] = 3;
    }
  }
  //return;
  cout << s.size() << "\n";
  FOR_EACH_R(it, s)
    cout << it->first << " " << it->second << "\n";
}

int main() {
  int k; cin >> k;
  for (int i=0;i<k;++i) {
    cout << "Case #" << (i+1) << ": ";
    zmain();
  }
}
