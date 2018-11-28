#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int arr[1005];

int main() {
	int T;
	cin >> T;
	for(int z = 1; z <= T; z++) {
		int N;
		cin >> N;
		int x = 0, total = 0;
		for(int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
			x ^= arr[i];
			total += arr[i];
		}
		cout << "Case #" << z << ": ";
		if(x)
			cout << "NO";
		else {
			sort(arr, arr+N);
			cout << total - arr[0];
		}
		cout << endl;
	}
	return 0;
}
