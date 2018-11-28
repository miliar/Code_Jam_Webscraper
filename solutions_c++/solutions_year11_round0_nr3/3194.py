#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int z=0;z<T;z++) {
		
		// read in, and compute xor and sum over all
		int xorAll=0, sumAll=0;
		int N;
		cin >> N;
		vector<int> Ci;
		for (int i=0;i<N;i++) {
			int tmp;
			cin >> tmp;
			Ci.push_back(tmp);
			xorAll ^= tmp;
			sumAll += tmp;
		}

		if (xorAll!=0) {
			cout << "Case #" << z+1 << ": " << "NO" << endl;
		} else {
			// exhaust all  combinations , nn-2 in fact
			vector<int> vec(N,0);
			vec[0] = 1;
			int maxV = 0;

			int sumVec; // loop criteria
			do {

				// iterate through the partition
				int xor1=0,sum1=0,xor0=0;
				for (int j=0;j<N;j++) {
					if (vec[j]==1) {
						xor1 ^= Ci[j];
						sum1 += Ci[j];
					} else
						xor0 ^= Ci[j];
				}
				int sum0 = sumAll-sum1;

				//
				if (xor1==xor0) {
					int tmp;
					if (sum1>sum0)
						tmp = sum1;
					else
						tmp = sum0;
					if (tmp>maxV)
						maxV = tmp;
				}

				// add 1 
				for (int j=0;j<N;j++) {
					if (vec[j]==0) {
						vec[j]=1;
						break;
					} else
						vec[j] = 0;
				}
				// judge if out of loop		
				sumVec = 0;
				for (int j=0;j<N;j++)
					sumVec += vec[j];

			} while (sumVec < N);
			cout << "Case #" << z+1 << ": " << maxV << endl;
		} // end if else: cannot split into two even piles
	} // end one case
}