#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);
	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int n;
		cin >> n;

		vector<bool> halls;
		vector<int> num;
		for (int i=0;i<n;i++) {
			char ch;
			cin >> ch;
			halls.push_back(ch == 'B');
			int temp;
			cin >> temp;
			num.push_back(temp);
		}

		int res = 0;

		int prev = 0;
		bool prev_hall = halls[0];
		int cur_true=1,cur_false=1;

		for (int i=0;i<n;i++) {
			int val = 1;
			if (halls[i]) {
				val += abs(num[i] - cur_true);
				cur_true = num[i];
			}
			else {
				val += abs(num[i] - cur_false);
				cur_false = num[i];
			}

			if (prev_hall != halls[i]) {
				val = max(1, val-prev);
				prev = 0;
			}

			res += val;

			prev += val;
			prev_hall = halls[i];
		}

		cout << "Case #" << (q+1) << ": " << res << endl;
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}