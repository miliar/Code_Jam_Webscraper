#include <iostream>
#include <fstream>
using namespace std;

int a[100];

int calc(int n, int s, int p, int* a){
  int ret = 0;
  for(int i=0; i<n; ++i) {
    int b = a[i] - p;
    if(b<0) continue;
    if(b >= 2*(p-1)) ret++;
    else {
      if(b >= 2*(p-2) && s>0) {
	ret ++;
	s--;
      }
    }
  }
  return ret;
}

int main(int argc, char** argv) {
  int t, n, s, p;
  ifstream fin(argv[1]);
  fin >> t;
  for(int i=1; i<=t; ++i) {
    fin >> n >> s >> p;
    for(int j=0; j<n; ++j) fin >> a[j];
    cout << "Case #" << i << ": " << calc(n, s, p, a) << endl;
  }
  fin.close();
  return 0;
}
