#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define REPP(i,m,n) for (int i = m; i < m+n; i++)
#define REPR(i,a,b) for (int i = a; i <= b; i++)

#define foreach(it,type) for (typeof(type.begin()) it = type.begin(); it != type.end(); it++)

#define MAX(n,m) (((n) > (m)) ? (n) : (m))
#define MIN(n,m) (((n) < (m)) ? (n) : (m))

typedef vector<int> vi;

int main(int argc, char* argv[]) {
  ifstream fin (argv[1]);

  int T;
  fin >> T;

	REP(t,T) {
		int N,L,H;
		fin >> N >> L >> H;

		vi nums(N);
		REP(n,N) {
			fin >> nums[n];
		}

		bool found = false;
		int ans;
		REPR(f,L,H) {
			bool yes = true;
			REP(j,nums.size()) {
				if (nums[j] % f == 0 || f % nums[j] == 0) {

				} else {
					yes = false;break;
				}
			}
			if (yes) {
				found = true;
				ans = f;
				break;
			}
		}

		cout << "Case #" << t+1 << ": ";
		if (found) {
			cout << ans << endl;
		} else {
			cout << "NO" << endl;
		}
	}

  return 0;
}
