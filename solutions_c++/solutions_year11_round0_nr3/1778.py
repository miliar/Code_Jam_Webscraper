#include <iostream>

using namespace std;

int t, n, sum, c, Min, q;

int main(){
	cin >> t;
	for (int _i = 0; _i < t; ++_i){
		cin >> n;
		sum = 0;
		q = 0;
		Min = 1000000;
		for  (int i = 0; i < n; ++i){
			cin >> c;
			sum += c;
			q ^= c;
			Min = min(Min, c);
		}
		cout << "Case #" << _i + 1 << ": ";
		if (q == 0){
			cout << sum - Min << endl;
		}
		else{
			cout << "NO" << endl;
		}
	}
	return 0;
}