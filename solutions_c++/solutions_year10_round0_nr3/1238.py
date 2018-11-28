#include <iostream>
#include <vector>
using namespace std;
int main(){
	int T;
	scanf("%d", &T);
	long long R, k, N;
	for (int m = 0; m < T; ++m){
		cin >> R >> k >> N;
		vector<long long> arr(N);
		for (long long i = 0; i < N; ++i){
			cin >> arr[i];
		}
		vector<long long> profit(N);
		vector<long long> end(N);
		for (long long i = 0; i < N; ++i){
			long long sum = 0;
			long long ii = i;
			long long t = 0;
			while (sum + arr[ii] <= k && t < N){
				sum += arr[ii];
				ii = (ii + 1) % N;
				t++;
			}
			profit[i] = sum;
			end[i] = ii;
		}
		long long res = 0;
		long long begin = 0;
		for (long long i = 0; i < R; ++i){
			res += profit[begin];
			begin = end[begin];
		}
		cout << "Case #" << m + 1 << ": " << res << endl;
		//cprintf("Case #%lld: %lld\n", m + 1, res);
	}
	return 0;
}