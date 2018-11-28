#include <iostream>

using namespace std;

int main (long long int argc, char const *argv[])
{
	long long int t;
	cin >> t;
	for (long long int i = 0; i < t; i++) {
		long long int r, k, n;
		cin >> r >> k >> n;
		long long int v[1000] = {0};
		long long int start[1000] = {0};
		long long int group[1000] = {0};
		for (long long int j = 0; j < n; j++) {
			cin >> group[j];
		}
		long long int index = 0;
		long long int sum = 0;
		long long int ans = 0;
		long long int t = 0;
		start[0] = 1;
		v[0] = 0;
		for (long long int j = 0; j < r; j++) {
			if (j != 0 && v[j] == 0) {
				start[index] = j+1;
				v[j] = ans;
			//	cout << j << ' ' << v[j] << ' ' << index << endl;
			}
			sum += group[index];
			t ++;
			ans += group[index];
			if ((index == n-1 && sum+group[0] > k || index < n-1 && sum+group[index+1] > k) || t >= n) {
				if (start[(index+1)%n] == 0) {
					t = 0;
					sum = 0;
				} else {
					long long int s = start[(index+1)%n] - 1;
					long long int a = j - s + 1;
					long long int b = r - s;
			//		cout << b << ' ' << s << ' ' << v[j]<<' '<<sum<<' '<<v[s];
					
					ans = (b/a)*(v[j]+sum-v[s]);
					if (b%a != 0){
						ans += v[s+b%a]-v[s];
					}
					ans += v[s];
					break;
				}
			} else {
				j--;
			}
			index++;
			if (index == n) index = 0;
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}