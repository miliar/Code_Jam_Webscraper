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
		int t;
		cin >> t;

		vector<vector<bool>> vals;
		vector<int> nums;
		for (int i=0;i<t;i++) {
			int temp;
			cin >> temp;
			nums.push_back(temp);
			vector<bool> flags;
			while (temp > 0) {
				flags.push_back(temp % 2);
				temp /= 2;
			}
			vals.push_back(flags);
		}

		int res = -1;
		bool flag = false;
		for (int i=1;i<(1<<nums.size())-1;i++) {
			int left=0,right=0,leftsum=0,rightsum=0;
			for (int j=0;j<nums.size();j++) {
				if ((i & (1 << j)) != 0) {
					left ^= nums[j];
					leftsum += nums[j];
				}
				else {
					right ^= nums[j];
					rightsum += nums[j];
				}
			}

			if (left == right) {
				flag = true;
				res = max(res, max(leftsum,rightsum));
			}
		}

		cout << "Case #" << (q+1) << ": ";
		if (!flag) {
			cout << "NO" << endl;
		}
		else {
			cout << res << endl;
		}
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}