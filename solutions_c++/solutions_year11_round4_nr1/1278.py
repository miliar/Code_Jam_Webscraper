#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <map>

using namespace std;

typedef pair<int, int> walk;

double accelerate(double v, double d, double va, double &t) {
	double tt = d/va;
	if(tt > t) {
		tt = t + (d - t*(va))/v;
		t = 0;
	}
	else
		t -= tt;
	
	return tt;
}

void spike() {
	int x, s, r, t, n;
	cin >> x >> s >> r >> t >> n;
	
	vector<walk> walks;
	int sum = 0;
	for(int i = 0; i < n; i++) {
		int b, e, w;
		cin >> b >> e >> w;
		walks.push_back(make_pair(w, e-b));
		sum += (e-b);
	}

	walks.push_back(make_pair(0, x-sum));

	sort(walks.begin(), walks.end());
	//reverse(walks.begin(), walks.end());

	double run = t;
	double time = 0;
	for(int i = 0; i < walks.size(); i++) {
		walk &w = walks[i];	

		time += accelerate(w.first + s, w.second, w.first + r, run);
	}
	cout.precision(10);
	cout << time << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);

	int z;
	cin >> z;
	for (int i = 0; i < z; i++) {
		cout << "Case #" << i+1 << ": ";
		spike();
	}
}