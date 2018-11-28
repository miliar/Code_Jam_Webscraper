#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef long long LL;
int main() {
    int T;
    cin >> T;
    for(int z=1; z<=T; z++) {
        cerr << z << endl;
        LL L, N, C;
        LL t;
        cin >> L >> t >> N >> C;
        vector<LL> len;
        len.resize(C);
        for(int i=0; i<len.size(); i++)
	  cin >> len[i];
        LL sol = 0;
        priority_queue<LL> Q;
        for(int i=0; i<N; i++) {
	  LL act = len[i%(int)len.size()];
	  act *= 2;
	  if(t == 0) {
	      Q.push(act);
	  }
	  else if(act > t) {
	      sol += t;
	      act -= t;
	      t = 0;
	      Q.push(act);
	  }
	  else {
	      t -= act;
	      sol += act;
	  }
        }
        while(L > 0 && !Q.empty()) {
	  LL x = Q.top();
	  Q.pop();
	  L--;
	  sol += x/2;
        }
        while(!Q.empty()) {
	  sol += Q.top();
	  Q.pop();
        }
        cout << "Case #" << z << ": " << sol << '\n';
    }
    return 0;
}