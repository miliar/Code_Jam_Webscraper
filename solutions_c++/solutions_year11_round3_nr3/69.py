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
		int n,l,h;
		
		cin >> n >> l >> h;
		vector<int> vals;
		for (int i=0;i<n;i++) {
			int temp;
			cin >> temp;
			vals.push_back(temp);
		}

		int res = -1;
		for (int i=l;i<=h;i++) {
			bool flag = true;

			for (int j=0;j<vals.size();j++) {
				if (vals[j] % i != 0 && i % vals[j] != 0) {
					flag = false;
					break;
				}
			}
			if (flag) {
				res = i;
				break;
			}
		}

		cout << "Case #" << (q+1) << ": ";
		if (res == -1) cout << "NO" << endl;
		else cout << res << endl;
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}