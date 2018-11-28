
#include <iostream>
#include <vector>
using namespace std;


int main() {
	long long T, C, D;

	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> C >> D;
		long long P[C], V[C];
		for(int i = 0; i < C; i++) cin >> P[i] >> V[i]; 

		long long mint = 0;

		for(int i = 0; i < C; i++) {
			long long nb = 0;
			for(int j = i; j < C; j++) {
				nb += V[j];
				long long dd = P[j] - P[i];
				long long tt = (nb - 1)*D - dd;
				if(tt > mint) mint = tt;
	//			cerr << "# " << i << " " << j << " " << nb << " " << dd << " " << tt << endl;
			}
		}
		cout << "Case #" << t << ": " << mint/2 << (mint%2?".5":"") << endl;

	}


}
