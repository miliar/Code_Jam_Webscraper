#include <iostream>
#include <algorithm>

using namespace std;

const int MN = 1000 + 10;

int arr[MN];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i ++) {
		if (i == t - 1)
			int x = 5;
		int n, sum = 0, xsum = 0;
		cin >> n;
		for(int j = 0; j < n; j ++) {
			scanf("%d", &arr[j]);
			sum += arr[j];
			xsum = (xsum ^ arr[j]);
		}
		printf("Case #%d: ", i + 1);
		if (xsum)
			cout << "NO\n";
		else cout << sum - *min_element(arr, arr + n) << endl;
	}
	return 0;
}