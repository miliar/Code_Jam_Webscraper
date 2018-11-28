#include <iostream>
#include <vector>

using namespace std;

static const int MAX_N=11;

double matrix[MAX_N][MAX_N]; // matrice di transizione

void fill_matrix() {
  int n,m,k;

  for (n=0;n<MAX_N;n++) {
    matrix[n][0] = 1.0;
    int s=-1;
    double factminv=1;
    for (m=1;m<=n;++m) {
      factminv /= m;
      matrix[n][m] = matrix[n][m-1] + s * factminv;
      s=-s;
    }
  }
  
  for (n=0;n<MAX_N;n++) {
    double kfactinv=1.0;
    for (k=1;k<=n;++k) {
      kfactinv /= k;
      matrix[n][n-k] *= kfactinv;
    }
  }
  
  for (n=0;n<MAX_N;n++) {
    for (k=0;k<=n;++k) {
      cerr<<"matrix["<<n<<"]["<< k <<"]="<<matrix[n][k]<<endl;
    }
  }
  
}

double array[MAX_N];

void fill_array() {
  array[0] = 0.0;
  for (int n=1;n<MAX_N;++n) {
    double r=0.0;
    for (int i=0;i<n;++i) {
      r += matrix[n][i] * (1.0 + array[i]);
    }
    r += matrix[n][n];
    r /= (1.0 - matrix[n][n]);
    array[n]=r;
    cerr<<"array["<<n<<"] = "<<r<<endl;
  }
}

main() {
  //  fill_matrix();
  //fill_array();
  int T;
  cin >> T;
  for (int test=1;test<=T;test++) {
    int n=0;
    int N;
    cin >> N;
    for (int i=0;i<N;++i) {
      int k;
      cin >> k;
      if (k != i+1) n++;
    }
    cout<<"Case #"<<test<<": "<<double(n) <<endl;
  }
}
