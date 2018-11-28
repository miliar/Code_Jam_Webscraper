#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int xx = 1; xx <= n; ++xx) {
	int m, vv;
	cin >> m >> vv;
	vector<int> v(m+1);
	vector<int> g((m+1)/2);
	vector<int> c((m+1)/2);
	vector<int> y(m+1);
	for (int i = 1; i <= (m-1)/2; ++i)
	    cin >> g[i] >> c[i];
	for (int i = (m+1)/2; i <= m; ++i) {
	    cin >> v[i];
	    y[i] = 1000000000;
	}
	for (int i = (m-1)/2; i >= 1; --i) {
	    y[i] = 1000000000;
	    if (g[i]) {
		v[i] = v[2*i] && v[2*i+1];
		if (v[i]) {
		    y[i] = min(y[i], min(y[2*i], y[2*i+1]));
		} else {
		    if (c[i])
			y[i] = min(y[i], 1 + min(v[2*i] ? 0 : y[2*i],
						 v[2*i+1] ? 0 : y[2*i+1]));
		    y[i] = min(y[i], (v[2*i] ? 0 : y[2*i]) +
			       (v[2*i+1] ? 0 : y[2*i+1]));
		}
	    } else {
		v[i] = v[2*i] || v[2*i+1];
		if (!v[i]) {
		    y[i] = min(y[i], min(y[2*i], y[2*i+1]));
		} else {
		    if (c[i])
			y[i] = min(y[i], 1 + min(!v[2*i] ? 0 : y[2*i],
						 !v[2*i+1] ? 0 : y[2*i+1]));
		    y[i] = min(y[i], (!v[2*i] ? 0 : y[2*i]) +
			       (!v[2*i+1] ? 0 : y[2*i+1]));
		}
	    }
	}
	if (vv == v[1])
	    cout << "Case #" << xx << ": " << 0 << endl;
	else if (y[1] >= 1000000000)
	    cout << "Case #" << xx << ": IMPOSSIBLE" << endl;
	else
	    cout << "Case #" << xx << ": " << y[1] << endl;
    }
    return 0;
}
