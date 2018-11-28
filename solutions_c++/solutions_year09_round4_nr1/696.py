#include <iostream>
#include <vector>
#include <string>
#include <boost/algorithm/string.hpp>
#include <algorithm>
#include <iterator>




using namespace std;
using namespace boost;


int main(int argc, char **argv) {
	int T;
	cin >> T;
	for (int t = 1;t <= T;t++) {
		int n;
		cin >> n;
		vector<int> v(n);
		for (int i = 0;i < n;i++)
		{
			string str;
			cin >> str;
			trim_right_if(str,is_any_of("0"));
			v[i] = str.size();
		}

		int count = 0;
		for (int i = 0;i < n;i++) {
			if (v[i] > i + 1) {
				int j;
				for (j = i + 1;j < n;j++)
					if (v[j] <= i + 1)
						break;
				for (int k = j;k >= i + 1;k--)
				{
					swap(v[k],v[k-1]);
					count++;
				}
			}
		}
		cout << "Case #" << t << ": " << count << endl;
	}
}

