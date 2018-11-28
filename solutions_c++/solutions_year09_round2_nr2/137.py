#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n;
string num;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> num;
		
		int k = -1;
		for (int j = num.size() - 2; j >= 0; --j)
			if (num[j] < num[j + 1]) {
				k = j;
				break;
			}

		if (k == -1) {
			num = "0" + num;
			sort(num.begin() + 1, num.end());
			for (int j = 0; j < num.size(); ++j)
				if (num[j] > '0') {
					swap(num[0], num[j]);
					break;
				}
		}
		else {
			for (int j = num.size() - 1; j > k; --j)
				if (num[j] > num[k]) {
					swap(num[j], num[k]);
					break;
				}
			sort(num.begin() + k + 1, num.end());
		}
		cout << "Case #" << i + 1 << ": " << num << endl;
	}

	return 0;
}