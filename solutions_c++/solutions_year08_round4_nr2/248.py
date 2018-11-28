#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define Forf(i,f,n) for(int i=(f);i<(n);++i)
#define For(i,n) for(int i=0;i<(n);++i)
#define foreach(it,m) for(typeof((m).begin()) it = (m).begin();it!=(m).end();++it) 

void solveit() {
  int N, M, A;
  cin >> N >> M >> A;

  Forf(i1,0,N+1) Forf(j1, 0, N+1)
    Forf(i2,0,M+1) Forf(j2, 0, M+1) {
    int ar = i1*j2-j1*i2;
    if (ar<0) ar=-ar;
    if (ar==A) {
      cout << 0 << " " << 0 << " " << i1 << " "
	   << i2 << " " << j1 << " " << j2 << endl;
      return;
    }
  }
  cout << "IMPOSSIBLE" << endl;
}


int main() {
  int N;
  cin >> N;
  For(c,N) {
    cout << "Case #" << (c+1) << ": ";
    solveit();
  }
}
