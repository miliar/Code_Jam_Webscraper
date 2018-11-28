/**
 * candy-splitting.cpp
 *
 * @date May 7, 2011
 * @author Arpan
 **/

#include <iostream>
//#include <vector>

//#define DEBUG

using namespace std;

/*void toBinary(int number, vector<bool>& binary) {
#ifdef DEBUG
	int number_orig = number;
#endif
    while(number) {
        binary.insert(binary.begin(), (number % 2) ? true : false); // should be the same as push_back
        number /= 2;
    }
#ifdef DEBUG
    cout << "toBinary(" << number_orig << ") = ";
    for (int access = 0; access < binary.size(); access++)
        cout << binary[access];
    cout << endl;
#endif
}*/

int main(int argc, char* argv[]) {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		long C[N];
		long total = 0;
		for(int i = 0; i < N; i++) {
			cin >> C[i];
			total += C[i];
		}

		// brute-force: this will work for the small case only! BigTheta(2^n)
#ifdef DEBUG
		long setCount = 1 << N;
#endif
		long setCountBy2 = 1 << (N - 1);
#ifdef DEBUG
		cout << "N = " << N << ", setCount = " << setCount << ", setCount/2 = " << setCountBy2 << endl;
#endif

		long maxNum = -1;
		long maxSum = -1;
		// for each possible set partition
		for(long num = 1; num < setCountBy2; num++) {
			// sum one partition (the sum of the other partition can be obtained using total)
			long sum0 = 0, sum1 = 0, fake_sum0 = 0, fake_sum1 = 0;
			for(int i = 0; i < N; i++) {
				if((1 << i) & num) {
					sum1 += C[i];
					fake_sum1 = fake_sum1 ^ C[i];
				}
				else {
					sum0 += C[i];
					fake_sum0 = fake_sum0 ^ C[i];
				}
			}

#ifdef DEBUG
			cout << num
				 << "\tsum0 = " << sum0 << "\tsum1 = " << sum1
				 << "\tfake_sum0 = " << fake_sum0 << "\tfake_sum1 = " << fake_sum1
				 << endl;
#endif

			if(fake_sum0 == fake_sum1) {
				if(sum0 > maxSum || sum1 > maxSum) {
					maxSum = max(sum0, sum1);
					maxNum = num;
				}
			}

		}

		cout << "Case #" << t << ": ";
		if(maxSum != -1)
			cout << maxSum << endl;
		else
			cout << "NO" << endl;
	}
}
