#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++) {
		cout << "Case #" << tc << ": ";
		int N;
		cin >> N;
		vector<int> v(N);
		int sum2=0, sum=0;
		for(int i=0; i<N; i++) {
			cin >> v[i];
			sum2 ^= v[i];
			sum += v[i];
		}
		if(sum2) {
			cout << "NO" << endl;
		} else {
			sort(v.begin(), v.end());
			cout << sum-v[0] << endl;
		}
	}
}
