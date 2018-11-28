#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		int A, B;
		cin >> A >> B;

		int result = 0;
		for (int i = A; i <= B; ++i) {
			int len = ((int)log10(i)) + 1;
			set<int> s;
			int last = i;
			int powNum = pow(10, len - 1);
			for (int j = 1; j < len; ++j) {
				if (last % 10 == 0)
					last /= 10;
				else {
					last = last / 10 + powNum * (last % 10);
					if (last <= B && last >= A && last > i)
						s.insert(last);
				}
			}
			result += s.size();
		}
		cout << "Case #" << testcase << ": " << result << endl;
	}
}
