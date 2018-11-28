// gcj2012-2.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";

		int n, s, p;
		cin >> n >> s >> p;
		vector<int> h;
		copy_n(istream_iterator<int>(cin), n, back_inserter(h));
		
		int ans = 0;

		for_each(h.begin(), h.end(), 
			[&](int sum) {
				if (sum < p) return;
				if (sum + 2 >= 3 * p) ++ans; else
				if (sum + 4 >= 3 * p && s > 0) {
					++ans;
					s--;
				}
			}
		);

		cout << ans << endl;
	}
	return 0;
}

