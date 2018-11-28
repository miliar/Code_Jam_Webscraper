#include <iostream>
using namespace std;

#define FOR(i, x) for(int i = 0; i < (x); i++)

int main() {
	int T;
	ios::sync_with_stdio(false);
	cin >> T;
	FOR(TC, T) {
		int n, sur, p, out = 0;
		cin >> n >> sur >> p;
		FOR(i, n) {
			int t;
			cin >> t;
			int mna = t / 3, mxa = (t + 2) / 3,
					mns = (t + 1) / 3 - 1, mxs = mns + 2;
			if(mna >= 0 && mxa <= 10 && mxa >= p)
				out++;
			else if(mns >= 0 && mxs <= 10 && mxs >= p && sur > 0)
			{
				sur--;
				out++;
			}
		}
		cout << "Case #" << TC + 1 << ": " << out << endl;
	}
	return 0;
}
