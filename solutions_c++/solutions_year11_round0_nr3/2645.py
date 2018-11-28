#include <iostream>
#include <vector>
using namespace std;
int main() {
    int T;
    cin >> T;
    for(int z=1; z<=T; z++) {
        int N;
        cin >> N;
        vector<int> v;
        while(N--) {
	  int x;
	  cin >> x;
	  v.push_back(x);
        }
        int ile = (1<<(v.size()));
        int sol = -1;
        for(int i=1; i<ile-1; i++) {
	  
	  int xors[2] = {0,0};
	  int sums[2] = {0,0};
	  int act = 0;
	  vector<int> test;
	  int tmp = i;
	  while(act < v.size()) {
	      int ind = tmp&1;
	      if(!ind)
		test.push_back(v[act]);
	      xors[ind] ^= v[act];
	      sums[ind] += v[act];
	      tmp >>= 1;
	      act++;
	  }
	  if(xors[0] == xors[1])
	      sol = max(sol, max(sums[0], sums[1]));
        }
        cout << "Case #" << z << ": ";
        if(sol > 0)
	  cout << sol << '\n';
        else
	  cout << "NO\n";
    }
}