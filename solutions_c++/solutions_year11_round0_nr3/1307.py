#include <iostream>

using namespace std;

int main(){
	int T;
	int N, C;
	int x, sum;

	cin >> T;
	for (int cnt = 1; cnt <= T; cnt++){
		cin >> N;
		x = 0;
		sum = 0;
		int mymin = 1000001;
		for (int i=0; i<N; ++i){
			cin >> C;
			x = x^C;
			sum += C;
			if (mymin > C)
				mymin = C;
		}
		cout << "Case #" << cnt << ": ";
		if (x!=0)
			cout << "NO" << endl;
		else 
			cout << sum - mymin << endl;

	}

	return 0;
}
