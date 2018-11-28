#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void out(vector<int> &v)
{
	for(vector<int>::iterator i = v.begin(); i != v.end(); ++i) {
		cout << *i << ' ';
	}
	cout << endl;
}

int calc(int t, vector<int> &dt, vector<int> &at)
{
	int st = dt.size() - 1;
	int res = 0;
	for(int i = at.size() - 1; i >= 0 && st >= 0; --i) {
		if(dt[st] >= at[i] + t) {
			++res;
			--st;
		}
	}
	return res;
}

int main(void)
{
	int n, t, na, nb;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		cin >> t;
		cin >> na >> nb;
		vector<int> dtA, dtB, atA, atB;
		for(int i = 0; i < na; ++i) {
			int hour, min; char dummy;
			cin >> hour >> dummy >> min;
			dtA.push_back(hour * 100 + min);
			cin >> hour >> dummy >> min;
			atB.push_back(hour * 100 + min);
		}
		for(int i = 0; i < nb; ++i) {
			int hour, min; char dummy;
			cin >> hour >> dummy >> min;
			dtB.push_back(hour * 100 + min);
			cin >> hour >> dummy >> min;
			atA.push_back(hour * 100 + min);
		}
		sort(dtA.begin(), dtA.end());
		sort(dtB.begin(), dtB.end());
		sort(atA.begin(), atA.end());
		sort(atB.begin(), atB.end());

		cout << "Case #" << nn+1 << ": " << na-calc(t, dtA, atA) << ' ' << nb-calc(t, dtB, atB) << endl;
	}
	return 0;
}
