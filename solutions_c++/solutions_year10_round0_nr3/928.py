#include <iostream>
#include <vector>

using namespace std;

#define lng long long

lng B[1000];

vector<vector<lng> > mult(const vector<vector<lng> >& A,
                          const vector<vector<lng> >& B) {
  int n = A.size();
  vector<vector<lng> > ret(n, vector<lng>(n, 0));
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      for(int k = 0; k < n; k++) {
        ret[i][j] += A[i][k] * B[k][j];
      }
    }
  }
  return ret;
}


int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    lng R, K, N;
    cin >> R >> K >> N;
    for(int i = 0; i < N; i++) cin >> B[i];
    
    int sz = N + 1;
    vector<vector<lng> > A(sz, vector<lng>(sz, 0));
    for(int i = 0; i < N; i++) {
      int j;
      long long sm = 0;
      for(j = 0; j < N; j++) {
        sm += B[(i + j) % N];
        if(sm > K) {
          sm -= B[(i + j) % N];
          break;
        }
      }
      A[(i + j) % N][i] = 1;
      A[N][i] = sm;
    }
    A[N][N] = 1;
    
    vector<vector<lng> > res(sz, vector<lng>(sz, 0));
    for(int i = 0; i < sz; i++) res[i][i] = 1;
    for(int i = 30; i >= 0; i--) {
      res = mult(res, res);
      if(R & 1 << i) res = mult(res, A);
    }

    cout << "Case #" << t << ": " << res[N][0] << endl;
  }
}
