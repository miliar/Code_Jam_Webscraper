#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> Vi;
typedef vector<double> Vd;
typedef vector<Vi> Mi;

int main() {
  int t,n;
  cin >> t;
  for(int i = 0; i < t; ++i) {
    cin >> n;
    Mi m(n,Vi(n));
    Vd wp(n);
    Vi ops(n);
    for(int j = 0; j < n; ++j) {
      int sum = 0;
      int tot = 0;
      for(int k = 0; k < n; ++k) {
	char c;
	cin >> c;
	if(c != '.') {
	  int num = c-'0';
	  m[j][k] = num;
	  sum += num;
	  ++tot;
	}
	else m[j][k] = -1;
      }
      wp[j] = double(sum)/tot;
      ops[j] = tot;
    }
    Vd owp(n);
    for(int j = 0; j < n; ++j) {
      int tot1 = 0;
      for(int k = 0; k < n; ++k) {
	if(k != j and m[j][k] != -1) {
	  int sum = 0;
	  int tot = 0;
	  for(int z = 0; z < n; ++z) {
	    if(z != j and m[k][z] != -1) {
	      sum += m[k][z];
	      ++tot;
	    }
	  }
	  owp[j] += double(sum)/tot;
	  ++tot1;
	}
      }
      owp[j] /= tot1;
    }
    Vd oowp(n);
    for(int j = 0; j < n; ++j) {
      for(int k = 0; k < n; ++k) {
	if(k != j and m[k][j] != -1) {
	  oowp[j] += owp[k];
	}
      }
      oowp[j] /= ops[j];
    }
    cout << "Case #" << i+1 << ":" << endl;
    for(int j = 0; j < n; ++j) cout << 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j] << endl;
  }
}