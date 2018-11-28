
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int tcn=1;tcn<=T;tcn++) {
    //runs, cap, ngroups
    int R,k,N;
    cin >> R >> k >> N;
    vector<int> g(N);
    vector<int> nh(N);
    vector<int> cash(N);
    for (int i=0;i<N;i++)
      cin >> g[i];
    //quad time should be good enough
    for (int i=0;i<N;i++) {
      int S = 0;
      for (int grps = 0; grps <=N;grps++) {
	if (grps < N && (S + g[(i+grps)%N] <= k)) {
	  S += g[(i+grps)%N];
	} else {
	  nh[i] = (i+grps)%N;
	  cash[i] = S;
	  break;
	}
      }
    }
    long long sum = 0;
    int head = 0;
    for (int i =0;i<R;i++) {
      sum += cash[head];
      head = nh[head];
    }
    cout << "Case #" << tcn << ": " << sum << endl;
  }
}
