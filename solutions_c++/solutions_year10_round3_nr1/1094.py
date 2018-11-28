#include <iostream>
#include <vector>

using namespace std;

int main (int argc, char * const argv[]) {
    int T,N;
	cin >> T;

	for(int i = 1;i<=T;i++) {
		cin >> N;
		vector<long> vA(N+1),vB(N+1);
		long A,B;
		long crosses = 0;
		for(int j = 1;j<=N;j++) {
			cin >> A >> B;
			vA[j] = A;
			vB[j] = B;
			for(int k = 1;k<j;k++) {
				if((A < vA[k]) && (B > vB[k]) || ((A > vA[k]) && (B < vB[k])))
					crosses += 1;
			}
		}
		cout << "Case #" << i<< ": " << crosses;
		if(i < T) { cout << endl;}
	}
	
    return 0;
}
