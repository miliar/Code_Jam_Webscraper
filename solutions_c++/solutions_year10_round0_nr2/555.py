#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
long long gcd(long long a, long long b){
	long long tmp;
	while (a != 0){
		tmp = b; b = a; a = tmp;
		a = a % b;
	}
	return b;
}

int main(){
	int C;
	scanf("%d", &C);
	int N;
	for (int m = 0; m < C; ++m){
		scanf("%d", &N);
		vector<long long> arr(N);
		long long y, res, tmp;
		for (int i = 0; i < N; ++i) {
			cin >> arr[i];
		}
		sort(arr.begin(), arr.end());
		tmp = arr[0];
		//cout << arr[0] << arr[1] << endl;
		for (int i = 0; i < N - 1; ++i){
			arr[i] = arr[i + 1] - arr[i];
			//cout << arr[i] << " ";
		}
		//cout << endl;
		for (int i = 0; i < N - 1; ++i){
			if (i == 0) 
				y = gcd(arr[0], arr[0]);
			else
				y = gcd(y, arr[i]);
			//cout << y << " ";
		}
		//cout << endl << y << endl;
		if (tmp % y == 0)
			res = 0;
		else 
			res = y - tmp % y;
		cout << "Case #" << m + 1 << ": " << res << endl;
		//printf("Case #%d: %lld\n", m + 1, res);
	}
	return 0;
}