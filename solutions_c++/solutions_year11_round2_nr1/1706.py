#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;
int main() {
  int t;
  cin >> t;

  int mat[100][100];
  double wp[100];
  double spl_wp[100][100];
  double owp[100];

  double oowp[100];
  
  for (int i = 0; i < t; ++i) {
    int n;
    cin >> n;
    //cout << "N is " << n << endl;
    for (int j = 0; j < n; ++j) {
      int played = 0;
      int won = 0;
      for (int k = 0; k < n; ++k) {
        char c;
        cin >> c;
        //cout << j << " " << k << "Char " << c << ";\n";
        if (c == '0') {
          mat[j][k] = 0;
          played++;
        } else if (c == '1') {
          mat[j][k] = 1;
          played++;
          won++;
        } else {
          mat[j][k] = -1;
        }
      } // end cols 
      wp[j] = won * 1.0 / played;

      // spl_wp
      for (int k = 0; k < n; ++k) {
        if (mat[j][k] != -1) {
          spl_wp[j][k] = (won - mat[j][k]) * 1.0 / (played - 1);
        }
      } // end cols
    } // end rows

    for (int j = 0; j < n; ++j) {
      owp[j] = 0;
      int ctr = 0;
      for (int k = 0; k < n; ++k) {
        if (mat[j][k] != -1) {
          ctr++;
          owp[j] += spl_wp[k][j];
        }
      } // end col
      owp[j] /= ctr;
    } // end row

    for (int j = 0; j < n; ++j) {
      oowp[j] = 0;
      int ctr = 0;
      for (int k = 0; k < n; ++k) {
        if (mat[j][k] != -1) {
          ctr++;
          oowp[j] += owp[k];
        }
      } // end col
      oowp[j] /= ctr;
    } // end row

    cout << "Case #" << i + 1 << ":\n";
    for (int j = 0; j < n; ++j) {
      cout << setprecision (12)  << 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j] << '\n';
    }
  } // end test cases
}
