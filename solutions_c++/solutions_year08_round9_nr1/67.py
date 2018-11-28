#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct cow { int a, b, c; };

int main()
{
    int t;
    cin >> t;
    for (int x = 1; x <= t; ++x) {
	int n;
	cin >> n;
	vector<cow> v(n);
	for (int i = 0; i < n; ++i)
	    cin >> v[i].a >> v[i].b >> v[i].c;
	int y = 0;
	for (int i = 0; i < n; ++i) {
	    vector<pair<int, int> > q;
	    for (int j = 0; j < n; ++j) {
		if (v[i].a >= v[j].a &&
		    10000 - v[i].a >= v[j].b + v[j].c) {
		    q.push_back(make_pair(v[j].b, -1));
		    q.push_back(make_pair(10000 - v[i].a - v[j].c, 1));
		}
	    }
	    sort(q.begin(), q.end());
	    int z = 0;
	    for (typeof(q.begin()) j = q.begin(); j != q.end(); ++j) {
		z -= j->second;
		if (y < z)
		    y = z;
	    }
	}
	cout << "Case #" << x << ": " << y << endl;
    }
    return 0;
}
