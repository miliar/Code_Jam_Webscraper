#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <cassert>

using namespace std;

#define Forf(i,f,n) for(int i=(f);i<(n);++i)
#define For(i,n) for(int i=0;i<(n);++i)
#define foreach(it,m) for(typeof((m).begin()) it = (m).begin();it!=(m).end();++it) 

typedef pair<int,int> PII;
typedef vector<int> VI;


#define NUM 102


void solveit() {
  int H, W, R;
  cin >> H >> W >> R;
  vector<vector<short> > v(H, W);
  v[0][0] = 1;
  For(i,R) {
    int x, y;
    cin >> x >> y;
    v[x-1][y-1] = -1;
  }
  For(i,H) For(j,W) {
    if (v[i][j]==-1) continue;

    int ki = i-2, kj = j-1;
    if (ki>=0 and kj>=0 and v[ki][kj]!=-1) v[i][j] += v[ki][kj];
    ki = i-1, kj = j-2;
    if (ki>=0 and kj>=0 and v[ki][kj]!=-1) v[i][j] += v[ki][kj];
    v[i][j] %= 10007;
  }
  cout << v[H-1][W-1] << endl;
}


int main() {
  int N;
  cin >> N;
  For(c,N) {
    cout << "Case #" << (c+1) << ": ";
    solveit();
  }
}
