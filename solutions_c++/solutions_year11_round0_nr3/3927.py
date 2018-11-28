#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int ac,char* av[])
{
	int n; cin >> n;
	for (int i=1; i<=n; i++) {
		int c; cin >> c;
		vector<int> v;
		int x = 0, s=0, min = 0x7fffffff;
		for (int j=0; j<c; j++) {
			int e; cin >> e;
			v.push_back(e);
			x = x ^ e;
			s += e;
			if (e < min) min = e;
		}
		if (x != 0) {
			cout << "Case #" << i << ": NO" << endl;
		} else {
			// nth_element(v.begin(), v.begin(), v.end());
			cout << "Case #" << i << ": " << s-min << endl;
		}
	}
	return 0;
}

