#include <iostream>
#include <algorithm>
using namespace std;
int main(int n, char** p) {
	int N;
	cin >> N;
	for(int i=0; i<N; ++i) {
		int LEN;
		cin >> LEN;
		int ROBO[2] = {1,1};
		int ROBOT[2] = {0,0};
		int T = 0;
		for(int j=0; j<LEN; ++j) {
			char S[2];
			int P;
			cin >> S;
			cin >> P;
			int slct = S[0] == 'O'?0:1;
			if(T - ROBOT[slct] >= abs(P - ROBO[slct])) {
				ROBO[slct] = P;
				ROBOT[slct] = ++T;
			} else {
				ROBOT[slct] = T = abs(P - ROBO[slct]) - (T-ROBOT[slct]) + 1 + T;
				ROBO[slct] = P;
			}
		}
		cout << "Case #"<<i+1 << ": " << T<<endl;
	}
}
	
