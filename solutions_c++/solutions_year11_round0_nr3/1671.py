#include <iostream>

using namespace std;

void main (){
	int test;
	cin >> test;
	

	for (int t = 0; t < test; t++){
		int n;
		cin >> n;

		int sol = 0;
		int small = 100000000;
		int sum = 0;

		for (int i = 0; i < n; i++){
			int next;
			cin >> next;
			sol = (sol ^ next);
			small = (small < next) ? small : next;
			sum += next;
		}

		// Output
		
		cout << "Case #" << t+1 << ": ";
		if (sol == 0){
			cout << sum - small;
		}
		else {
			cout << "NO";
		}

		if (t != test - 1){
			cout << endl;
		}
	}
}