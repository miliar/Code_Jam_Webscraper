#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);
	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int s,x,r,n;
		double t;
		cin >> x >> s >> r >> t >> n;

		vector<int> b(n),e(n),w(n);
		int w_dis = 0;
		for (int i=0;i<n;i++) {
			cin >> b[i] >> e[i] >> w[i];
			w_dis += e[i] - b[i];
		}

		double res = 0;
		vector<int> vals;
		for (int i=0;i<x;i++) {
			int speed = 0;
			for (int j=0;j<n;j++) {
				if (b[j] <= i && i < e[j]) {
					speed = w[j];
				}
			}

			vals.push_back(speed);
		}

		sort(vals.begin(), vals.end());
		for (int i=0;i<vals.size();i++) {
			double time = 1.0 / (vals[i] + s);
			if (t > 0) {
				time = 1.0 / (vals[i] + r);
				if (time > t) {
					time = t + (1.0 - t * (vals[i] + r)) / (vals[i] + s);
					t = 0;
				}
				else t -= time;
			}
			res += time;
		}

		cout << "Case #" << (q+1) << ": " << setprecision (8) << res << endl;

	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
