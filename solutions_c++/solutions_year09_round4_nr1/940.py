
#include <iostream>

using namespace std;


int main() {

	int T, N;
	char c;
	cin >> T;
	int num[40];

	for (int t = 1; t <= T; t++) {
		cin >> N;
		for (int i = 0; i < N; i++) {
			int last_one = 0;
			int k;
			for (k=0; k < N; k++) {
				cin >> c;
				if (c=='1') last_one = k+1;
			}
			num[i] = last_one;
		}

		int swaps = 0;
		int tmp;
		for (int i = 0; i < N; i++) {
			if (num[i] > i+1) {
				int k = i+1;
				while(num[k] > i+1) k++;
				for(int j = k; j>i; j--) {
					tmp = num[j];
					num[j] = num[j-1];
					num[j-1] = tmp;
					swaps++;
				}
			}
		}
		cout << "Case #" << t << ": " << swaps << endl;
	}


	
	return 0;

}


