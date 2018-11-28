#include <iostream>
#include <vector>

using namespace std;

int calc(int n, int s, int p, vector<int> &v) {
  int ret = 0;
  int cand = 0;
  for (int i=0; i<n; i++) {
    int vv = v[i];
    int rest = vv - p;
    if (rest < 0) continue;
    int d = rest / 2;
    int st = p-2;

    if (d > st) {
	    ret++;
    } else if (d == st) {
	    if (cand < s) cand++;
    } 
  }

  return ret + cand;
}

int main(void) {
	int t;

	cin >> t;
	for (int i=0; i<t; i++) {
		int n, s, p;

		cin >> n >> s >> p;
		vector<int> v;
		for (int j=0; j<n; j++) {
			int tj;
			cin >> tj;
			v.push_back(tj);
		}
		cout << "Case #" << (i+1) << ": ";
		cout << calc(n, s, p, v);	
		cout << endl;
	}

}
