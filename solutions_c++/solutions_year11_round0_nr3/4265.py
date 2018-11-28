#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
	long int n, c, temp, total_sum, left_sum, right_sum, patrick_left_sum, patrick_right_sum, sean, test_case;
	vector<long int> pieces;
	cin >> n;
	test_case = 1;
	while (n--) {
		typedef vector<long int>::iterator it;
		sean = 0;
		pieces.clear();
		cin >> c;
		for (int i = 0; i < c; i++) {
			cin >> temp;
			pieces.push_back(temp);
		}
		total_sum = accumulate(pieces.begin(), pieces.end(), 0);
		sort(pieces.begin(), pieces.end());
		for (it i = pieces.begin(); i != pieces.end() - 1; ++i) {
			left_sum = accumulate(pieces.begin(), i + 1, 0);
			right_sum = total_sum - left_sum;
			patrick_left_sum = patrick_right_sum = 0;
			it p = pieces.begin();
			while (p != i + 1) {
				patrick_left_sum = patrick_left_sum ^ (*p);
				p++;
			}
			while (p != pieces.end()) {
				patrick_right_sum = patrick_right_sum ^ (*p);
				p++;
			}
			if (patrick_left_sum == patrick_right_sum) {
				sean = right_sum;
				break;
			}
		}
		cout << "Case #" << test_case++ << ": ";
		if (sean)
			cout << sean << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}