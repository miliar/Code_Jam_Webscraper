#include <iostream>

using namespace std;

int main (int argc, char * const argv[]) {
	
	long long T, N, C, min, total, i, j, k, sum[30];
    bool cry;
	
	cin >> T;
	for (i=0; i<T; i++) {
		cin >> N;
		memset(sum, 0, sizeof(long long)*30);
		min = 100000000;
		total = 0;
		for (j=0; j<N; j++) {
			cin >> C;
			total += C;
			k=0;
			if ( C < min) min = C;
			do {
				sum[k] = (sum[k] + (C % 2)) % 2;
				k++;
				C = C /2;
			} while (C >0);
		}
		cry = false;
		for (j=0; j<30; j++) {
			if (sum[j] !=0) {
				cry = true;
			}
		}
		
		cout << "Case #" << i+1 << ": ";
		if (cry) {
			cout << "NO" <<endl	;
		} else {
			cout << total - min<<endl;
		}

	}
    return 0;
}
