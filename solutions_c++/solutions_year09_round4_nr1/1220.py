#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;


int main() {
  int C;
  cin >> C;
  for(int c =0; c < C;++c ) {
    int N;
    cin >> N;
    
    vector<int> sol;
    for(int i=0; i < N; ++i) {
      string l;
      cin >> l;
      int j=l.size();
      for(; j > 0 && l[j -1] != '1'; --j);
      sol.push_back(j);
    }

    int cost=0;
    for(int i=0; i < N; ++i) {
      for(int b=sol.size()-1; b >=0; --b) {
	if( sol[b] <= b+1) continue;
	int g=b;
	while(sol[g] > b+1) ++g;
	cost += (g-b);;
	while(g > b) {
	  swap( sol[g], sol[g-1] );
	  --g;
	}
      }
    }
    cout << "Case #" << (c+1) << ": " << cost << endl;
  }
}
