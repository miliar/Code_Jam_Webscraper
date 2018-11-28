#include <iostream>
using namespace std;


bool check(int pd, int pg) {
  if (pg != 0 && pg != 100) return true;
  if (pd == 0 && pg == 0) return true;
  if (pd == 100 && pg == 100) return true;
  return false;
} 

bool solve(int n, int pd, int pg) {
  for (int d = 1; d <= n; d++) {
	if (d * pd % 100 != 0) continue;
	if (check(pd, pg)) return true;
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  
  for (int i = 0; i < T; i++) {
	int N, Pd, Pg;
	cin >> N >> Pd >> Pg;
	bool f = solve(N, Pd, Pg);
	cout << "Case #" << i + 1 << ": ";
	if (f) {
	  cout << "Possible" << endl;
	} else {
	  cout << "Broken" << endl;
	}
  }
  return 0;
}
	
