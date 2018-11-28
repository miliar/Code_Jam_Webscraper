#include <iostream>
#include <algorithm>
using namespace std;

int N,S,p,t[100];

int mem[101][101];

int rec(int th, int s) {
  if(th == N) {
    return s == S ? 0 : -1;
  }
  int &res = mem[th][s];
  if(res != -2) return res;
  res = -1;
  for(int i = 0; i <= 10; ++i) {
    int a = i;
    for(int j = 0; j <= 2; ++j) {
      int b = i+j;
      if(b > 10) break;
      if(s == S && j == 2) break;
      for(int k = j; k <= 2; ++k) {
	int c = i+k;
	if(c > 10) break;
	if(s == S && k == 2) break;
	if(3*i+j+k == t[th]) {
	  int tmp = rec(th+1,s+(k==2));
	  if(tmp != -1)
	    res = max(res,tmp+(i+k>=p));
	}
      }
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    cin >> N >> S >> p;
    for(int i = 0; i < N; ++i) cin >> t[i];
    fill(mem[0],mem[101],-2);
    cout << "Case #" << tc << ": " << rec(0,0) << endl;
  }
  return 0;
}
